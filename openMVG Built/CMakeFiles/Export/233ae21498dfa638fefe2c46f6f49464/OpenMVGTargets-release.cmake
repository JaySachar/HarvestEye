#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "OpenMVG::lib_CoinUtils" for configuration "Release"
set_property(TARGET OpenMVG::lib_CoinUtils APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OpenMVG::lib_CoinUtils PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/lib_CoinUtils.lib"
  )

list(APPEND _cmake_import_check_targets OpenMVG::lib_CoinUtils )
list(APPEND _cmake_import_check_files_for_OpenMVG::lib_CoinUtils "${_IMPORT_PREFIX}/lib/lib_CoinUtils.lib" )

# Import target "OpenMVG::lib_Osi" for configuration "Release"
set_property(TARGET OpenMVG::lib_Osi APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OpenMVG::lib_Osi PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/lib_Osi.lib"
  )

list(APPEND _cmake_import_check_targets OpenMVG::lib_Osi )
list(APPEND _cmake_import_check_files_for_OpenMVG::lib_Osi "${_IMPORT_PREFIX}/lib/lib_Osi.lib" )

# Import target "OpenMVG::lib_clp" for configuration "Release"
set_property(TARGET OpenMVG::lib_clp APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OpenMVG::lib_clp PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/lib_clp.lib"
  )

list(APPEND _cmake_import_check_targets OpenMVG::lib_clp )
list(APPEND _cmake_import_check_files_for_OpenMVG::lib_clp "${_IMPORT_PREFIX}/lib/lib_clp.lib" )

# Import target "OpenMVG::lib_OsiClpSolver" for configuration "Release"
set_property(TARGET OpenMVG::lib_OsiClpSolver APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OpenMVG::lib_OsiClpSolver PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/lib_OsiClpSolver.lib"
  )

list(APPEND _cmake_import_check_targets OpenMVG::lib_OsiClpSolver )
list(APPEND _cmake_import_check_files_for_OpenMVG::lib_OsiClpSolver "${_IMPORT_PREFIX}/lib/lib_OsiClpSolver.lib" )

# Import target "OpenMVG::openMVG_stlplus" for configuration "Release"
set_property(TARGET OpenMVG::openMVG_stlplus APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OpenMVG::openMVG_stlplus PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/openMVG_stlplus.lib"
  )

list(APPEND _cmake_import_check_targets OpenMVG::openMVG_stlplus )
list(APPEND _cmake_import_check_files_for_OpenMVG::openMVG_stlplus "${_IMPORT_PREFIX}/lib/openMVG_stlplus.lib" )

# Import target "OpenMVG::openMVG_jpeg" for configuration "Release"
set_property(TARGET OpenMVG::openMVG_jpeg APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OpenMVG::openMVG_jpeg PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "C"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/openMVG_jpeg.lib"
  )

list(APPEND _cmake_import_check_targets OpenMVG::openMVG_jpeg )
list(APPEND _cmake_import_check_files_for_OpenMVG::openMVG_jpeg "${_IMPORT_PREFIX}/lib/openMVG_jpeg.lib" )

# Import target "OpenMVG::openMVG_zlib" for configuration "Release"
set_property(TARGET OpenMVG::openMVG_zlib APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OpenMVG::openMVG_zlib PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "C"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/openMVG_zlib.lib"
  )

list(APPEND _cmake_import_check_targets OpenMVG::openMVG_zlib )
list(APPEND _cmake_import_check_files_for_OpenMVG::openMVG_zlib "${_IMPORT_PREFIX}/lib/openMVG_zlib.lib" )

# Import target "OpenMVG::openMVG_png" for configuration "Release"
set_property(TARGET OpenMVG::openMVG_png APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OpenMVG::openMVG_png PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "C"
  IMPORTED_LINK_INTERFACE_LIBRARIES_RELEASE "OpenMVG::openMVG_zlib"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/openMVG_png.lib"
  )

list(APPEND _cmake_import_check_targets OpenMVG::openMVG_png )
list(APPEND _cmake_import_check_files_for_OpenMVG::openMVG_png "${_IMPORT_PREFIX}/lib/openMVG_png.lib" )

# Import target "OpenMVG::openMVG_tiff" for configuration "Release"
set_property(TARGET OpenMVG::openMVG_tiff APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OpenMVG::openMVG_tiff PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "C;CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/openMVG_tiff.lib"
  )

