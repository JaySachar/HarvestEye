#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "rerun_sdk" for configuration "RelWithDebInfo"
set_property(TARGET rerun_sdk APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(rerun_sdk PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELWITHDEBINFO "CXX"
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/rerun_sdk.lib"
  )

list(APPEND _cmake_import_check_targets rerun_sdk )
list(APPEND _cmake_import_check_files_for_rerun_sdk "${_IMPORT_PREFIX}/lib/rerun_sdk.lib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
