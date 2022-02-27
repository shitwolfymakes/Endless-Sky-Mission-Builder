// SPDX-License-Identifier: GPL-3.0-only
/*
 * esmbapplication.h
 *
 * Copyright (c) 2021, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef ESMBAPPLICATION_H
#define ESMBAPPLICATION_H

#include <QStringList>

#include "nlohmann/json.hpp"

using json = nlohmann::json;

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
    json jsonItems;
    std::map<std::string, json> idMap;

public:
    // controlled instantiation
    static ESMBApplication& getInstance();

    // public methods
    void setNames(QStringList);
    QStringList getNames();
    void updateItemNames();

    void setJsonItems(json);
    json getJsonItems();

    void updateIdMap();
};

#endif // ESMBAPPLICATION_H
