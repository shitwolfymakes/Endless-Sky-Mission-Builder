cmake_minimum_required(VERSION 3.14 FATAL_ERROR)

# ---- Project ----

# Note: update this to your new project's name and version
project(
  ESMB
  VERSION 1.0
  LANGUAGES CXX
)

# ---- Include guards ----

if(PROJECT_SOURCE_DIR STREQUAL PROJECT_BINARY_DIR)
  message(
    FATAL_ERROR
      "In-source builds not allowed. Please make a new directory (called a build directory) and run CMake from there."
  )
endif()

# ---- Add dependencies via CPM ----
# see https://github.com/TheLartians/CPM.cmake for more info

include(cmake/CPM.cmake)
set(CPM_USE_LOCAL_PACKAGES OFF)
set(CPM_LOCAL_PACKAGES_ONLY OFF)

# PackageProject.cmake will be used to make our target installable
#CPMAddPackage("gh:TheLartians/PackageProject.cmake@1.8.0")

# ---- Create library ----

# Note: for header-only libraries change all PUBLIC flags to INTERFACE and create an interface
# target: add_library(${PROJECT_NAME} INTERFACE)
#add_library(${PROJECT_NAME} ${headers} ${sources})

#set_target_properties(${PROJECT_NAME} PROPERTIES CXX_STANDARD 17)

# being a cross-platform target, we enforce standards conformance on MSVC
#target_compile_options(${PROJECT_NAME} PUBLIC "$<$<COMPILE_LANG_AND_ID:CXX,MSVC>:/permissive->")

# Link dependencies
#target_link_libraries(${PROJECT_NAME} PRIVATE fmt::fmt)

#target_include_directories(
#  ${PROJECT_NAME} PUBLIC $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>
#                         $<INSTALL_INTERFACE:include/${PROJECT_NAME}-${PROJECT_VERSION}>
#)

# ---- Create an installable target ----
# this allows users to install and find the library via `find_package()`.

# the location where the project's version header will be placed should match the project's regular
# header paths
#string(TOLOWER ${PROJECT_NAME}/version.h VERSION_HEADER_LOCATION)

#packageProject(
#  NAME ${PROJECT_NAME}
#  VERSION ${PROJECT_VERSION}
#  NAMESPACE ${PROJECT_NAME}
#  BINARY_DIR ${PROJECT_BINARY_DIR}
#  INCLUDE_DIR ${PROJECT_SOURCE_DIR}/include
#  INCLUDE_DESTINATION include/${PROJECT_NAME}-${PROJECT_VERSION}
#  VERSION_HEADER "${VERSION_HEADER_LOCATION}"
#  COMPATIBILITY SameMajorVersion
#  DEPENDENCIES "fmt 7.1.3"
#)

set(ESMB_EXTERNAL_DIR ${ESMB_SOURCE_DIR}/external)
add_subdirectory(src)
