// SPDX-License-Identifier: GPL-3.0-only
/*
 * datafileparser.h
 *
 * Copyright (c) 2021, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef DATAFILEPARSER_H
#define DATAFILEPARSER_H

#include <iostream>
#include <regex>
#include <string>
#include <vector>

#include "boost/algorithm/string/join.hpp"

#include "common//fileitem.h"
#include "common/fileitemconstants.h"

#include "event/itemevent.h"
#include "government/itemgovernment.h"
#include "mission/itemmission.h"
#include "phrase/itemphrase.h"
#include "ship/itemship.h"
#include "substitutions/itemsubstitutions.h"

class DataFileParser
{
private:
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
