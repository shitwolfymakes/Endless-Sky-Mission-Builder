cmake_minimum_required(VERSION 3.16)

# Executable
add_library(esjsonlib STATIC
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
    parsers/filephraseitemparser.cpp
    parsers/filesubstitutionsitemparser.cpp
)

add_subdirectory(${ESMB_EXTERNAL_DIR} ${ESMB_BINARY_DIR}/external)

target_link_libraries(esjsonlib PUBLIC nlohmann_json)

target_include_directories(esjsonlib SYSTEM PUBLIC ${Boost_INCLUDE_DIRS})
target_include_directories(esjsonlib PRIVATE ${CMAKE_CURRENT_SOURCE_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/model ${CMAKE_CURRENT_SOURCE_DIR}/parser)
