// SPDX-License-Identifier: GPL-3.0-only
/*
 * fileitem.cpp
 *
 * Copyright (c) 2021, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "fileitem.h"

FileItem::FileItem() {}

void FileItem::setName(std::string name) {
    this->name = name;
}

void FileItem::setLines(std::vector<std::string> lines) {
    this->lines = lines;
}

void FileItem::appendLine(std::string line) {
    this->lines.push_back(line);
}

std::string FileItem::getName() const {
    return name;
}

std::vector<std::string> FileItem::getLines() const {
    return lines;
}

std::string FileItem::toString() const {
    // this is O(n), whereas std::accumulate is O(n^2) for strings
    std::string str;
    for (const auto &piece: lines) str += piece;
    return str;
}

void FileItem::printLines() const {
    std::cout << "Item Data:" << std::endl;
    for (const std::string &line: lines) {
        std::cout << line << std::endl;
    }
}
