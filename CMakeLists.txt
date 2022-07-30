cmake_minimum_required(VERSION 3.16)

project(ESMB VERSION 0.1 LANGUAGES CXX)

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

# QT
#set(QT_MIN_VERSION 5.15.0)
find_package(Qt6 REQUIRED COMPONENTS Core Gui Widgets Test)

set(QT_LIBRARIES Qt6::Core Qt6::Gui Qt6::Widgets)

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
