# Install script for directory: C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/openMVG/robust_estimation

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

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Dd][Ee][Bb][Uu][Gg])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/Windows-AMD64-/Debug/openMVG_robust_estimation.lib")
  elseif(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/Windows-AMD64-/Release/openMVG_robust_estimation.lib")
  elseif(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Mm][Ii][Nn][Ss][Ii][Zz][Ee][Rr][Ee][Ll])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/Windows-AMD64-/MinSizeRel/openMVG_robust_estimation.lib")
  elseif(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Rr][Ee][Ll][Ww][Ii][Tt][Hh][Dd][Ee][Bb][Ii][Nn][Ff][Oo])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/Windows-AMD64-/RelWithDebInfo/openMVG_robust_estimation.lib")
  elseif(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Mm][Aa][Ii][Nn][Tt][Aa][Ii][Nn][Ee][Rr])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/Windows-AMD64-/Maintainer/openMVG_robust_estimation.lib")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Dd][Ee][Bb][Uu][Gg])$")
    include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/openMVG/robust_estimation/CMakeFiles/openMVG_robust_estimation.dir/install-cxx-module-bmi-Debug.cmake" OPTIONAL)
  elseif(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
    include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/openMVG/robust_estimation/CMakeFiles/openMVG_robust_estimation.dir/install-cxx-module-bmi-Release.cmake" OPTIONAL)
  elseif(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Mm][Ii][Nn][Ss][Ii][Zz][Ee][Rr][Ee][Ll])$")
    include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/openMVG/robust_estimation/CMakeFiles/openMVG_robust_estimation.dir/install-cxx-module-bmi-MinSizeRel.cmake" OPTIONAL)
  elseif(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Rr][Ee][Ll][Ww][Ii][Tt][Hh][Dd][Ee][Bb][Ii][Nn][Ff][Oo])$")
    include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/openMVG/robust_estimation/CMakeFiles/openMVG_robust_estimation.dir/install-cxx-module-bmi-RelWithDebInfo.cmake" OPTIONAL)
  elseif(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Mm][Aa][Ii][Nn][Tt][Aa][Ii][Nn][Ee][Rr])$")
    include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/openMVG/robust_estimation/CMakeFiles/openMVG_robust_estimation.dir/install-cxx-module-bmi-Maintainer.cmake" OPTIONAL)
  endif()
endif()

