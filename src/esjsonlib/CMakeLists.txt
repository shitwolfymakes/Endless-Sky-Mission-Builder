cmake_minimum_required(VERSION 3.16)

# Executable
add_library(esjsonlib STATIC
    model/fileitem.cpp
    model/fileitem.h
    model/itemevent.cpp
    model/itemevent.h
    model/itemgovernment.cpp
    model/itemgovernment.h
    model/itemmission.cpp
    model/itemmission.h
    model/itemphrase.cpp
    model/itemphrase.h
    model/itemship.cpp
    model/itemship.h
    model/itemsubstitutions.cpp
    model/itemsubstitutions.h

    model/fileitemconstants.h

    parsers/datafileparser.cpp
    parsers/datafileparser.h
    parsers/fileitemparser.cpp
    parsers/fileitemparser.h
    parsers/filemissionitemparser.cpp
    parsers/filemissionitemparser.h
    parsers/filephraseitemparser.cpp
    parsers/filephraseitemparser.h
    parsers/filesubstitutionsitemparser.cpp
    parsers/filesubstitutionsitemparser.h
)

add_subdirectory(${ESMB_EXTERNAL_DIR} ${ESMB_BINARY_DIR}/external)

target_link_libraries(esjsonlib PUBLIC nlohmann_json)

target_include_directories(esjsonlib SYSTEM PUBLIC ${Boost_INCLUDE_DIRS})
target_include_directories(esjsonlib PRIVATE ${CMAKE_CURRENT_SOURCE_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/model ${CMAKE_CURRENT_SOURCE_DIR}/parser)
