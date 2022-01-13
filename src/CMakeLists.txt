cmake_minimum_required(VERSION 3.14 FATAL_ERROR)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -Wpedantic")

option(BUILD_WERROR "Build with -Werror" ON)

if(BUILD_WERROR)
    if (LINUX)
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Werror")
    endif (LINUX)
endif(BUILD_WERROR)

set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

# ---- Add source files ----
set(SOURCES
    esmbapplication.cpp
    mainwindow.cpp

    model/fileitem.cpp
    model/itemevent.cpp
    model/itemgovernment.cpp
    model/itemmission.cpp
    model/itemphrase.cpp
    model/itemship.cpp
    model/itemsubstitution.cpp

    parsers/datafileparser.cpp
    parsers/fileitemparser.cpp
    parsers/filemissionitemparser.cpp
    parsers/filesubstitutionitemparser.cpp
)

set(HEADERS
    esmbapplication.h
    mainwindow.h

    model/fileitem.h
    model/fileitemconstants.h
    model/itemevent.h
    model/itemgovernment.h
    model/itemmission.h
    model/itemphrase.h
    model/itemship.h
    model/itemsubstitution.h

    parsers/datafileparser.h
    parsers/fileitemparser.h
    parsers/filemissionitemparser.h
    parsers/filesubstitutionitemparser.h
)

set(UI
    mainwindow.ui
)

set(RESOURCES resources.qrc)

link_directories(${Boost_LIBRARY_DIRS})

find_package(Threads)

if (WIN32)
    set(BOOST_ROOT C:/cpp_libs/boost/boost_1_77_0)
endif()
find_package(Boost REQUIRED)

# Library
add_library(esmb_lib STATIC
    ${SOURCES}
    ${HEADERS}
    ${MOC}
    ${UIC}
    ${QRC}
)


target_include_directories(esmb_lib SYSTEM PUBLIC
    ${Boost_INCLUDE_DIRS}
)

target_include_directories(esmb_lib PUBLIC ${ESMB_SOURCE_DIR}/src)


# Executable
add_executable(esmb main.cpp)
target_link_libraries(esmb esmb_lib)

add_subdirectory(${ESMB_EXTERNAL_DIR} ${ESMB_BINARY_DIR}/external)

target_link_libraries(esmb_lib PUBLIC nlohmann_json ${QT_LIBRARIES})
