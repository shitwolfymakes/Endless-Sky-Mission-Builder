// SPDX-License-Identifier: GPL-3.0-only
/*
 * esmbapplication.h
 *
 * Copyright (c) 2021, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef ESMBAPPLICATION_H
#define ESMBAPPLICATION_H

#include <QStringList>

class ESMBApplication
{
private:
    // private default constructor (prohibits creation from the outside)
    ESMBApplication() {};

    // private copy constructor (prohibits copy creation)
    ESMBApplication(const ESMBApplication&);

    // private assignment operator (prohibits assignment)
    const ESMBApplication& operator=(const ESMBApplication&);

    // member data
    QStringList itemNames;

public:
    // controlled instantiation
    static ESMBApplication& getInstance();

    // public methods
    QStringList getNames();

};

#endif // ESMBAPPLICATION_H
