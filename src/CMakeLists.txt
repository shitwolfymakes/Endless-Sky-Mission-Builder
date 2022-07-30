cmake_minimum_required(VERSION 3.16)

set(CMAKE_CXX_STANDARD 17)
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
    model/itemsubstitutions.cpp

    parsers/datafileparser.cpp
    parsers/fileitemparser.cpp
    parsers/filemissionitemparser.cpp
    parsers/filesubstitutionsitemparser.cpp
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
    model/itemsubstitutions.h

    parsers/datafileparser.h
    parsers/fileitemparser.h
    parsers/filemissionitemparser.h
    parsers/filesubstitutionsitemparser.h
)

set(UI
    mainwindow.ui
)

set(RESOURCES resources.qrc)

link_directories(${Boost_LIBRARY_DIRS})

find_package(Threads)
find_package(Boost 1.71 REQUIRED)

# Executable
add_executable(esmb main.cpp)
target_compile_features(esmb PRIVATE cxx_std_17)
set_target_properties(esmb PROPERTIES
    WIN32_EXECUTABLE ON
    MACOSX_BUNDLE ON
)

# Library
add_library(esmb_lib STATIC
    ${SOURCES}
    ${HEADERS}
    ${MOC}
    ${UIC}
    ${QRC}
)
target_include_directories(esmb_lib SYSTEM PUBLIC ${Boost_INCLUDE_DIRS})

target_link_libraries(esmb_lib PRIVATE ${QT_LIBRARIES})
target_include_directories(esmb_lib PUBLIC ${ESMB_SOURCE_DIR}/src)
add_subdirectory(${ESMB_EXTERNAL_DIR} ${ESMB_BINARY_DIR}/external)
target_link_libraries(esmb_lib PUBLIC nlohmann_json)

target_link_libraries(esmb PRIVATE esmb_lib ${QT_LIBRARIES})
