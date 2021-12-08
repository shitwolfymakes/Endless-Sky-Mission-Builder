cmake_minimum_required(VERSION 3.14 FATAL_ERROR)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

find_package(QT NAMES Qt5 COMPONENTS Widgets REQUIRED)
find_package(Qt${QT_VERSION_MAJOR} COMPONENTS Core Gui Widgets REQUIRED)
set(QT_LIBRARIES Qt${QT_VERSION_MAJOR}::Core Qt${QT_VERSION_MAJOR}::Gui Qt${QT_VERSION_MAJOR}::Widgets)
include_directories(${Qt5Widgets_INCLUDE_DIRS})

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

    parsers/datafileparser.cpp
    parsers/fileitemparser.cpp
    parsers/filemissionitemparser.cpp
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

    parsers/datafileparser.h
    parsers/fileitemparser.h
    parsers/filemissionitemparser.h
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
add_library(esmb_src OBJECT
    ${SOURCES}
    ${HEADERS}
    ${MOC}
    ${UIC}
    ${QRC})

target_include_directories(esmb_src SYSTEM PUBLIC
    ${Boost_INCLUDE_DIRS}
)

target_include_directories(esmb_src PUBLIC ${ESMB_SOURCE_DIR}/src)


# Executable
add_executable(esmb_exec main.cpp)
target_link_libraries(esmb_exec PUBLIC esmb_src ${QT_LIBRARIES})
set_target_properties(esmb_exec PROPERTIES OUTPUT_NAME esmb)

add_subdirectory(${ESMB_EXTERNAL_DIR} ${ESMB_BINARY_DIR}/external)

target_link_libraries(esmb_src PUBLIC nlohmann_json)
