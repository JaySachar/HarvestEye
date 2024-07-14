#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "rerun_sdk" for configuration "MinSizeRel"
set_property(TARGET rerun_sdk APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(rerun_sdk PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_MINSIZEREL "CXX"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/lib/rerun_sdk.lib"
  )

list(APPEND _cmake_import_check_targets rerun_sdk )
list(APPEND _cmake_import_check_files_for_rerun_sdk "${_IMPORT_PREFIX}/lib/rerun_sdk.lib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
