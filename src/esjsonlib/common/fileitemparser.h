// SPDX-License-Identifier: GPL-3.0-only
/*
 * fileitemparser.h
 *
 * Copyright (c) 2021, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef FILEITEMPARSER_H
#define FILEITEMPARSER_H

#include <iostream>
#include <string>
#include <vector>

#include <boost/algorithm/string.hpp>
#include <boost/format.hpp>
#include <boost/tokenizer.hpp>
#include "nlohmann/json.hpp"

#include "common/fileitemconstants.h"

// for convenience
using json = nlohmann::json;

class FileItemParser
{
protected:
    std::vector<std::string> lines;
    json data;

    FileItemParser(std::vector<std::string>);

    std::vector<std::string> tokenize(std::string);
    bool isOneOf(std::string, std::vector<std::string>);
    // TODO: Implement parseFilter here

public:
    virtual json run() = 0;
    virtual json get_data() const = 0;

    static int getIndentLevel(std::string);
    static int collectNodeLines(std::vector<std::string> *, int, json *);
};

#endif // FILEITEMPARSER_H
