cmake_minimum_required(VERSION 3.20)

project(ESMB VERSION 0.1 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# ---- Include guards ----
if(PROJECT_SOURCE_DIR STREQUAL PROJECT_BINARY_DIR)
  message(
    FATAL_ERROR
      "In-source builds not allowed. Please make a new directory (called a build directory) and run CMake from there."
  )
endif()

# includes and top level flags
include(CheckCXXCompilerFlag)
set(ESMB_BUILD_TESTS ON)

find_package(Boost 1.71.0 REQUIRED)

# QT
list(APPEND CMAKE_PREFIX_PATH "~/Qt/6.5.3/gcc_64")
find_package(Qt6 REQUIRED COMPONENTS Core Gui Widgets Test)
qt_standard_project_setup()

set(QT_LIBRARIES Qt6::Core Qt6::Gui Qt6::Widgets)

# setup CPM for package management
include(cmake/CPM.cmake)
set(CPM_USE_LOCAL_PACKAGES OFF)
set(CPM_LOCAL_PACKAGES_ONLY OFF)

# add the src subproject
set(ESMB_EXTERNAL_DIR ${ESMB_SOURCE_DIR}/external)
add_subdirectory(src/esmb)
add_subdirectory(src/esjsonlib)

# add the test subproject
if (ESMB_BUILD_TESTS)
    add_subdirectory(tests)
endif()
