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

#ifndef OPENVDS_RANGE_H
#define OPENVDS_RANGE_H

namespace OpenVDS
{
template<typename T>
struct Range
{
  T Min;
  T Max;

  Range() = default;
  Range(T min, T max) : Min(min), Max(max) {}
};

template<typename T>
T rangeSize(const Range<T> &r)
{
  return r.Max - r.Min;
}

using IntRange    = Range<int>;
using FloatRange  = Range<float>;
using DoubleRange = Range<double>;

} // end namespace OpenVDS

#endif // OPENVDS_RANGE_H
