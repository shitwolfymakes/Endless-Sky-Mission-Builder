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

#include "model/fileitem.h"
#include "model/fileitemconstants.h"

#include "event/itemevent.h"
#include "government/itemgovernment.h"
#include "mission/itemmission.h"
#include "phrase/itemphrase.h"
#include "ship/itemship.h"
#include "substitutions/itemsubstitutions.h"

class DataFileParser
{
private:
    // store the file data in different formats
    std::string rawData;
    std::vector<std::string> lines;

    std::vector<std::unique_ptr<FileItem>> fileItems;
    json jsonItems;

public:
    DataFileParser(std::string);

    //const QStringList toList();
    std::vector<std::string> toStdStringVector();
    void printRawData();
    void run();
    void storeItemForParsing(int, std::string, ItemType);
    bool isFileItemStartLine(std::string);

    json getJsonItems();
};

#endif // DATAFILEPARSER_H
