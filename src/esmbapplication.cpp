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

void ESMBApplication::setNames(QStringList itemNames) {
    this->itemNames = itemNames;
}

QStringList ESMBApplication::getNames() {
    return itemNames;
}

void ESMBApplication::updateItemNames() {
    QStringList ids;
    json j = getJsonItems();
    for (auto it = j.begin(); it != j.end(); ++it) {
        json item = *it;
        if (!it->contains("id")) {
            continue;
        }
        std::string id = item["id"];
        ids.append(QString::fromStdString(id));
    }
    setNames(ids);
}

void ESMBApplication::setJsonItems(json jsonItems) {
    this->jsonItems = jsonItems;
}

json ESMBApplication::getJsonItems() {
    return jsonItems;
}

void ESMBApplication::updateIdMap() {
    // WARNING: this code assumes there are no duplicate items
    idMap.clear();
    // populate a map class var
    // fill the map with the key="id", value=<mission obj reference> for each item in getJsonItems
    json j = getJsonItems();
    for (auto it = j.begin(); it != j.end(); ++it) {
        json item = *it;
        if (!it->contains("id")) {
            continue;
        }
        std::string id = item["id"];
        idMap.emplace(id, std::ref(item));
    }
    updateItemNames();
}
