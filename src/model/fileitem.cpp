// SPDX-License-Identifier: GPL-3.0-only
/*
 * fileitem.cpp
 *
 * Copyright (c) 2021, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "fileitem.h"

FileItem::FileItem() {};

std::string FileItem::getName() {
    return name;
}

void FileItem::setName(std::string name) {
    this->name = name;
}

void FileItem::appendLine(std::string line) {
    this->lines.push_back(line);
}

std::vector<std::string> FileItem::getLines() {
    return lines;
}

void FileItem::setLines(std::vector<std::string> lines) {
    this->lines = lines;
}

std::string FileItem::toString() {
    // this is O(n), whereas std::accumulate is O(n^2) for strings
    std::string str;
    for (const auto &piece: lines) str += piece;
    return str;
}

void FileItem::printLines() {
    qDebug() << "Item Data:";
    for (const std::string &line: lines) {
        QString qLine = QString::fromStdString(line);
        qDebug("\t%s", qUtf8Printable(qLine));
    }
}
