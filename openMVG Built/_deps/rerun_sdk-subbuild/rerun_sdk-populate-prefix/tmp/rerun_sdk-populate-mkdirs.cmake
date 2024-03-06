# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/_deps/rerun_sdk-src"
  "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/_deps/rerun_sdk-build"
  "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/_deps/rerun_sdk-subbuild/rerun_sdk-populate-prefix"
  "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/_deps/rerun_sdk-subbuild/rerun_sdk-populate-prefix/tmp"
  "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/_deps/rerun_sdk-subbuild/rerun_sdk-populate-prefix/src/rerun_sdk-populate-stamp"
  "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/_deps/rerun_sdk-subbuild/rerun_sdk-populate-prefix/src"
  "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/_deps/rerun_sdk-subbuild/rerun_sdk-populate-prefix/src/rerun_sdk-populate-stamp"
)

set(configSubDirs Debug)
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/_deps/rerun_sdk-subbuild/rerun_sdk-populate-prefix/src/rerun_sdk-populate-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/_deps/rerun_sdk-subbuild/rerun_sdk-populate-prefix/src/rerun_sdk-populate-stamp${cfgdir}") # cfgdir has leading slash
endif()
