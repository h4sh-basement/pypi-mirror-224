// Copyright 2021 Yan Yan
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#pragma once

#include <tensorview/core/all.h>
#ifdef __CUDACC_RTC__
#include <tensorview/core/nvrtc_std.h>
#else
#include <type_traits>
#include <limits>
#endif

namespace tv {
namespace hash {

namespace detail {

template <int N, bool Signed> struct SizeToInt;

template <bool Signed> struct SizeToInt<1, Signed> {
  using type = std::conditional_t<Signed, int8_t, uint8_t>;
};

template <bool Signed> struct SizeToInt<2, Signed> {
  using type = std::conditional_t<Signed, int16_t, uint16_t>;
};

template <bool Signed> struct SizeToInt<4, Signed> {
  using type = std::conditional_t<Signed, int32_t, uint32_t>;
};

template <bool Signed> struct SizeToInt<8, Signed> {
  using type = std::conditional_t<Signed, int64_t, unsigned long long>;
};

template <typename T> struct MapTypeToInt {
  using type = typename SizeToInt<sizeof(T), true>::type;
};

template <typename T> struct MapTypeToUnsignedInt {
  using type = typename SizeToInt<sizeof(T), false>::type;
};

template <typename K>
struct default_empty_key;

template <>
struct default_empty_key<int32_t>{
  static constexpr int32_t value = std::numeric_limits<int32_t>::max();
};

template <>
struct default_empty_key<int64_t>{
  static constexpr int64_t value = std::numeric_limits<int64_t>::max();
};
template <>
struct default_empty_key<uint32_t>{
  static constexpr uint32_t value = std::numeric_limits<uint32_t>::max();
};

template <>
struct default_empty_key<uint64_t>{
  static constexpr uint64_t value = std::numeric_limits<uint64_t>::max();
};

struct __place_holder_t;

template <>
struct default_empty_key<
    std::conditional<std::is_same<uint64_t, unsigned long long>::value,
                     __place_holder_t, unsigned long long>::type> {
  static constexpr unsigned long long value = std::numeric_limits<unsigned long long>::max();
};

} // namespace detail

template <int K>
using itemsize_to_unsigned_t = typename detail::SizeToInt<K, false>::type;

template <typename K>
using to_unsigned_t = typename detail::MapTypeToUnsignedInt<K>::type;

template <typename K>
constexpr K default_empty_key_v = detail::default_empty_key<K>::value;

template <typename K, typename V, K EmptyKey = default_empty_key_v<K>>
struct pair {
  K first;
  V second;
  using key_type_uint = to_unsigned_t<K>;
  TV_HOST_DEVICE_INLINE bool empty() { return first == EmptyKey; }
};

template <typename T> TV_HOST_DEVICE size_t align_to_power2(T size) {
  size_t r = 0;
  size_t num_1_bit = size & 1 ? 1 : 0;
  while (size >>= 1) {
    r++;
    if (size & 1) {
      ++num_1_bit;
    }
  }
  if (num_1_bit == 1) {
    return 1 << r;
  } else {
    return 1 << (r + 1);
  }
}

} // namespace hash

} // namespace tv
