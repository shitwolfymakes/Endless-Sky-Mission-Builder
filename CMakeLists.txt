cmake_minimum_required(VERSION 3.14 FATAL_ERROR)

# ---- Project ----

# Note: update this to your new project's name and version
project(
  ESMB
  VERSION 0.1
  LANGUAGES CXX
)

# ---- Include guards ----

if(PROJECT_SOURCE_DIR STREQUAL PROJECT_BINARY_DIR)
  message(
    FATAL_ERROR
      "In-source builds not allowed. Please make a new directory (called a build directory) and run CMake from there."
  )
endif()

set(BUILD_TESTS ON)

# setup CPM for package management
include(cmake/CPM.cmake)
set(CPM_USE_LOCAL_PACKAGES OFF)
set(CPM_LOCAL_PACKAGES_ONLY OFF)

# add the src subproject
set(ESMB_EXTERNAL_DIR ${ESMB_SOURCE_DIR}/external)
add_subdirectory(src)

# add the test subproject
if (ESMB_BUILD_TESTS)
  add_subdirectory(test)
endif()
