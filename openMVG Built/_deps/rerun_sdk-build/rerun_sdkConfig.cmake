
####### Expanded from @PACKAGE_INIT@ by configure_package_config_file() #######
####### Any changes to this file will be overwritten by the next CMake run ####
####### The input file was Config.cmake.in                            ########

get_filename_component(PACKAGE_PREFIX_DIR "${CMAKE_CURRENT_LIST_DIR}/../../../" ABSOLUTE)

####################################################################################

include("${CMAKE_CURRENT_LIST_DIR}/rerun_sdkTargets.cmake")

set(RERUN_LIB_DIR "${CMAKE_CURRENT_LIST_DIR}/../..")

# Setup `rerun_c` (imported libraries can't be exported!)
add_library(rerun_c STATIC IMPORTED GLOBAL)
get_filename_component(RERUN_C_LIB_NAME "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/_deps/rerun_sdk-src/lib/rerun_c__win_x64.lib" NAME)
set_target_properties(rerun_c PROPERTIES IMPORTED_LOCATION "${RERUN_LIB_DIR}/${RERUN_C_LIB_NAME}")
if(APPLE)
    target_link_libraries(rerun_c INTERFACE "-framework CoreFoundation" "-framework IOKit")
elseif(UNIX) # if(LINUX) # CMake 3.25
    target_link_libraries(rerun_c INTERFACE "-lm -ldl -pthread")
elseif(WIN32)
    target_link_libraries(rerun_c INTERFACE ws2_32.dll Bcrypt.dll Userenv.dll ntdll.dll)
endif()

# Setup `rerun_arrow_target` (imported libraries can't be exported and package dependencies need to be re-declared)
# if(ON AND NOT OFF)
if(ON AND NOT OFF)
    message(STATUS "Rerun is using bundled arrow library.")

    add_library(rerun_arrow_target STATIC IMPORTED GLOBAL)
    get_filename_component(RERUN_ARROW_LIB_NAME "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/lib/arrow_static.lib" NAME)
    set_target_properties(rerun_arrow_target PROPERTIES IMPORTED_LOCATION "${RERUN_LIB_DIR}/${RERUN_ARROW_LIB_NAME}")

    # We have to explicitly opt in the arrow bundled dependencies, otherwise we're missing the symbols for mimalloc.
    add_library(arrow_targetBundledDeps STATIC IMPORTED)
    get_filename_component(RERUN_ARROW_DEPS_LIB_NAME "C:/Users/Jay/Documents/Github/HarvestEye/openMVG Built/arrow/lib/arrow_bundled_dependencies.lib" NAME)
    set_target_properties(arrow_targetBundledDeps PROPERTIES IMPORTED_LOCATION "${RERUN_LIB_DIR}/${RERUN_ARROW_DEPS_LIB_NAME}")
    target_link_libraries(rerun_arrow_target INTERFACE arrow_targetBundledDeps)
else()
    if(OFF)
        message(WARNING
            "Rerun got built with an automatically downloaded version of libArrow,"
            "but it was not bundled as part of the install since export of shared libArrow is not supported yet."
            "Set RERUN_ARROW_LINK_SHARED to OFF during install or make sure find_package succeeds for Arrow."
        )
    endif()

    find_package(Arrow REQUIRED)

    message(STATUS "Rerun is using a system installed libArrow.")
    option(RERUN_ARROW_LINK_SHARED "Link to the Arrow shared library" OFF)

    if(RERUN_ARROW_LINK_SHARED)
        add_library(rerun_arrow_target ALIAS Arrow::arrow_shared)
    else()
        add_library(rerun_arrow_target ALIAS Arrow::arrow_static)
    endif()
endif()
