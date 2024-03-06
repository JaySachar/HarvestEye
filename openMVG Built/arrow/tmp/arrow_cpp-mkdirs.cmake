# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp"
  "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-build"
  "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow"
  "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/tmp"
  "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-stamp"
  "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src"
  "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-stamp"
)

set(configSubDirs Debug;Release;MinSizeRel;RelWithDebInfo;Maintainer)
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/src/arrow_cpp-stamp${cfgdir}") # cfgdir has leading slash
endif()
