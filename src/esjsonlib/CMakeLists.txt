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
    model/itemship.cpp
    model/itemship.h

    model/fileitemconstants.h

    parsers/datafileparser.cpp
    parsers/datafileparser.h
    parsers/fileitemparser.cpp
    parsers/fileitemparser.h
    parsers/filemissionitemparser.cpp
    parsers/filemissionitemparser.h

    phrase/itemphrase.h
    phrase/itemphrase.cpp
    phrase/filephraseitemparser.h
    phrase/filephraseitemparser.cpp

    substitutions/itemsubstitutions.h
    substitutions/itemsubstitutions.cpp
    substitutions/filesubstitutionsitemparser.h
    substitutions/filesubstitutionsitemparser.cpp
)

add_subdirectory(${ESMB_EXTERNAL_DIR} ${ESMB_BINARY_DIR}/external)

target_link_libraries(esjsonlib PUBLIC nlohmann_json)

target_include_directories(esjsonlib SYSTEM PUBLIC ${Boost_INCLUDE_DIRS})
target_include_directories(esjsonlib PRIVATE ${CMAKE_CURRENT_SOURCE_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/model ${CMAKE_CURRENT_SOURCE_DIR}/parser)
