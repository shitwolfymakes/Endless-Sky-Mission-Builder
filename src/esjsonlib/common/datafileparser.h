// SPDX-License-Identifier: GPL-3.0-only
/*
 * datafileparser.h
 *
 * Copyright (c) 2021, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef DATAFILEPARSER_H
#define DATAFILEPARSER_H

#include <iosfwd>
#include <string>
#include <vector>

#include "nlohmann/json.hpp"
using json = nlohmann::json;

#include "common/fileitemconstants.h"

class FileItem;

class DataFileParser {
    std::string rawData;
    std::vector<std::string> lines;
    std::vector<std::unique_ptr<FileItem>> fileItems;
    json jsonItems;

public:
    // CREATORS
    DataFileParser(std::string);

    // MANIPULATORS
    void run();
    void storeItemForParsing(int, std::string, ItemType);

    // ACCESSORS
    void printRawData() const;
    bool isFileItemStartLine(std::string) const;
    json getJsonItems() const;
};

#endif // DATAFILEPARSER_H
