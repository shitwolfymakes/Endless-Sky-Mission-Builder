cmake_minimum_required(VERSION 3.16)

# Executable
add_library(esjsonlib STATIC
    common/fileitemconstants.h
    common/fileitem.h
    common/fileitem.cpp
    common/datafileparser.h
    common/datafileparser.cpp
    common/fileitemparser.h
    common/fileitemparser.cpp

    event/itemevent.h
    event/itemevent.cpp

    government/itemgovernment.h
    government/itemgovernment.cpp

    mission/itemmission.h
    mission/itemmission.cpp
    mission/filemissionitemparser.h
    mission/filemissionitemparser.cpp

    phrase/itemphrase.h
    phrase/itemphrase.cpp
    phrase/filephraseitemparser.h
    phrase/filephraseitemparser.cpp

    ship/itemship.h
    ship/itemship.cpp

    substitutions/itemsubstitutions.h
    substitutions/itemsubstitutions.cpp
    substitutions/filesubstitutionsitemparser.h
    substitutions/filesubstitutionsitemparser.cpp
)

add_subdirectory(${ESMB_EXTERNAL_DIR} ${ESMB_BINARY_DIR}/external)

target_link_libraries(esjsonlib PUBLIC nlohmann_json)

target_include_directories(esjsonlib SYSTEM PUBLIC ${Boost_INCLUDE_DIRS})
target_include_directories(esjsonlib PRIVATE ${CMAKE_CURRENT_SOURCE_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/model ${CMAKE_CURRENT_SOURCE_DIR}/parser)