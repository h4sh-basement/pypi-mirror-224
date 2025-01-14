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

namespace tv {

namespace math {

template <typename T, size_t N> struct UnaryOp;

template <typename T, size_t N> struct UnaryIdentity {
  using argument_t = tv::array<T, N>;
  using result_t = tv::array<T, N>;

  TV_HOST_DEVICE_INLINE constexpr result_t operator()(const argument_t &src) {
    return src;
  }
};

} // namespace math
} // namespace tv
