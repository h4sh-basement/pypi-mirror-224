/****************************************************************************
** Copyright 2020 The Open Group
** Copyright 2020 Bluware, Inc.
**
** Licensed under the Apache License, Version 2.0 (the "License");
** you may not use this file except in compliance with the License.
** You may obtain a copy of the License at
**
**     http://www.apache.org/licenses/LICENSE-2.0
**
** Unless required by applicable law or agreed to in writing, software
** distributed under the License is distributed on an "AS IS" BASIS,
** WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
** See the License for the specific language governing permissions and
** limitations under the License.
****************************************************************************/

#ifndef DATA_PROVIDER_H
#define DATA_PROVIDER_H

#include <OpenVDS/OpenVDS.h>
#include "IO/IOManager.h"
#include "IO/File.h"
#include <map>
#include <memory>
#include <mutex>
#include <cassert>

struct DataTransfer : public OpenVDS::TransferDownloadHandler
{
  DataTransfer(int64_t offset = 0)
    : offset(offset)
    , size(0)
  {}

  void HandleObjectSize(int64_t size) override
  {
    this->size = size;
  }

  void HandleObjectLastWriteTime(const std::string &lastWriteTimeISO8601) override
  {
    this->lastWriteTime = lastWriteTimeISO8601;
  }

  void HandleMetadata(const std::string &key, const std::string &header) override
  {
  }

  void HandleData(std::vector<uint8_t> &&data) override
  {
    this->data = std::move(data);
  }

  void Completed(const OpenVDS::Request &request, const OpenVDS::Error &error) override
  {
    (void)request;
    (void)error;
  }

  int64_t offset;
  int64_t size;
  std::string lastWriteTime;
  std::vector<uint8_t> data;
};

struct DataProvider
{
  DataProvider(OpenVDS::File *file)
    : m_file(file)
    , m_ioManager(nullptr)
  {
  }

  DataProvider(const std::string &url, OpenVDS::IOManager *ioManager, OpenVDS::Error &error)
    : m_file(nullptr)
    , m_ioManager(ioManager)
    , m_url(url)
  {
    if (m_ioManager)
    {
      auto syncTransfer = std::make_shared<DataTransfer>();
      auto syncRequest = m_ioManager->ReadObjectInfo("", syncTransfer);
      if (syncRequest->WaitForFinish(error))
      {
        m_size = syncTransfer->size;
        m_lastWriteTime = syncTransfer->lastWriteTime;
      }
    }
  }

  bool Read(void* data, int64_t offset, int32_t length, OpenVDS::Error& error) const
  {
    if (m_file)
    {
      return m_file->Read(data, offset, length, error);
    }
    
    if (m_ioManager)
    {
      auto dataTransfer = std::make_shared<DataTransfer>();
      auto request = m_ioManager->ReadObject("", dataTransfer, {offset, offset + length});
      if (!request->WaitForFinish(error))
      {
        return false;
      }
      memcpy(data, dataTransfer->data.data(), std::min(size_t(length), dataTransfer->data.size()));
      return true;
    }

    error.code = -1;
    error.string = "Invalid dataprovider, no file nor ioManager provided";
    return false;
  }

  int64_t Size(OpenVDS::Error &error) const
  {
    if (m_file)
      return m_file->Size(error);

    if (m_ioManager)
      return m_size;

    error.code = -1;
    error.string = "Invalid dataprovider, no file nor ioManager provided";
    return 0;
  }

  std::string LastWriteTime(OpenVDS::Error &error) const
  {
    if (m_file)
      return m_file->LastWriteTime(error);

    if (m_ioManager)
      return m_lastWriteTime;

    error.code = -1;
    error.string = "Invalid dataprovider, no file nor ioManager provided";
    return "";
  }

  static std::string URLDecode(const std::string & url)
  {
    std::string result;
    result.reserve(url.size());
    int len = int(url.size());

    for(int i = 0; i < len; i++)
    {
      char c = url[i];

      if(c == '+')
      {
        c = ' ';
      }
      else if(c == '%' && i + 2 < len)
      {
        char temp[3] = { url[i+1], url[i+2] };
        char *end;
        char decoded = char(strtol(temp, &end, 16));
        if(end == temp + 2)
        {
          c = decoded;
          i += 2;
        }
      }

      result.push_back(c);
    }
    return result;
  }

