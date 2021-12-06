set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

set(SOURCES
    esmbapplication.cpp
    main.cpp
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

add_executable(esmb main.cpp)
target_link_libraries(esmb PUBLIC ${QT_LIBRARIES})

set_target_properties(esmb PROPERTIES
    MACOSX_BUNDLE_GUI_IDENTIFIER shitwolfymakes.com
)

target_link_libraries(esmb PRIVATE esmb_lib nlohmann_json::nlohmann_json)
