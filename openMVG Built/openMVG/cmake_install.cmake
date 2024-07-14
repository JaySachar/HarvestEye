# Install script for directory: C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/openMVG

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "C:/Program Files (x86)/openMVG")
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

if(CMAKE_INSTALL_COMPONENT STREQUAL "headers" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/openMVG" TYPE DIRECTORY FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/openMVG/." FILES_MATCHING REGEX "/[^/]*\\.hpp$" REGEX "/[^/]*\\.h$")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/openMVG/cameras/cmake_install.cmake")
  include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/openMVG/clustering/cmake_install.cmake")
  include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/openMVG/exif/cmake_install.cmake")
  include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/openMVG/features/cmake_install.cmake")
  include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/openMVG/graph/cmake_install.cmake")
  include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/openMVG/graphics/cmake_install.cmake")
  include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/openMVG/image/cmake_install.cmake")
  include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/openMVG/linearProgramming/cmake_install.cmake")
  include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/openMVG/geodesy/cmake_install.cmake")
  include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/openMVG/geometry/cmake_install.cmake")
  include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/openMVG/matching/cmake_install.cmake")
  include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/openMVG/matching_image_collection/cmake_install.cmake")
  include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/openMVG/multiview/cmake_install.cmake")
  include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/openMVG/numeric/cmake_install.cmake")
  include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/openMVG/robust_estimation/cmake_install.cmake")
  include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/openMVG/tracks/cmake_install.cmake")
  include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/openMVG/color_harmonization/cmake_install.cmake")
  include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/openMVG/spherical/cmake_install.cmake")
  include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/openMVG/system/cmake_install.cmake")
  include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/openMVG/sfm/cmake_install.cmake")
  include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/openMVG/stl/cmake_install.cmake")
  include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/openMVG/vector_graphics/cmake_install.cmake")

endif()

