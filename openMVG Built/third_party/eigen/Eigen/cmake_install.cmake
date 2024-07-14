# Install script for directory: C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/Eigen

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/eigen3/Eigen" TYPE FILE FILES
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/Eigen/Cholesky"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/Eigen/CholmodSupport"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/Eigen/Core"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/Eigen/Dense"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/Eigen/Eigen"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/Eigen/Eigenvalues"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/Eigen/Geometry"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/Eigen/Householder"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/Eigen/IterativeLinearSolvers"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/Eigen/Jacobi"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/Eigen/KLUSupport"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/Eigen/LU"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/Eigen/MetisSupport"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/Eigen/OrderingMethods"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/Eigen/PaStiXSupport"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/Eigen/PardisoSupport"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/Eigen/QR"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/Eigen/QtAlignedMalloc"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/Eigen/SPQRSupport"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/Eigen/SVD"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/Eigen/Sparse"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/Eigen/SparseCholesky"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/Eigen/SparseCore"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/Eigen/SparseLU"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/Eigen/SparseQR"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/Eigen/StdDeque"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/Eigen/StdList"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/Eigen/StdVector"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/Eigen/SuperLUSupport"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/Eigen/UmfPackSupport"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Devel" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/eigen3/Eigen" TYPE DIRECTORY FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/third_party/eigen/Eigen/src" FILES_MATCHING REGEX "/[^/]*\\.h$")
endif()