list(APPEND _cmake_import_check_targets OpenMVG::openMVG_tiff )
list(APPEND _cmake_import_check_files_for_OpenMVG::openMVG_tiff "${_IMPORT_PREFIX}/lib/openMVG_tiff.lib" )

# Import target "OpenMVG::openMVG_ceres" for configuration "Release"
set_property(TARGET OpenMVG::openMVG_ceres APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OpenMVG::openMVG_ceres PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/openMVG_ceres.lib"
  )

list(APPEND _cmake_import_check_targets OpenMVG::openMVG_ceres )
list(APPEND _cmake_import_check_files_for_OpenMVG::openMVG_ceres "${_IMPORT_PREFIX}/lib/openMVG_ceres.lib" )

# Import target "OpenMVG::openMVG_easyexif" for configuration "Release"
set_property(TARGET OpenMVG::openMVG_easyexif APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OpenMVG::openMVG_easyexif PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/openMVG_easyexif.lib"
  )

list(APPEND _cmake_import_check_targets OpenMVG::openMVG_easyexif )
list(APPEND _cmake_import_check_files_for_OpenMVG::openMVG_easyexif "${_IMPORT_PREFIX}/lib/openMVG_easyexif.lib" )

# Import target "OpenMVG::openMVG_fast" for configuration "Release"
set_property(TARGET OpenMVG::openMVG_fast APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OpenMVG::openMVG_fast PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/openMVG_fast.lib"
  )

list(APPEND _cmake_import_check_targets OpenMVG::openMVG_fast )
list(APPEND _cmake_import_check_files_for_OpenMVG::openMVG_fast "${_IMPORT_PREFIX}/lib/openMVG_fast.lib" )

# Import target "OpenMVG::openMVG_exif" for configuration "Release"
set_property(TARGET OpenMVG::openMVG_exif APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OpenMVG::openMVG_exif PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/openMVG_exif.lib"
  )

list(APPEND _cmake_import_check_targets OpenMVG::openMVG_exif )
list(APPEND _cmake_import_check_files_for_OpenMVG::openMVG_exif "${_IMPORT_PREFIX}/lib/openMVG_exif.lib" )

# Import target "OpenMVG::openMVG_features" for configuration "Release"
set_property(TARGET OpenMVG::openMVG_features APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OpenMVG::openMVG_features PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/openMVG_features.lib"
  )

list(APPEND _cmake_import_check_targets OpenMVG::openMVG_features )
list(APPEND _cmake_import_check_files_for_OpenMVG::openMVG_features "${_IMPORT_PREFIX}/lib/openMVG_features.lib" )

# Import target "OpenMVG::openMVG_image" for configuration "Release"
set_property(TARGET OpenMVG::openMVG_image APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OpenMVG::openMVG_image PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/openMVG_image.lib"
  )

list(APPEND _cmake_import_check_targets OpenMVG::openMVG_image )
list(APPEND _cmake_import_check_files_for_OpenMVG::openMVG_image "${_IMPORT_PREFIX}/lib/openMVG_image.lib" )

# Import target "OpenMVG::openMVG_linearProgramming" for configuration "Release"
set_property(TARGET OpenMVG::openMVG_linearProgramming APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OpenMVG::openMVG_linearProgramming PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/openMVG_linearProgramming.lib"
  )

list(APPEND _cmake_import_check_targets OpenMVG::openMVG_linearProgramming )
list(APPEND _cmake_import_check_files_for_OpenMVG::openMVG_linearProgramming "${_IMPORT_PREFIX}/lib/openMVG_linearProgramming.lib" )

# Import target "OpenMVG::openMVG_lInftyComputerVision" for configuration "Release"
set_property(TARGET OpenMVG::openMVG_lInftyComputerVision APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OpenMVG::openMVG_lInftyComputerVision PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/openMVG_lInftyComputerVision.lib"
  )

list(APPEND _cmake_import_check_targets OpenMVG::openMVG_lInftyComputerVision )
list(APPEND _cmake_import_check_files_for_OpenMVG::openMVG_lInftyComputerVision "${_IMPORT_PREFIX}/lib/openMVG_lInftyComputerVision.lib" )

# Import target "OpenMVG::openMVG_geometry" for configuration "Release"
set_property(TARGET OpenMVG::openMVG_geometry APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OpenMVG::openMVG_geometry PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/openMVG_geometry.lib"
  )

