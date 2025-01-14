/****************************************************************************
** Copyright 2019 The Open Group
** Copyright 2019 Bluware, Inc.
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

#ifndef SEGY_FILE_INFO_H
#define SEGY_FILE_INFO_H

#include "SEGY.h"
#include "DataProvider.h"

#include <cstdint>
#include <vector>
#include <functional>

namespace OpenVDS { class File; typedef struct VDSError Error; }

struct SEGYBinInfo
{
  int    m_inlineNumber;
  int    m_crosslineNumber;
  double m_ensembleXCoordinate;
  double m_ensembleYCoordinate;

  SEGYBinInfo() : m_inlineNumber(), m_crosslineNumber(), m_ensembleXCoordinate(), m_ensembleYCoordinate() {}
  SEGYBinInfo(int inlineNumber, int crosslineNumber, double positionX, double positionY) : m_inlineNumber(inlineNumber), m_crosslineNumber(crosslineNumber), m_ensembleXCoordinate(positionX), m_ensembleYCoordinate(positionY) {}
};

struct SEGYSegmentInfo
{
  int     m_primaryKey;

  int64_t m_traceStart,
          m_traceStop;

  SEGYBinInfo
          m_binInfoStart,
          m_binInfoStop;

  SEGYSegmentInfo() : m_primaryKey(), m_traceStart(), m_traceStop(), m_binInfoStart(), m_binInfoStop() {}
  SEGYSegmentInfo(int primaryKey, int64_t trace, SEGYBinInfo const &binInfo) : m_primaryKey(primaryKey), m_traceStart(trace), m_traceStop(trace), m_binInfoStart(binInfo), m_binInfoStop(binInfo) {}
  SEGYSegmentInfo(int primaryKey, int64_t traceStart, int64_t traceStop, SEGYBinInfo const &binInfoStart, SEGYBinInfo const &binInfoStop) : m_primaryKey(primaryKey), m_traceStart(traceStart), m_traceStop(traceStop), m_binInfoStart(binInfoStart), m_binInfoStop(binInfoStop) {}
};

struct SEGYBinInfoHeaderFields
{
  SEGY::HeaderField m_inlineNumberHeaderField;
  SEGY::HeaderField m_crosslineNumberHeaderField;
  SEGY::HeaderField m_coordinateScaleHeaderField;
  SEGY::HeaderField m_ensembleXCoordinateHeaderField;
  SEGY::HeaderField m_ensembleYCoordinateHeaderField;
  double      m_scaleOverride;

  SEGYBinInfoHeaderFields() : m_inlineNumberHeaderField(), m_crosslineNumberHeaderField(), m_coordinateScaleHeaderField(), m_ensembleXCoordinateHeaderField(), m_ensembleYCoordinateHeaderField(), m_scaleOverride() {}
  SEGYBinInfoHeaderFields(SEGY::HeaderField inlineNumberHeaderField, SEGY::HeaderField crosslineNumberHeaderField, SEGY::HeaderField coordinateScaleHeaderField, SEGY::HeaderField ensembleXCoordinateHeaderField, SEGY::HeaderField ensembleYCoordinateHeaderField, double scaleOverride = 0.0) : m_inlineNumberHeaderField(inlineNumberHeaderField), m_crosslineNumberHeaderField(crosslineNumberHeaderField), m_coordinateScaleHeaderField(coordinateScaleHeaderField), m_ensembleXCoordinateHeaderField(ensembleXCoordinateHeaderField), m_ensembleYCoordinateHeaderField(ensembleYCoordinateHeaderField), m_scaleOverride(scaleOverride) {}

  static SEGYBinInfoHeaderFields StandardHeaderFields() { return SEGYBinInfoHeaderFields(SEGY::TraceHeader::InlineNumberHeaderField, SEGY::TraceHeader::CrosslineNumberHeaderField, SEGY::TraceHeader::CoordinateScaleHeaderField, SEGY::TraceHeader::EnsembleXCoordinateHeaderField, SEGY::TraceHeader::EnsembleYCoordinateHeaderField); }
};

struct SEGYFileInfo
{
  uint64_t      m_persistentID;

  SEGY::Endianness
                m_headerEndianness;

  SEGY::BinaryHeader::DataSampleFormatCode
                m_dataSampleFormatCode;

  int           m_sampleCount;

  double        m_startTimeMilliseconds;

  double        m_sampleIntervalMilliseconds;

  int           m_detectedScale;

  // per-file trace counts
  std::vector<int64_t>
                m_traceCounts;

  // a vector of per-file vectors
  std::vector<std::vector<SEGYSegmentInfo>>
                m_segmentInfoLists;

  // vector of per-file offset-vector maps for SEGYType::PrestackOffsetSorted
  std::vector<std::map<int, std::vector<SEGYSegmentInfo>>>
                m_segmentInfoListsByOffset;


  SEGY::HeaderField
                m_primaryKey,
                m_secondaryKey;

  SEGY::SEGYType
                m_segyType;

  OPENVDS_EXPORT static uint64_t StaticGetUniqueID();

  SEGYFileInfo() : m_persistentID(), m_headerEndianness(), m_dataSampleFormatCode(), m_sampleCount(), m_startTimeMilliseconds(), m_sampleIntervalMilliseconds(), m_primaryKey(), m_secondaryKey(), m_segyType(SEGY::SEGYType::Poststack) {}
  SEGYFileInfo(uint64_t persistentID, SEGY::Endianness headerEndianness = SEGY::Endianness::BigEndian) : m_persistentID(persistentID), m_headerEndianness(headerEndianness), m_dataSampleFormatCode(SEGY::BinaryHeader::DataSampleFormatCode::Unknown), m_sampleCount(), m_startTimeMilliseconds(), m_sampleIntervalMilliseconds(), m_primaryKey(), m_secondaryKey(), m_segyType(SEGY::SEGYType::Poststack) {}
  SEGYFileInfo(SEGY::Endianness headerEndianness) : m_persistentID(StaticGetUniqueID()), m_headerEndianness(headerEndianness), m_dataSampleFormatCode(SEGY::BinaryHeader::DataSampleFormatCode::Unknown), m_sampleCount(), m_startTimeMilliseconds(), m_sampleIntervalMilliseconds(), m_primaryKey(), m_secondaryKey(), m_segyType(SEGY::SEGYType::Poststack) {}

  OPENVDS_EXPORT int  TraceByteSize() const;

  OPENVDS_EXPORT bool Scan(const std::vector<DataProvider>& dataProviders, OpenVDS::Error &error, SEGY::HeaderField const &primaryKeyHeaderField, SEGY::HeaderField const &secondaryKeyHeaderField = SEGY::HeaderField(), SEGY::HeaderField const &startTimeHeaderField = SEGY::TraceHeader::StartTimeHeaderField, SEGY::HeaderField const& offsetHeaderField = SEGY::TraceHeader::OffsetHeaderField, SEGYBinInfoHeaderFields const &binInfoHeaderFields = SEGYBinInfoHeaderFields::StandardHeaderFields());

  OPENVDS_EXPORT SEGYBinInfo readBinInfoFromHeader(const char* header, SEGYBinInfoHeaderFields const& headerFields, SEGY::Endianness endianness, int segmentTraceIndex) const;

  OPENVDS_EXPORT bool Is4D() const;

  OPENVDS_EXPORT bool IsUnbinned() const;

  OPENVDS_EXPORT bool HasGatherOffset() const;

  OPENVDS_EXPORT bool Is2D() const;

  OPENVDS_EXPORT bool IsOffsetSorted() const;

  OPENVDS_EXPORT static double convertScaleToScaleFactor(int scale);
};

#endif  // SEGY_FILE_INFO_H
