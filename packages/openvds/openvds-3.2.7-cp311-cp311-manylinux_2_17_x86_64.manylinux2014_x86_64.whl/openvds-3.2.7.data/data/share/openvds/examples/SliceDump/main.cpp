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

#define _CRT_SECURE_NO_WARNINGS 1

#include <cxxopts.hpp>

#include <stdio.h>

#include <OpenVDS/VolumeDataLayout.h>
#include <OpenVDS/OpenVDS.h>
#include <OpenVDS/VolumeDataAccess.h>
#include <OpenVDS/ValueConversion.h>

#include <array>
#include <limits>

#include "GenerateVDS.h"

static bool ends_with(std::string const &value, std::string const &ending)
{
    if (ending.size() > value.size()) return false;
    return std::equal(ending.rbegin(), ending.rend(), value.rbegin());
}

static bool in_axis_mapping_range(char a, int32_t (&axis)[3], int index)
{
  if (a < '0' && a > '2')
    return false;
  int value = a - '0';
  for (int i = 0; i < index; i++)
  {
    if (axis[i] == value)
      return false;
  }
  axis[index] = value;
  return true;
}

static bool parse_axis_mapping(const std::string arg, int32_t (&axis)[3])
{
  memset(axis, std::numeric_limits<int>::max(), sizeof(axis));
  if (arg.size() < 5)
    return false;
  int i = 0;
  if (!in_axis_mapping_range(arg[0], axis, i++))
    return false;
  if (!in_axis_mapping_range(arg[2], axis, i++))
    return false;
  if (!in_axis_mapping_range(arg[4], axis, i++))
    return false;
  return true;
}

