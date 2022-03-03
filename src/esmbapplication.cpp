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
    json *j = getJsonItems();
    for (auto it = j->begin(); it != j->end(); ++it) {
        if (!it->contains("id")) {
            continue;
        }
        ids.append(QString::fromStdString((*it)["id"]));
    }
    setNames(ids);
}

void ESMBApplication::setCurrentItem(json *j) {
    this->currentItem = j;
}

json* ESMBApplication::getCurrentItem() {
    return currentItem;
}

void ESMBApplication::setJsonItems(json jsonItems) {
    this->jsonItems = jsonItems;
}

json* ESMBApplication::getJsonItems() {
    return &jsonItems;
}

json* ESMBApplication::getJsonItemById(std::string id) {
    json *j = getJsonItems();
    for (auto it = j->begin(); it != j->end(); ++it) {
        json item = *it;
        if (!it->contains("id")) {
            continue;
        }
        if (id.compare((*it)["id"]) == 0) {
            return &(*it);
        }
    }
    return nullptr;
}
