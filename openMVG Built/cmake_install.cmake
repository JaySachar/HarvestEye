# Install script for directory: C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/openMVG_dependencies" TYPE DIRECTORY FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG/src/dependencies/" FILES_MATCHING REGEX "/[^/]*\\.hpp$" REGEX "/[^/]*\\.h$")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/openMVG/cmake/OpenMVGTargets.cmake")
    file(DIFFERENT _cmake_export_file_changed FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/openMVG/cmake/OpenMVGTargets.cmake"
         "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/CMakeFiles/Export/233ae21498dfa638fefe2c46f6f49464/OpenMVGTargets.cmake")
    if(_cmake_export_file_changed)
      file(GLOB _cmake_old_config_files "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/openMVG/cmake/OpenMVGTargets-*.cmake")
      if(_cmake_old_config_files)
        string(REPLACE ";" ", " _cmake_old_config_files_text "${_cmake_old_config_files}")
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/openMVG/cmake/OpenMVGTargets.cmake\" will be replaced.  Removing files [${_cmake_old_config_files_text}].")
        unset(_cmake_old_config_files_text)
        file(REMOVE ${_cmake_old_config_files})
      endif()
      unset(_cmake_old_config_files)
    endif()
    unset(_cmake_export_file_changed)
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/openMVG/cmake" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/CMakeFiles/Export/233ae21498dfa638fefe2c46f6f49464/OpenMVGTargets.cmake")
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Dd][Ee][Bb][Uu][Gg])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/openMVG/cmake" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/CMakeFiles/Export/233ae21498dfa638fefe2c46f6f49464/OpenMVGTargets-debug.cmake")
  endif()
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Mm][Aa][Ii][Nn][Tt][Aa][Ii][Nn][Ee][Rr])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/openMVG/cmake" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/CMakeFiles/Export/233ae21498dfa638fefe2c46f6f49464/OpenMVGTargets-maintainer.cmake")
  endif()
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Mm][Ii][Nn][Ss][Ii][Zz][Ee][Rr][Ee][Ll])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/openMVG/cmake" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/CMakeFiles/Export/233ae21498dfa638fefe2c46f6f49464/OpenMVGTargets-minsizerel.cmake")
  endif()
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Rr][Ee][Ll][Ww][Ii][Tt][Hh][Dd][Ee][Bb][Ii][Nn][Ff][Oo])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/openMVG/cmake" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/CMakeFiles/Export/233ae21498dfa638fefe2c46f6f49464/OpenMVGTargets-relwithdebinfo.cmake")
  endif()
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/openMVG/cmake" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/CMakeFiles/Export/233ae21498dfa638fefe2c46f6f49464/OpenMVGTargets-release.cmake")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/openMVG/cmake" TYPE FILE FILES "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/OpenMVGConfig.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/dependencies/osi_clp/cmake_install.cmake")
  include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/third_party/cmake_install.cmake")
  include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/testing/cmake_install.cmake")
  include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/openMVG/cmake_install.cmake")
  include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/openMVG_Samples/cmake_install.cmake")
  include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/software/cmake_install.cmake")
  include("C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/nonFree/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
