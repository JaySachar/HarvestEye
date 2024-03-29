# This file is part of OpenMVG, an Open Multiple View Geometry C++ library.

# Copyright (c) 2015 Pierre MOULON.

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#

# Config file for OpenMVG library - Find OpenMVG & dependencies.
#
# This file is used by CMake when FIND_PACKAGE( OpenMVG ) is invoked (and
# the directory containing this file is present in CMAKE_MODULE_PATH).
#
# This module defines the following variables:
#
# OPENMVG_FOUND: True if OpenMVG has been successfully found.
#
# OPENMVG_VERSION: Version of OpenMVG found.
#

# Called if we failed to find OpenMVG or any of it's required dependencies,
# unsets all public (designed to be used externally) variables and reports
# error message at priority depending upon [REQUIRED/QUIET/<NONE>] argument.
macro(OPENMVG_REPORT_NOT_FOUND REASON_MSG)
  # FindPackage() only references OpenMVG_FOUND, and requires it to be
  # explicitly set FALSE to denote not found (not merely undefined).
  set(OPENMVG_FOUND FALSE)

  # Reset the CMake module path to its state when this script was called.
  set(CMAKE_MODULE_PATH ${CALLERS_CMAKE_MODULE_PATH})

  # Note <package>_FIND_[REQUIRED/QUIETLY] variables defined by
  # FindPackage() use the camelcase library name, not uppercase.
  if (OPENMVG_FIND_QUIETLY)
    message(STATUS "Failed to find OPENMVG - " ${REASON_MSG} ${ARGN})
  elseif (OPENMVG_FIND_REQUIRED)
    message(FATAL_ERROR "Failed to find OPENMVG - " ${REASON_MSG} ${ARGN})
  else()
    # Neither QUIETLY nor REQUIRED, use SEND_ERROR which emits an error
    # that prevents generation, but continues configuration.
    message(SEND_ERROR "Failed to find OPENMVG - " ${REASON_MSG} ${ARGN})
  endif ()
  return()
endmacro(OPENMVG_REPORT_NOT_FOUND)

# set the version.
set(OPENMVG_VERSION 2.1.0)

# Get the (current, i.e. installed) directory containing this file.
get_filename_component(CURRENT_CONFIG_INSTALL_DIR
  "${CMAKE_CURRENT_LIST_FILE}" PATH)

# Record the state of the CMake module path when this script was
# called so that we can ensure that we leave it in the same state on
# exit as it was on entry, but modify it locally.
set(CALLERS_CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH})
# Reset CMake module path to the installation directory of this
# script.
set(CMAKE_MODULE_PATH ${CURRENT_CONFIG_INSTALL_DIR})

# Build the absolute root install directory as a relative path
get_filename_component(CURRENT_ROOT_INSTALL_DIR
  ${CMAKE_MODULE_PATH}/../../../ ABSOLUTE)
if (NOT EXISTS ${CURRENT_ROOT_INSTALL_DIR})
  OPENMVG_REPORT_NOT_FOUND(
    "OpenMVG install root: ${CURRENT_ROOT_INSTALL_DIR}, "
    "determined from relative path from OpenMVGConfig.cmake install location: "
    "${CMAKE_MODULE_PATH}, does not exist.")
endif (NOT EXISTS ${CURRENT_ROOT_INSTALL_DIR})

# Check if OpenMVG header is installed
if (NOT EXISTS ${CURRENT_ROOT_INSTALL_DIR}/include/openMVG/version.hpp)
  OPENMVG_REPORT_NOT_FOUND(
    "OpenMVG install root: ${CMAKE_MODULE_PATH}. "
    "Cannot find openMVG include files.")
endif (NOT EXISTS ${CURRENT_ROOT_INSTALL_DIR}/include/openMVG/version.hpp)

##### the libraries themselves come in via OpenMVGTargets-<release/debug>.cmake
# as link libraries rules as target.

set(THREADS_PREFER_PTHREAD_FLAG ON)
find_package(Threads REQUIRED)

# Record state of build time dependencies
set(OpenMVG_USE_INTERNAL_CEREAL "ON")
set(OpenMVG_USE_OPENMP "ON")

# Find transitive dependencies if required
include(CMakeFindDependencyMacro)
if (OpenMVG_USE_OPENMP)
  find_dependency(OpenMP REQUIRED)
endif()
if (NOT OpenMVG_USE_INTERNAL_CEREAL)
  find_dependency(cereal REQUIRED)
endif()

# Import exported OpenMVG targets
include(${CURRENT_CONFIG_INSTALL_DIR}/OpenMVGTargets.cmake)

# As we use OPENMVG_REPORT_NOT_FOUND() to abort, if we reach this point we have
# found OpenMVG and all required dependencies.
message(STATUS "----")
message(STATUS "OpenMVG Find_Package")
message(STATUS "----")
message(STATUS "Found OpenMVG version: ${OPENMVG_VERSION}")
message(STATUS "Installed in: ${CURRENT_ROOT_INSTALL_DIR}")
message(STATUS "----")

set(OPENMVG_FOUND TRUE)

# Reset the CMake module path to its state when this script was called.
set(CMAKE_MODULE_PATH ${CALLERS_CMAKE_MODULE_PATH})
