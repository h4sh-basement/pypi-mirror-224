/***************************************************************************************************
 * Copyright (c) 2020, NVIDIA CORPORATION.  All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 *modification, are permitted provided that the following conditions are met:
 *     * Redistributions of source code must retain the above copyright notice,
 *this list of conditions and the following disclaimer.
 *     * Redistributions in binary form must reproduce the above copyright
 *notice, this list of conditions and the following disclaimer in the
 *documentation and/or other materials provided with the distribution.
 *     * Neither the name of the NVIDIA CORPORATION nor the names of its
 *contributors may be used to endorse or promote products derived from this
 *software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 *AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 *IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 *DISCLAIMED. IN NO EVENT SHALL NVIDIA CORPORATION BE LIABLE FOR ANY DIRECT,
 *INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 * BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 *DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
 *OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TOR (INCLUDING
 *NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
 *EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *
 **************************************************************************************************/

/*! \file
    \brief Basic copy routines for tensor views
*/
#pragma once
#include <tensorview/core/all.h>

namespace tv {
namespace gemm {
namespace transform {

/// Transforms a fragment by doing a transpose
template <int ElementCount, typename TransposeShape, typename Element>
struct Transpose {
  // we need a empty function before c++17.
  TV_DEVICE_INLINE
  void transform(Element *dst, const Element *src) {}
};

/// Specialization for int8_t 4x4 transpose
template <int ElementCount>
struct Transpose<ElementCount, tv::mp_list_int<4, 4>, int8_t> {

  static const int kElementCount = ElementCount;
  static constexpr tv::array<int, 2> kTransposeShape{4, 4};
  using Element = int8_t;

  static_assert(
      !(kElementCount % (kTransposeShape[0] * kTransposeShape[1])),
      "Shape needs to be multiple of 16 elements to do a 4x4 transpose");

  TV_DEVICE_INLINE
  void transform(Element *dst, const Element *src) {
    const int *src_int = reinterpret_cast<const int *>(src);
    int *dst_int = reinterpret_cast<int *>(dst);

    TV_PRAGMA_UNROLL
    for (int i = 0;
         i < kElementCount / (kTransposeShape[0] * kTransposeShape[1]); i++) {

      int const i0 = 4 * i + 0;
      int const i1 = 4 * i + 1;
      int const i2 = 4 * i + 2;
      int const i3 = 4 * i + 3;

      int a0 = src_int[i0];
      int a1 = src_int[i1];
      int a2 = src_int[i2];
      int a3 = src_int[i3];
      // looks like they are just 12 swap operations.
      int b0, b1, b2, b3, c0;
      asm volatile("prmt.b32 %0, %1, %2, 0x0040;"
                   : "=r"(b0)
                   : "r"(a0), "r"(a1));
      asm volatile("prmt.b32 %0, %1, %2, 0x0040;"
                   : "=r"(c0)
                   : "r"(a2), "r"(a3));
      asm volatile("prmt.b32 %0, %1, %2, 0x5410;"
                   : "=r"(b0)
                   : "r"(b0), "r"(c0));

      asm volatile("prmt.b32 %0, %1, %2, 0x0051;"
                   : "=r"(b1)
                   : "r"(a0), "r"(a1));
      asm volatile("prmt.b32 %0, %1, %2, 0x0051;"
                   : "=r"(c0)
                   : "r"(a2), "r"(a3));
      asm volatile("prmt.b32 %0, %1, %2, 0x5410;"
                   : "=r"(b1)
                   : "r"(b1), "r"(c0));

      asm volatile("prmt.b32 %0, %1, %2, 0x0062;"
                   : "=r"(b2)
                   : "r"(a0), "r"(a1));
      asm volatile("prmt.b32 %0, %1, %2, 0x0062;"
                   : "=r"(c0)
                   : "r"(a2), "r"(a3));
      asm volatile("prmt.b32 %0, %1, %2, 0x5410;"
                   : "=r"(b2)
                   : "r"(b2), "r"(c0));

      asm volatile("prmt.b32 %0, %1, %2, 0x0073;"
                   : "=r"(b3)
                   : "r"(a0), "r"(a1));
      asm volatile("prmt.b32 %0, %1, %2, 0x0073;"
                   : "=r"(c0)
                   : "r"(a2), "r"(a3));
      asm volatile("prmt.b32 %0, %1, %2, 0x5410;"
                   : "=r"(b3)
                   : "r"(b3), "r"(c0));

      dst_int[i0] = b0;
      dst_int[i1] = b1;
      dst_int[i2] = b2;
      dst_int[i3] = b3;
    }
  }
};
} // namespace transform

} // namespace gemm
} // namespace tv
