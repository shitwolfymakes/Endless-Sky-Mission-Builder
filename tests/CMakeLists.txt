cmake_minimum_required(VERSION 3.16)

project (ESMB_Tests)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fpermissive")

# Thanks to clementine-player for having a clear and concise CMakeLists for this

include_directories(${CMAKE_SOURCE_DIR}/src/esmb)
include_directories(${CMAKE_BINARY_DIR}/src/esmb)
include_directories(${CMAKE_SOURCE_DIR}/src/esjsonlib)
include_directories(${CMAKE_BINARY_DIR}/src/esjsonlib)

include_directories(${QT_QTTEST_INCLUDE_DIR})

set(HEADERS
    common/fileitemparser_tests.h
    mission/filemissionitemparser_tests.h
    phrase/filephraseitemparser_tests.h
    substitutions/filesubstitutionsitemparser_tests.h
)

add_custom_target(esmb_test
    echo "Running ESMB tests"
    WORKING_DIRECTORY ${CURRENT_BINARY_DIR}
)
add_custom_target(build_tests
    WORKING_DIRECTORY ${CURRENT_BINARY_DIR}
)
add_dependencies(esmb_test build_tests)

add_library(test_gui_main STATIC EXCLUDE_FROM_ALL main.cpp ${HEADERS})
target_link_libraries(test_gui_main esjsonlib gtest gtest_main gmock)
target_include_directories(test_gui_main PRIVATE ${CMAKE_SOURCE_DIR}/src/esmb ${CMAKE_SOURCE_DIR}/src/esjsonlib)
set_target_properties(test_gui_main PROPERTIES COMPILE_DEFINITIONS GUI)

add_library(test_main STATIC EXCLUDE_FROM_ALL main.cpp ${HEADERS})
target_link_libraries(test_main esjsonlib gtest gtest_main gmock)
target_include_directories(test_main PRIVATE ${CMAKE_SOURCE_DIR}/src/esmb ${CMAKE_SOURCE_DIR}/src/esjsonlib)

# Given a file foo_test.cpp, creates a target foo_test and adds it to the test target.
macro(add_test_file file_path test_source gui_required)
    get_filename_component(TEST_NAME ${test_source} NAME_WE)
    add_executable(${TEST_NAME}
        #EXCLUDE_FROM_ALL # this prevents the test from being built (when targeting ALL)
        "${file_path}/${test_source}.cpp"
        "${file_path}/${test_source}.h"
    )

    target_link_libraries(${TEST_NAME} gtest gtest_main gmock esjsonlib ${QT_LIBRARIES} ${QT_QTTEST_LIBRARY} Qt6::Test)
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


add_test_file(common fileitemparser_tests false)
add_test_file(mission filemissionitemparser_tests false)
add_test_file(phrase filephraseitemparser_tests false)
add_test_file(substitutions filesubstitutionsitemparser_tests false)