  std::string GetPathFromURL(std::string url) const
  {
    // Skip protocol if present
    auto start = url.find_first_of(":/?#");
    start = (start == std::string::npos || url[start] != ':') ? 0 : start + 1;
    // Skip host if present
    if(url.compare(start, 2, "//") == 0)
    {
      start = url.find_first_of("/?#", start + 2);
    }
    // Stop at query or fragment
    auto stop = url.find_first_of("?#", start);
    return (stop == std::string::npos) ? url.substr(start) : url.substr(start, stop - start);
  }

  std::string GetPath() const
  {
    return m_file ? m_file->FileName() : URLDecode(GetPathFromURL(m_url));
  }

  std::string GetFileOrObjectName() const
  {
    std::string path = GetPath();
    auto pos = path.find_last_of(":/\\");
    return (pos == std::string::npos) ? path : path.substr(pos + 1);
  }

  std::unique_ptr<OpenVDS::File> m_file;
  std::unique_ptr<OpenVDS::IOManager> m_ioManager;
  const std::string m_url;
  int64_t m_size = 0;
  std::string m_lastWriteTime;
};

struct DataView
{

  DataView(DataProvider &dataProvider, int64_t pos, int64_t size, bool isPopulate, OpenVDS::Error &error)
    : m_fileView(nullptr)
    , m_pos(0)
    , m_size(0)
    , m_ref(0)
  {
    if (dataProvider.m_file)
    {
      m_fileView = dataProvider.m_file->CreateFileView(pos, size, isPopulate, error);
    }
    else if (dataProvider.m_ioManager)
    {
      m_pos = pos;
      m_size = size;
      int64_t end = pos + size;
      const int chunk_size = 1 << 23; //8 MB
      for (int64_t i = pos; i < end; i+= chunk_size)
      {
        int64_t chunk_end = std::min(i + chunk_size, end);
        m_transfers.push_back(std::make_shared<DataTransfer>(i - pos));
        m_requests.push_back(dataProvider.m_ioManager->ReadObject("", m_transfers.back(), {i, chunk_end - 1}));
      }
    }
    else
    {
      error.code = 2;
      error.string = "Missing data provider";
    }
  }
  ~DataView()
  {
    if (m_fileView)
      OpenVDS::FileView::RemoveReference(m_fileView);
  }

  const void * Pointer(OpenVDS::Error &error)
  {
    if (m_fileView)
      return m_fileView->Pointer();
    if (m_requests.size())
    {
      if (m_requests.size() == 1)
      {
        if (m_requests[0]->WaitForFinish(m_error))
          m_data = std::move(m_transfers[0]->data);
      }
      else
      {
        m_data.resize(m_size);
        OpenVDS::Error reqError;
        for (int i = 0; i < int(m_requests.size()); i++)
        {
          if (!m_requests[i]->WaitForFinish(reqError))
          {
            m_error = reqError;
            break;
          }
          auto& transfer = *m_transfers[i];
          assert(transfer.size == int64_t(transfer.data.size()));
          assert(transfer.offset + transfer.data.size() <= m_data.size());
          memcpy(m_data.data() + transfer.offset, transfer.data.data(), transfer.data.size());
        }
      }
      m_requests = std::vector<std::shared_ptr<OpenVDS::Request>>();
      m_transfers = std::vector<std::shared_ptr<DataTransfer>>();
    }
    if (m_error.code)
    {
      error = m_error;
      return nullptr;
    }
    return m_data.data();
  }

  int64_t Pos() const
  {
    if (m_fileView)
      return m_fileView->Pos();
    return m_pos;
  }

  int64_t Size() const
  {
    if (m_fileView)
      return m_fileView->Size();
    return m_size;
  }

  void ref()
  {
    m_ref++;
  }

  bool deref()
  {
    m_ref--;
    return m_ref == 0;
  }

