# Install script for directory: C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/array

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/arrow/array" TYPE FILE FILES
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/array/array_base.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/array/array_binary.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/array/array_decimal.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/array/array_dict.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/array/array_nested.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/array/array_primitive.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/array/builder_adaptive.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/array/builder_base.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/array/builder_binary.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/array/builder_decimal.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/array/builder_dict.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/array/builder_nested.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/array/builder_primitive.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/array/builder_time.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/array/builder_union.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/array/concatenate.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/array/data.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/array/diff.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/array/util.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/array/validate.h"
    )
endif()

