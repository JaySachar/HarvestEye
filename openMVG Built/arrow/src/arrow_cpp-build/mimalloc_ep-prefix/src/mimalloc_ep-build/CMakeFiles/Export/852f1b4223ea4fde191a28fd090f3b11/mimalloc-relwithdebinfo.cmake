#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "mimalloc-static" for configuration "RelWithDebInfo"
set_property(TARGET mimalloc-static APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(mimalloc-static PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELWITHDEBINFO "CXX"
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/mimalloc-2.0/mimalloc-static.lib"
  )

list(APPEND _cmake_import_check_targets mimalloc-static )
list(APPEND _cmake_import_check_files_for_mimalloc-static "${_IMPORT_PREFIX}/lib/mimalloc-2.0/mimalloc-static.lib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