  OpenVDS::FileView *m_fileView;
  std::vector<uint8_t> m_data;
  int64_t m_pos;
  int64_t m_size;
  std::vector<std::shared_ptr<OpenVDS::Request>> m_requests;
  std::vector<std::shared_ptr<DataTransfer>> m_transfers;
  OpenVDS::Error m_error;
  int m_ref;
};

struct DataRequestInfo
{
  int64_t offset;
  int64_t size;

  bool operator==(const DataRequestInfo &other) const
  {
    return offset == other.offset && size == other.size;
  }
  bool operator!=(const DataRequestInfo &other) const
  {
    return offset != other.offset || size != other.size;
  }
  bool operator<(const DataRequestInfo &other) const
  {
    if (offset == other.offset)
      return size < other.size;
    return offset < other.offset;
  }
};

class DataViewManager
{
public:
  DataViewManager(DataProvider &dataProvider, int64_t prefetchLimit)
    : m_dataProvider(dataProvider)
    , m_memoryLimit(prefetchLimit)
    , m_usage(0)
  {
  }

  std::shared_ptr<DataView> acquireDataView(DataRequestInfo &dataRequestInfo, bool isPopulate, OpenVDS::Error& error)
  {
    std::unique_lock<std::mutex> lock(m_mutex);

    if (m_error.code)
    {
      error = m_error;
      return nullptr;
    }

    auto it = m_dataViewMap.lower_bound(dataRequestInfo);
    if (it == m_dataViewMap.end() || it->first != dataRequestInfo)
    {
      // if we've called acquire and it's not already in the map then we need to initiate the request and not just stick it in the queue
      auto dataView = std::make_shared<DataView>(m_dataProvider, dataRequestInfo.offset, dataRequestInfo.size, true, m_error);
      it = m_dataViewMap.insert(it, { dataRequestInfo, dataView });
      m_usage += dataRequestInfo.size;
    }

    return it->second;
  }

  void addDataRequests(const std::vector<DataRequestInfo>& dataRequestInfos)
  {
    std::unique_lock<std::mutex> lock(m_mutex);

    if (m_error.code == 0)
    {
      m_requests.insert(m_requests.end(), dataRequestInfos.begin(), dataRequestInfos.end());
      prefetchUntilMemoryLimit();
    }
  }

  void retireDataViewsBefore(const DataRequestInfo& dataRequestInfo)
  {
    std::unique_lock<std::mutex> lock(m_mutex);

    auto it = m_dataViewMap.begin();
    while (it != m_dataViewMap.end() && it->first < dataRequestInfo)
    {
      m_usage -= it->second->Size();
      it = m_dataViewMap.erase(it);
    }

    prefetchUntilMemoryLimit();
  }

  void retireAllDataViews()
  {
    std::unique_lock<std::mutex> lock(m_mutex);

    m_dataViewMap.clear();
    m_usage = 0;

    prefetchUntilMemoryLimit();
  }

private:
  typedef std::map<DataRequestInfo, std::shared_ptr<DataView>> DataViewMap;

  DataProvider &m_dataProvider;
  std::vector<DataRequestInfo> m_requests;
  DataViewMap m_dataViewMap;
  std::mutex m_mutex;
  const int64_t m_memoryLimit;
  int64_t m_usage;
  OpenVDS::Error m_error;

  void prefetchUntilMemoryLimit()
  {
    if (m_usage >= m_memoryLimit)
      return;

    size_t i;
    for (i = 0; i < m_requests.size() && m_usage < m_memoryLimit && m_error.code == 0; i++)
    {
      auto &req = m_requests[i];
      auto it = m_dataViewMap.find(req);
      if (it != m_dataViewMap.end())
        continue;
      auto dataView = std::make_shared<DataView>(m_dataProvider, req.offset, req.size, true, m_error);
      m_dataViewMap.insert(it, {req, dataView});
      m_usage += req.size;
    }
    m_requests.erase(m_requests.begin(), m_requests.begin() + i);
  }
};

#endif //DATA_PROVIDER_H
