# Install script for directory: C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/testing

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/arrow/testing" TYPE FILE FILES
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/testing/async_test_util.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/testing/builder.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/testing/executor_util.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/testing/extension_type.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/testing/future_util.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/testing/generator.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/testing/gtest_compat.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/testing/gtest_util.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/testing/json_integration.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/testing/matchers.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/testing/pch.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/testing/random.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/testing/uniform_real.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/testing/util.h"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp/cpp/src/arrow/testing/visibility.h"
    )
endif()

