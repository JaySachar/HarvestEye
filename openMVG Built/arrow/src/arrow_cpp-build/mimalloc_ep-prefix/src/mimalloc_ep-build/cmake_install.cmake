# Install script for directory: C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/mimalloc_ep-prefix/src/mimalloc_ep

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/mimalloc_ep/src/mimalloc_ep")
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
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/mimalloc-2.0" TYPE STATIC_LIBRARY FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/mimalloc_ep-prefix/src/mimalloc_ep-build/Debug/mimalloc-static.lib")
  elseif(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/mimalloc-2.0" TYPE STATIC_LIBRARY FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/mimalloc_ep-prefix/src/mimalloc_ep-build/Release/mimalloc-static.lib")
  elseif(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Mm][Ii][Nn][Ss][Ii][Zz][Ee][Rr][Ee][Ll])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/mimalloc-2.0" TYPE STATIC_LIBRARY FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/mimalloc_ep-prefix/src/mimalloc_ep-build/MinSizeRel/mimalloc-static.lib")
  elseif(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Rr][Ee][Ll][Ww][Ii][Tt][Hh][Dd][Ee][Bb][Ii][Nn][Ff][Oo])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/mimalloc-2.0" TYPE STATIC_LIBRARY FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/mimalloc_ep-prefix/src/mimalloc_ep-build/RelWithDebInfo/mimalloc-static.lib")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Dd][Ee][Bb][Uu][Gg])$")
    include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/mimalloc_ep-prefix/src/mimalloc_ep-build/CMakeFiles/mimalloc-static.dir/install-cxx-module-bmi-Debug.cmake" OPTIONAL)
  elseif(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
    include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/mimalloc_ep-prefix/src/mimalloc_ep-build/CMakeFiles/mimalloc-static.dir/install-cxx-module-bmi-Release.cmake" OPTIONAL)
  elseif(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Mm][Ii][Nn][Ss][Ii][Zz][Ee][Rr][Ee][Ll])$")
    include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/mimalloc_ep-prefix/src/mimalloc_ep-build/CMakeFiles/mimalloc-static.dir/install-cxx-module-bmi-MinSizeRel.cmake" OPTIONAL)
  elseif(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Rr][Ee][Ll][Ww][Ii][Tt][Hh][Dd][Ee][Bb][Ii][Nn][Ff][Oo])$")
    include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/mimalloc_ep-prefix/src/mimalloc_ep-build/CMakeFiles/mimalloc-static.dir/install-cxx-module-bmi-RelWithDebInfo.cmake" OPTIONAL)
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/mimalloc-2.0/mimalloc.cmake")
    file(DIFFERENT _cmake_export_file_changed FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/mimalloc-2.0/mimalloc.cmake"
         "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/mimalloc_ep-prefix/src/mimalloc_ep-build/CMakeFiles/Export/852f1b4223ea4fde191a28fd090f3b11/mimalloc.cmake")
    if(_cmake_export_file_changed)
      file(GLOB _cmake_old_config_files "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/mimalloc-2.0/mimalloc-*.cmake")
      if(_cmake_old_config_files)
        string(REPLACE ";" ", " _cmake_old_config_files_text "${_cmake_old_config_files}")
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/mimalloc-2.0/mimalloc.cmake\" will be replaced.  Removing files [${_cmake_old_config_files_text}].")
        unset(_cmake_old_config_files_text)
        file(REMOVE ${_cmake_old_config_files})
      endif()
      unset(_cmake_old_config_files)
    endif()
    unset(_cmake_export_file_changed)
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/mimalloc-2.0" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/mimalloc_ep-prefix/src/mimalloc_ep-build/CMakeFiles/Export/852f1b4223ea4fde191a28fd090f3b11/mimalloc.cmake")
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Dd][Ee][Bb][Uu][Gg])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/mimalloc-2.0" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/mimalloc_ep-prefix/src/mimalloc_ep-build/CMakeFiles/Export/852f1b4223ea4fde191a28fd090f3b11/mimalloc-debug.cmake")
  endif()
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Mm][Ii][Nn][Ss][Ii][Zz][Ee][Rr][Ee][Ll])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/mimalloc-2.0" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/mimalloc_ep-prefix/src/mimalloc_ep-build/CMakeFiles/Export/852f1b4223ea4fde191a28fd090f3b11/mimalloc-minsizerel.cmake")
  endif()
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Rr][Ee][Ll][Ww][Ii][Tt][Hh][Dd][Ee][Bb][Ii][Nn][Ff][Oo])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/mimalloc-2.0" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/mimalloc_ep-prefix/src/mimalloc_ep-build/CMakeFiles/Export/852f1b4223ea4fde191a28fd090f3b11/mimalloc-relwithdebinfo.cmake")
  endif()
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/mimalloc-2.0" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/mimalloc_ep-prefix/src/mimalloc_ep-build/CMakeFiles/Export/852f1b4223ea4fde191a28fd090f3b11/mimalloc-release.cmake")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mimalloc-2.0" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/mimalloc_ep-prefix/src/mimalloc_ep/include/mimalloc.h")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mimalloc-2.0" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/mimalloc_ep-prefix/src/mimalloc_ep/include/mimalloc-override.h")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mimalloc-2.0" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/mimalloc_ep-prefix/src/mimalloc_ep/include/mimalloc-new-delete.h")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/mimalloc-2.0" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/mimalloc_ep-prefix/src/mimalloc_ep/cmake/mimalloc-config.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/mimalloc-2.0" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/mimalloc_ep-prefix/src/mimalloc_ep/cmake/mimalloc-config-version.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build/mimalloc_ep-prefix/src/mimalloc_ep-build/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
