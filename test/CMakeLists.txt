cmake_minimum_required(VERSION 3.14 FATAL_ERROR)

project (ESMB_Tests LANGUAGES CXX)

# Thanks to clementine-player for having a clear and concise CMakeLists for this
#include_directories(${GMOCK_INCLUDE_DIRS} ${GTEST_INCLUDE_DIRS})
enable_testing()

include_directories(${CMAKE_SOURCE_DIR}/src)
include_directories(${CMAKE_BINARY_DIR}/src)

include_directories(${QT_QTTEST_INCLUDE_DIR})


add_custom_target(esmb_test
    echo "Running ESMB tests"
    WORKING_DIRECTORY ${CURRENT_BINARY_DIR}
)
add_custom_target(build_tests
    WORKING_DIRECTORY ${CURRENT_BINARY_DIR}
)
add_dependencies(esmb_test build_tests)

add_library(test_gui_main STATIC EXCLUDE_FROM_ALL main.cpp)
target_link_libraries(test_gui_main esmb_lib)
set_target_properties(test_gui_main PROPERTIES COMPILE_DEFINITIONS GUI)

add_library(test_main STATIC EXCLUDE_FROM_ALL main.cpp)
target_link_libraries(test_main esmb_lib)

# Given a file foo_test.cpp, creates a target foo_test and adds it to the test target.
macro(add_test_file test_source gui_required)
    get_filename_component(TEST_NAME ${test_source} NAME_WE)
    add_executable(${TEST_NAME}
        EXCLUDE_FROM_ALL
        ${test_source}
    )

    target_link_libraries(${TEST_NAME} gtest_main esmb_lib ${QT_LIBRARIES} ${QT_QTTEST_LIBRARY} Qt5::Test)# ${GMOCK_LIBRARIES} clementine_lib test_utils Qt5::Test)
    set(GUI_REQUIRED ${gui_required})
    if (GUI_REQUIRED)
        target_link_libraries(${TEST_NAME} test_gui_main)
    else (GUI_REQUIRED)
        target_link_libraries(${TEST_NAME} test_main)
    endif (GUI_REQUIRED)

    check_cxx_compiler_flag("-Wno-bool-conversions" SUPPORTS_NOBOOL)
    if (SUPPORTS_NOBOOL)
        set_target_properties(${TEST_NAME} PROPERTIES COMPILE_FLAGS "-Wno-bool-conversions")
    endif (SUPPORTS_NOBOOL)

    add_custom_command(TARGET esmb_test POST_BUILD
        COMMAND ./${TEST_NAME}${CMAKE_EXECUTABLE_SUFFIX})
    add_dependencies(build_tests ${TEST_NAME})
endmacro (add_test_file)


add_test_file(parsers/filemissionitemparser_tests.cpp false)
