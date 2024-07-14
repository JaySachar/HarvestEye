# Install script for directory: C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/software/SfMWebGLViewer

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
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/bin" TYPE EXECUTABLE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/Windows-AMD64-/Debug/openMVG_main_openMVG2WebGL.exe")
  elseif(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/bin" TYPE EXECUTABLE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/Windows-AMD64-/Release/openMVG_main_openMVG2WebGL.exe")
  elseif(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Mm][Ii][Nn][Ss][Ii][Zz][Ee][Rr][Ee][Ll])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/bin" TYPE EXECUTABLE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/Windows-AMD64-/MinSizeRel/openMVG_main_openMVG2WebGL.exe")
  elseif(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Rr][Ee][Ll][Ww][Ii][Tt][Hh][Dd][Ee][Bb][Ii][Nn][Ff][Oo])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/bin" TYPE EXECUTABLE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/Windows-AMD64-/RelWithDebInfo/openMVG_main_openMVG2WebGL.exe")
  elseif(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Mm][Aa][Ii][Nn][Tt][Aa][Ii][Nn][Ee][Rr])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/bin" TYPE EXECUTABLE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/Windows-AMD64-/Maintainer/openMVG_main_openMVG2WebGL.exe")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Dd][Ee][Bb][Uu][Gg])$")
    include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/software/SfMWebGLViewer/CMakeFiles/openMVG_main_openMVG2WebGL.dir/install-cxx-module-bmi-Debug.cmake" OPTIONAL)
  elseif(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
    include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/software/SfMWebGLViewer/CMakeFiles/openMVG_main_openMVG2WebGL.dir/install-cxx-module-bmi-Release.cmake" OPTIONAL)
  elseif(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Mm][Ii][Nn][Ss][Ii][Zz][Ee][Rr][Ee][Ll])$")
    include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/software/SfMWebGLViewer/CMakeFiles/openMVG_main_openMVG2WebGL.dir/install-cxx-module-bmi-MinSizeRel.cmake" OPTIONAL)
  elseif(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Rr][Ee][Ll][Ww][Ii][Tt][Hh][Dd][Ee][Bb][Ii][Nn][Ff][Oo])$")
    include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/software/SfMWebGLViewer/CMakeFiles/openMVG_main_openMVG2WebGL.dir/install-cxx-module-bmi-RelWithDebInfo.cmake" OPTIONAL)
  elseif(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Mm][Aa][Ii][Nn][Tt][Aa][Ii][Nn][Ee][Rr])$")
    include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/software/SfMWebGLViewer/CMakeFiles/openMVG_main_openMVG2WebGL.dir/install-cxx-module-bmi-Maintainer.cmake" OPTIONAL)
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/openMVG/webgl/common" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/software/SfMWebGLViewer/common/camera.js")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/openMVG/webgl/common" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/software/SfMWebGLViewer/common/camera_gizmo.js")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/openMVG/webgl/common" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/software/SfMWebGLViewer/common/common.js")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/openMVG/webgl/common" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/software/SfMWebGLViewer/common/dual_quaternion.js")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/openMVG/webgl/common" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/software/SfMWebGLViewer/common/index.html")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/openMVG/webgl/common" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/software/SfMWebGLViewer/common/main.js")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/openMVG/webgl/common" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/software/SfMWebGLViewer/common/matrix3.js")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/openMVG/webgl/common" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/software/SfMWebGLViewer/common/matrix4.js")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/openMVG/webgl/common" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/software/SfMWebGLViewer/common/plane.js")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/openMVG/webgl/common" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/software/SfMWebGLViewer/common/point_cloud.js")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/openMVG/webgl/common" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/software/SfMWebGLViewer/common/quaternion.js")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/openMVG/webgl/common" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/software/SfMWebGLViewer/common/render_context.js")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/openMVG/webgl/common" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/software/SfMWebGLViewer/common/shader.js")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/openMVG/webgl/common" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/software/SfMWebGLViewer/common/style.css")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/openMVG/webgl/common" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/software/SfMWebGLViewer/common/trackball.js")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/openMVG/webgl/common" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/software/SfMWebGLViewer/common/vector.js")
endif()

