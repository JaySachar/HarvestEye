# Install script for directory: C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/unsupported/Eigen

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

if(CMAKE_INSTALL_COMPONENT STREQUAL "Devel" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/eigen3/unsupported/Eigen" TYPE FILE FILES
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/unsupported/Eigen/AdolcForward"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/unsupported/Eigen/AlignedVector3"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/unsupported/Eigen/ArpackSupport"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/unsupported/Eigen/AutoDiff"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/unsupported/Eigen/BVH"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/unsupported/Eigen/EulerAngles"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/unsupported/Eigen/FFT"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/unsupported/Eigen/IterativeSolvers"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/unsupported/Eigen/KroneckerProduct"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/unsupported/Eigen/LevenbergMarquardt"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/unsupported/Eigen/MatrixFunctions"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/unsupported/Eigen/MoreVectorization"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/unsupported/Eigen/MPRealSupport"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/unsupported/Eigen/NonLinearOptimization"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/unsupported/Eigen/NumericalDiff"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/unsupported/Eigen/OpenGLSupport"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/unsupported/Eigen/Polynomials"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/unsupported/Eigen/Skyline"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/unsupported/Eigen/SparseExtra"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/unsupported/Eigen/SpecialFunctions"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/unsupported/Eigen/Splines"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Devel" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/eigen3/unsupported/Eigen" TYPE DIRECTORY FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/unsupported/Eigen/src" FILES_MATCHING REGEX "/[^/]*\\.h$")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/third_party/eigen/unsupported/Eigen/CXX11/cmake_install.cmake")

endif()

