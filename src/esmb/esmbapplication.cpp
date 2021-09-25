#include "esmbapplication.h"

ESMBApplication& ESMBApplication::getInstance() {
    // static objects are constructed only once
    static ESMBApplication esmb;
    return esmb;
}

QStringList ESMBApplication::getNames() {
    return itemNames;
}
