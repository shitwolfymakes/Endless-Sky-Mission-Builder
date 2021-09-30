// SPDX-License-Identifier: GPL-3.0-only
/*
 * fileitem.cpp
 *
 * Copyright (c) 2021, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "fileitem.h"

FileItem::FileItem() {};

string FileItem::getName() {
    return name;
}

void FileItem::setName(string name) {
    this->name = name;
}

void FileItem::appendLine(string line) {
    this->lines.push_back(line);
}

vector<string> FileItem::getLines() {
    return lines;
}

void FileItem::setLines(vector<string> lines) {
    this->lines = lines;
}

string FileItem::toString() {
    // this is O(n), whereas std::accumulate is O(n^2) for strings
    std::string str;
    for (const auto &piece: lines) str += piece;
    return str;
}

void FileItem::printItem() {
    qDebug() << "Item Data:";
    for (const std::string &line: lines) {
        QString qLine = QString::fromStdString(line);
        qDebug("\t%s", qUtf8Printable(qLine));
    }
}
