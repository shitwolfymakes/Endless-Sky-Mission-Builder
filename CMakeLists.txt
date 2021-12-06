# ESMB root CMakeLists.txt
cmake_minimum_required(VERSION 3.18)

project(esmb)

set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(QT_COMPONENTS Core Gui Widgets)
find_package(QT NAMES Qt5 COMPONENTS Widgets REQUIRED)
find_package(Qt${QT_VERSION_MAJOR} COMPONENTS Core Gui Widgets REQUIRED)
set(QT_LIBRARIES Qt${QT_VERSION_MAJOR}::Core Qt${QT_VERSION_MAJOR}::Gui Qt${QT_VERSION_MAJOR}::Widgets)
include_directories(${Qt5Widgets_INCLUDE_DIRS})

find_package(Threads)

if (WIN32)
    set(BOOST_ROOT C:/cpp_libs/boost/boost_1_77_0)
endif()
find_package(Boost REQUIRED)

# Use FetchContent to get dependencies on windows
include(FetchContent)

# Get googletest dependency
FetchContent_Declare(
    googletest
    # Specify the commit you depend on and update it regularly.
    URL https://github.com/google/googletest/archive/d61d4d8e64c08a662055e82904bbf90e108a704f.zip
)
# For Windows: Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)
include_directories(${googletest_SOURCE_DIR}/include)

# Get JSON dependency
FetchContent_Declare(json
    GIT_REPOSITORY https://github.com/ArthurSonzogni/nlohmann_json_cmake_fetchcontent
    GIT_TAG v3.10.4
)
FetchContent_GetProperties(json)
if(NOT json_POPULATED)
    FetchContent_Populate(json)
    add_subdirectory(${json_SOURCE_DIR} ${json_BINARY_DIR} EXCLUDE_FROM_ALL)
endif()
include_directories(${json_SOURCE_DIR}/include) # necessary as explained by https://stackoverflow.com/a/56593741/9820346

add_subdirectory(src)
add_subdirectory(test)
