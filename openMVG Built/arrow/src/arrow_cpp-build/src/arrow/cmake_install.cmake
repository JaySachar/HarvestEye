# Install script for directory: C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/release/arrow_bundled_dependencies.lib")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Dd][Ee][Bb][Uu][Gg])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/release/Debug/arrow_static.lib")
  elseif(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/release/Release/arrow_static.lib")
  elseif(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Mm][Ii][Nn][Ss][Ii][Zz][Ee][Rr][Ee][Ll])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/release/MinSizeRel/arrow_static.lib")
  elseif(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Rr][Ee][Ll][Ww][Ii][Tt][Hh][Dd][Ee][Bb][Ii][Nn][Ff][Oo])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/release/RelWithDebInfo/arrow_static.lib")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/Arrow" TYPE FILE FILES
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/src/arrow/ArrowConfig.cmake"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/src/arrow/ArrowConfigVersion.cmake"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/Arrow/ArrowTargets.cmake")
    file(DIFFERENT _cmake_export_file_changed FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/Arrow/ArrowTargets.cmake"
         "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/src/arrow/CMakeFiles/Export/817832ed7b630b992c3753a0fa15add4/ArrowTargets.cmake")
    if(_cmake_export_file_changed)
      file(GLOB _cmake_old_config_files "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/Arrow/ArrowTargets-*.cmake")
      if(_cmake_old_config_files)
        string(REPLACE ";" ", " _cmake_old_config_files_text "${_cmake_old_config_files}")
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/Arrow/ArrowTargets.cmake\" will be replaced.  Removing files [${_cmake_old_config_files_text}].")
        unset(_cmake_old_config_files_text)
        file(REMOVE ${_cmake_old_config_files})
      endif()
      unset(_cmake_old_config_files)
    endif()
    unset(_cmake_export_file_changed)
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/Arrow" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/src/arrow/CMakeFiles/Export/817832ed7b630b992c3753a0fa15add4/ArrowTargets.cmake")
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Dd][Ee][Bb][Uu][Gg])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/Arrow" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/src/arrow/CMakeFiles/Export/817832ed7b630b992c3753a0fa15add4/ArrowTargets-debug.cmake")
  endif()
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Mm][Ii][Nn][Ss][Ii][Zz][Ee][Rr][Ee][Ll])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/Arrow" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/src/arrow/CMakeFiles/Export/817832ed7b630b992c3753a0fa15add4/ArrowTargets-minsizerel.cmake")
  endif()
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Rr][Ee][Ll][Ww][Ii][Tt][Hh][Dd][Ee][Bb][Ii][Nn][Ff][Oo])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/Arrow" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/src/arrow/CMakeFiles/Export/817832ed7b630b992c3753a0fa15add4/ArrowTargets-relwithdebinfo.cmake")
  endif()
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/Arrow" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/src/arrow/CMakeFiles/Export/817832ed7b630b992c3753a0fa15add4/ArrowTargets-release.cmake")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/src/arrow/arrow.pc")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/arrow" TYPE FILE FILES
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/api.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/array.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/buffer.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/buffer_builder.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/builder.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/chunk_resolver.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/chunked_array.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/compare.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/config.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/datum.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/device.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/extension_type.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/memory_pool.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/memory_pool_test.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/pch.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/pretty_print.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/record_batch.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/result.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/scalar.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/sparse_tensor.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/status.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/stl.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/stl_allocator.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/stl_iterator.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/table.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/table_builder.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/tensor.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/type.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/type_fwd.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/type_traits.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/visit_array_inline.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/visit_data_inline.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/visit_scalar_inline.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/visit_type_inline.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/visitor.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/visitor_generate.h"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/Arrow" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/src/arrow/ArrowOptions.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/Arrow" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/arrow-config.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/src/arrow/testing/cmake_install.cmake")
  include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/src/arrow/array/cmake_install.cmake")
  include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/src/arrow/c/cmake_install.cmake")
  include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/src/arrow/io/cmake_install.cmake")
  include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/src/arrow/tensor/cmake_install.cmake")
  include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/src/arrow/util/cmake_install.cmake")
  include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/src/arrow/vendored/cmake_install.cmake")

endif()