list(APPEND _cmake_import_check_targets OpenMVG::openMVG_geometry )
list(APPEND _cmake_import_check_files_for_OpenMVG::openMVG_geometry "${_IMPORT_PREFIX}/lib/openMVG_geometry.lib" )

# Import target "OpenMVG::openMVG_matching" for configuration "Release"
set_property(TARGET OpenMVG::openMVG_matching APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OpenMVG::openMVG_matching PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/openMVG_matching.lib"
  )

list(APPEND _cmake_import_check_targets OpenMVG::openMVG_matching )
list(APPEND _cmake_import_check_files_for_OpenMVG::openMVG_matching "${_IMPORT_PREFIX}/lib/openMVG_matching.lib" )

# Import target "OpenMVG::openMVG_kvld" for configuration "Release"
set_property(TARGET OpenMVG::openMVG_kvld APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OpenMVG::openMVG_kvld PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/openMVG_kvld.lib"
  )

list(APPEND _cmake_import_check_targets OpenMVG::openMVG_kvld )
list(APPEND _cmake_import_check_files_for_OpenMVG::openMVG_kvld "${_IMPORT_PREFIX}/lib/openMVG_kvld.lib" )

# Import target "OpenMVG::openMVG_matching_image_collection" for configuration "Release"
set_property(TARGET OpenMVG::openMVG_matching_image_collection APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OpenMVG::openMVG_matching_image_collection PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/openMVG_matching_image_collection.lib"
  )

list(APPEND _cmake_import_check_targets OpenMVG::openMVG_matching_image_collection )
list(APPEND _cmake_import_check_files_for_OpenMVG::openMVG_matching_image_collection "${_IMPORT_PREFIX}/lib/openMVG_matching_image_collection.lib" )

# Import target "OpenMVG::openMVG_multiview" for configuration "Release"
set_property(TARGET OpenMVG::openMVG_multiview APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OpenMVG::openMVG_multiview PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/openMVG_multiview.lib"
  )

list(APPEND _cmake_import_check_targets OpenMVG::openMVG_multiview )
list(APPEND _cmake_import_check_files_for_OpenMVG::openMVG_multiview "${_IMPORT_PREFIX}/lib/openMVG_multiview.lib" )

# Import target "OpenMVG::openMVG_numeric" for configuration "Release"
set_property(TARGET OpenMVG::openMVG_numeric APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OpenMVG::openMVG_numeric PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/openMVG_numeric.lib"
  )

list(APPEND _cmake_import_check_targets OpenMVG::openMVG_numeric )
list(APPEND _cmake_import_check_files_for_OpenMVG::openMVG_numeric "${_IMPORT_PREFIX}/lib/openMVG_numeric.lib" )

# Import target "OpenMVG::openMVG_robust_estimation" for configuration "Release"
set_property(TARGET OpenMVG::openMVG_robust_estimation APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OpenMVG::openMVG_robust_estimation PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/openMVG_robust_estimation.lib"
  )

list(APPEND _cmake_import_check_targets OpenMVG::openMVG_robust_estimation )
list(APPEND _cmake_import_check_files_for_OpenMVG::openMVG_robust_estimation "${_IMPORT_PREFIX}/lib/openMVG_robust_estimation.lib" )

# Import target "OpenMVG::openMVG_system" for configuration "Release"
set_property(TARGET OpenMVG::openMVG_system APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OpenMVG::openMVG_system PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/openMVG_system.lib"
  )

list(APPEND _cmake_import_check_targets OpenMVG::openMVG_system )
list(APPEND _cmake_import_check_files_for_OpenMVG::openMVG_system "${_IMPORT_PREFIX}/lib/openMVG_system.lib" )

# Import target "OpenMVG::openMVG_sfm" for configuration "Release"
set_property(TARGET OpenMVG::openMVG_sfm APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OpenMVG::openMVG_sfm PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/openMVG_sfm.lib"
  )

list(APPEND _cmake_import_check_targets OpenMVG::openMVG_sfm )
list(APPEND _cmake_import_check_files_for_OpenMVG::openMVG_sfm "${_IMPORT_PREFIX}/lib/openMVG_sfm.lib" )

# Import target "OpenMVG::vlsift" for configuration "Release"
set_property(TARGET OpenMVG::vlsift APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OpenMVG::vlsift PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "C"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/vlsift.lib"
  )

list(APPEND _cmake_import_check_targets OpenMVG::vlsift )
list(APPEND _cmake_import_check_files_for_OpenMVG::vlsift "${_IMPORT_PREFIX}/lib/vlsift.lib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