int main(int argc, char **argv)
{
  cxxopts::Options options("slicedump", "slicedump - A tool to dump a slice to file");
  options.positional_help("<output file>");

  std::string file_name;
  std::string url;
  std::string connectionString;
  std::string axis = "0,1,2";
  int axis_position = std::numeric_limits<int>::min();
  int32_t output_width = 500;
  int32_t output_height = 500;
  bool generate_noise = false;

  options.add_option("", "", "url", "Url for the VDS", cxxopts::value<std::string>(url), "<string>");
  options.add_option("", "", "connection-string", "Azure Blob Storage connection string.", cxxopts::value<std::string>(connectionString), "<string>");
  options.add_option("", "", "axis",     "Axis mapping. Comma seperated list. First digite is the axis for the slice. "
                                         "Second is the x axis and third is the y axis", cxxopts::value(axis), "<axis id>");
  options.add_option("", "", "noise",    "Generate a noise VDS in memory, and grab a slice from this (default off).", cxxopts::value(generate_noise), "<enable>");
  options.add_option("", "", "position", "Position on axis for slice", cxxopts::value(axis_position), "<position in axis>");
  options.add_option("", "", "o_width",  "Output image width (default 200)", cxxopts::value(output_width), "<output width>");
  options.add_option("", "", "o_height", "Output image height (default 200)", cxxopts::value(output_height), "<output height>");
  options.add_option("", "", "output", "", cxxopts::value(file_name), "");
  options.parse_positional("output");

  try
  {
    options.parse(argc, argv);
  }
  catch(cxxopts::OptionParseException &e)
  {
    fprintf(stderr, "%s\n", e.what());
    return EXIT_FAILURE;
  }

  OpenVDS::Error error;
  OpenVDS::ScopedVDSHandle handle;

  if (generate_noise)
  {
    handle = generateSimpleInMemory3DVDS(60,60,60, OpenVDS::VolumeDataChannelDescriptor::Format_U8);
    if (handle)
      fill3DVDSWithNoise(handle);
  }
  else if(url.empty())
  {
    fprintf(stderr, "Either specify noise generation or provide a url.\n");
    return EXIT_FAILURE;
  }
  else
  {
    handle = OpenVDS::Open(url, connectionString, error);
  }
  
  if (file_name.empty())
  {
    fprintf(stderr, "No output filename specified");
    return EXIT_FAILURE;
  }

  int32_t axis_mapper[3];
  if (!parse_axis_mapping(axis, axis_mapper))
  {
    fprintf(stderr, "Invalid axis mapping format: %s\n", axis.c_str());
    fprintf(stderr, "Expected to comma seperated list ie. 1,2,0");
    return EXIT_FAILURE;
  }
  fprintf(stdout, "Using axis mapping [%d, %d, %d]\n", axis_mapper[0], axis_mapper[1], axis_mapper[2]);


  if (!handle)
  {
    fprintf(stderr, "Failed to open VDS: %s\n", error.string.c_str());
    return error.code;
  }

  if (!ends_with(file_name, ".bmp"))
    file_name = file_name + ".bmp";

  std::unique_ptr<FILE, decltype(&fclose)> file(fopen(file_name.c_str(), "wb"), &fclose);
  if (!file)
  {
    fprintf(stderr, "Failed to open file: %s\n", file_name.c_str());
    return -4;
  }

  OpenVDS::VolumeDataLayout *layout = OpenVDS::GetLayout(handle);
  OpenVDS::VolumeDataAccessManager accessManager = OpenVDS::GetAccessManager(handle);

  int sampleCount[3];
  sampleCount[0] = layout->GetDimensionNumSamples(axis_mapper[0]);
  sampleCount[1] = layout->GetDimensionNumSamples(axis_mapper[1]);
  sampleCount[2] = layout->GetDimensionNumSamples(axis_mapper[2]);

  fprintf(stdout, "Found data set with sample count [%d, %d, %d]\n", sampleCount[0], sampleCount[1], sampleCount[2]);

  float x_sample_shift = float(sampleCount[1]) / output_width;
  float y_sample_shift = float(sampleCount[2]) / output_height;

  std::vector<std::array<float, OpenVDS::Dimensionality_Max>> samples;
  samples.resize(size_t(output_width) * size_t(output_height));

  axis_position = std::max(0, axis_position);
  axis_position = std::min(sampleCount[0], axis_position);

  for (int y = 0; y < output_height; y++)
  {
    float y_pos = y * y_sample_shift + 0.5f;
    for (int x = 0; x < output_width; x++)
    {
      float x_pos = x * x_sample_shift + 0.5f;
      auto &pos = samples[size_t(y) * size_t(output_width) + size_t(x)];
      pos[size_t(axis_mapper[0])] = axis_position + 0.5f;
      pos[size_t(axis_mapper[1])] = x_pos;
      pos[size_t(axis_mapper[2])] = y_pos;
    }
  }

  auto request = accessManager.RequestVolumeSamples(OpenVDS::Dimensions_012, 0, 0, reinterpret_cast<const float (*)[OpenVDS::Dimensionality_Max]>(samples.data()), (int)samples.size(), OpenVDS::InterpolationMethod::Linear);
  bool finished = request->WaitForCompletion();
  if (!finished)
  {
    request->IsCanceled(); //get the error
    int code = request->GetErrorCode();
    std::string errorstr = request->GetErrorMessage();
    fprintf(stderr, "Failed to download request: %d - %s\n", code, errorstr.c_str());
    return -2;
  }

  float minValue = layout->GetChannelValueRangeMin(0);
  float maxValue = layout->GetChannelValueRangeMax(0);
  float intScale = layout->GetChannelIntegerScale(0);
  float intLayout = layout->GetChannelIntegerOffset(0);
  OpenVDS::QuantizingValueConverterWithNoValue<uint8_t, float, false> converter(minValue, maxValue, intScale, intLayout, 0.f, 0.f);

  std::vector<float> data = std::move(request->Data());
  std::vector<std::array<uint8_t, 3>> fileData;
  fileData.resize(size_t(output_width) * size_t(output_height));
  for (int y = 0; y < output_height; y++)
  {
    for (int x = 0; x < output_width; x++)
    {

      uint8_t value =  converter.ConvertValue(data[size_t(y * output_width + x)]);
      auto &color = fileData[size_t(y * output_width + x)];
      color[0] =  value;
      color[1] =  value;
      color[2] =  value;
    }
  }

  uint32_t filesize = 54 + (sizeof(*fileData.data()) * uint32_t(fileData.size()));
  uint8_t bmpfileheader[14] = {'B','M', 0,0,0,0, 0,0, 0,0, 54,0,0,0};
  uint8_t bmpinfoheader[40] = {40,0,0,0, 0,0,0,0, 0,0,0,0, 1,0, 24,0};
  uint8_t bmppad[3] = {0,0,0};

  bmpfileheader[ 2] = (uint8_t)(filesize    );
  bmpfileheader[ 3] = (uint8_t)(filesize>> 8);
  bmpfileheader[ 4] = (uint8_t)(filesize>>16);
  bmpfileheader[ 5] = (uint8_t)(filesize>>24);

  bmpinfoheader[ 4] = (uint8_t)(output_width    );
  bmpinfoheader[ 5] = (uint8_t)(output_width>> 8);
  bmpinfoheader[ 6] = (uint8_t)(output_width>>16);
  bmpinfoheader[ 7] = (uint8_t)(output_width>>24);
  bmpinfoheader[ 8] = (uint8_t)(output_height    );
  bmpinfoheader[ 9] = (uint8_t)(output_height>> 8);
  bmpinfoheader[10] = (uint8_t)(output_height>>16);
  bmpinfoheader[11] = (uint8_t)(output_height>>24);
  fwrite(bmpfileheader,1,14,file.get());
  fwrite(bmpinfoheader,1,40,file.get());

  for (int32_t i = 0; i < output_height; i++)
  {
    fwrite(reinterpret_cast<const uint8_t *>(fileData.data()) +(output_width*(output_height-i-1)*3),3,size_t(output_width),file.get());
    fwrite(bmppad,1,(-3 * output_width) & 3, file.get());
  }
  file.reset();
  fprintf(stdout, "File written to: %s\n", file_name.c_str());
  return 0;
}
