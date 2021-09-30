// SPDX-License-Identifier: GPL-3.0-only
/*
 * esmbapplication.cpp
 *
 * Copyright (c) 2021, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "esmbapplication.h"

ESMBApplication& ESMBApplication::getInstance() {
    // static objects are constructed only once
    static ESMBApplication esmb;
    return esmb;
}

QStringList ESMBApplication::getNames() {
    return itemNames;
}
