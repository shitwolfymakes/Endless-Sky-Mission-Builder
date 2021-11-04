QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

CONFIG += c++11

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

SOURCES += \
    esmbapplication.cpp \
    main.cpp \
    mainwindow.cpp \
    model/fileitem.cpp \
    model/itemevent.cpp \
    model/itemgovernment.cpp \
    model/itemmission.cpp \
    model/itemphrase.cpp \
    model/itemship.cpp \
    parsers/datafileparser.cpp \
    parsers/fileitemparser.cpp \
    parsers/filemissionitemparser.cpp

HEADERS += \
    esmbapplication.h \
    mainwindow.h \
    model/fileitem.h \
    model/fileitemconstants.h \
    model/itemevent.h \
    model/itemgovernment.h \
    model/itemmission.h \
    model/itemphrase.h \
    model/itemship.h \
    parsers/datafileparser.h \
    parsers/fileitemparser.h \
    parsers/filemissionitemparser.h

FORMS += \
    mainwindow.ui

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target

RESOURCES += \
    resources.qrc

DISTFILES +=

INCLUDEPATH += \
    C:/cpp_libs/boost/boost_1_77_0 \
    C:/cpp_libs/nlohmann_json/3.10.4/
LIBS += -L/cpp_libs/boost/boost_1_77_0/stage/lib
