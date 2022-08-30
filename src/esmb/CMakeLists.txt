cmake_minimum_required(VERSION 3.16)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -Wpedantic")

option(BUILD_WERROR "Build with -Werror" ON)

if(BUILD_WERROR)
    if (LINUX)
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Werror")
    endif (LINUX)
endif(BUILD_WERROR)

# Executable
add_executable(esmb
    esmbapplication.cpp

    mainwindow.ui
    mainwindow.cpp
    main.cpp
)

target_link_libraries(esmb PRIVATE
    esjsonlib
    ${QT_LIBRARIES})
target_include_directories(esmb PRIVATE ${CMAKE_SOURCE_DIR}/src/esmb ${CMAKE_SOURCE_DIR}/src/esjsonlib)


set_target_properties(esmb PROPERTIES
    WIN32_EXECUTABLE ON
    MACOSX_BUNDLE ON
)
