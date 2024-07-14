# Install script for directory: C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/_deps/rerun_sdk-src

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
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/Windows-AMD64-/Debug/rerun_sdk.lib")
  elseif(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/Windows-AMD64-/Release/rerun_sdk.lib")
  elseif(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Mm][Ii][Nn][Ss][Ii][Zz][Ee][Rr][Ee][Ll])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/Windows-AMD64-/MinSizeRel/rerun_sdk.lib")
  elseif(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Rr][Ee][Ll][Ww][Ii][Tt][Hh][Dd][Ee][Bb][Ii][Nn][Ff][Oo])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/Windows-AMD64-/RelWithDebInfo/rerun_sdk.lib")
  elseif(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Mm][Aa][Ii][Nn][Tt][Aa][Ii][Nn][Ee][Rr])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/Windows-AMD64-/Maintainer/rerun_sdk.lib")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/_deps/rerun_sdk-src/src/" FILES_MATCHING REGEX "/[^/]*\\.hpp$" REGEX "/[^/]*\\.h$")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/_deps/rerun_sdk-src/lib/rerun_c__win_x64.lib")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE FILE FILES
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/lib/arrow_static.lib"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/lib/arrow_bundled_dependencies.lib"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/rerun_sdk/rerun_sdkTargets.cmake")
    file(DIFFERENT _cmake_export_file_changed FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/rerun_sdk/rerun_sdkTargets.cmake"
         "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/_deps/rerun_sdk-build/CMakeFiles/Export/ff0d44ecb878fe106368fbe2d1dd9267/rerun_sdkTargets.cmake")
    if(_cmake_export_file_changed)
      file(GLOB _cmake_old_config_files "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/rerun_sdk/rerun_sdkTargets-*.cmake")
      if(_cmake_old_config_files)
        string(REPLACE ";" ", " _cmake_old_config_files_text "${_cmake_old_config_files}")
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/rerun_sdk/rerun_sdkTargets.cmake\" will be replaced.  Removing files [${_cmake_old_config_files_text}].")
        unset(_cmake_old_config_files_text)
        file(REMOVE ${_cmake_old_config_files})
      endif()
      unset(_cmake_old_config_files)
    endif()
    unset(_cmake_export_file_changed)
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/rerun_sdk" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/_deps/rerun_sdk-build/CMakeFiles/Export/ff0d44ecb878fe106368fbe2d1dd9267/rerun_sdkTargets.cmake")
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Dd][Ee][Bb][Uu][Gg])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/rerun_sdk" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/_deps/rerun_sdk-build/CMakeFiles/Export/ff0d44ecb878fe106368fbe2d1dd9267/rerun_sdkTargets-debug.cmake")
  endif()
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Mm][Aa][Ii][Nn][Tt][Aa][Ii][Nn][Ee][Rr])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/rerun_sdk" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/_deps/rerun_sdk-build/CMakeFiles/Export/ff0d44ecb878fe106368fbe2d1dd9267/rerun_sdkTargets-maintainer.cmake")
  endif()
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Mm][Ii][Nn][Ss][Ii][Zz][Ee][Rr][Ee][Ll])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/rerun_sdk" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/_deps/rerun_sdk-build/CMakeFiles/Export/ff0d44ecb878fe106368fbe2d1dd9267/rerun_sdkTargets-minsizerel.cmake")
  endif()
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Rr][Ee][Ll][Ww][Ii][Tt][Hh][Dd][Ee][Bb][Ii][Nn][Ff][Oo])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/rerun_sdk" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/_deps/rerun_sdk-build/CMakeFiles/Export/ff0d44ecb878fe106368fbe2d1dd9267/rerun_sdkTargets-relwithdebinfo.cmake")
  endif()
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/rerun_sdk" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/_deps/rerun_sdk-build/CMakeFiles/Export/ff0d44ecb878fe106368fbe2d1dd9267/rerun_sdkTargets-release.cmake")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/rerun_sdk" TYPE FILE FILES
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/_deps/rerun_sdk-build/rerun_sdkConfig.cmake"
    "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/_deps/rerun_sdk-build/rerun_sdkConfigVersion.cmake"
    )
endif()

