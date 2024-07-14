# Install script for directory: C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/arrow/util" TYPE FILE FILES
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/algorithm.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/align_util.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/aligned_storage.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/async_generator.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/async_generator_fwd.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/async_util.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/base64.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/basic_decimal.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/benchmark_util.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/bit_block_counter.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/bit_run_reader.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/bit_stream_utils.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/bit_util.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/bitmap.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/bitmap_builders.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/bitmap_generate.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/bitmap_ops.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/bitmap_reader.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/bitmap_visit.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/bitmap_writer.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/bitset_stack.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/bpacking.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/bpacking64_default.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/bpacking_avx2.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/bpacking_avx512.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/bpacking_default.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/bpacking_neon.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/bpacking_simd128_generated.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/bpacking_simd256_generated.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/bpacking_simd512_generated.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/byte_size.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/byte_stream_split.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/bytes_view.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/cancel.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/checked_cast.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/compare.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/compression.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/concurrent_map.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/converter.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/counting_semaphore.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/cpu_info.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/debug.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/decimal.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/delimiting.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/dispatch.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/double_conversion.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/endian.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/formatting.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/functional.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/future.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/hash_util.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/hashing.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/int_util.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/int_util_overflow.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/io_util.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/iterator.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/key_value_metadata.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/launder.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/logging.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/macros.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/map.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/math_constants.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/memory.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/mutex.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/parallel.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/pcg_random.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/print.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/queue.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/range.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/rle_encoding.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/simd.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/small_vector.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/sort.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/spaced.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/stopwatch.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/string.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/string_builder.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/task_group.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/tdigest.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/test_common.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/thread_pool.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/time.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/tracing.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/trie.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/type_fwd.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/type_traits.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/ubsan.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/unreachable.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/uri.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/utf8.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/value_parsing.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/vector.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/visibility.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/windows_compatibility.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/util/windows_fixup.h"
    )
endif()

