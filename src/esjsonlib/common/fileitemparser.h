// SPDX-License-Identifier: GPL-3.0-only
/*
 * fileitemparser.h
 *
 * Copyright (c) 2021-2022, Andrew Sneed <wolfy@shitwolfymakes.com>
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

// for convenience
using json = nlohmann::json;

class FileItemParser
{
protected:
    // DATA
    std::vector<std::string> lines;

protected:
    // CREATORS
    FileItemParser();

public:
    // MANIPULATORS
    virtual json run() = 0;

    // ACCESSORS
    virtual json get_data() const = 0;

    static std::vector<std::string> tokenize(std::string);
    static bool isOneOf(std::string, std::vector<std::string>);
    static int getIndentLevel(std::string);
    static int collectNodeLines(std::vector<std::string> *, int, json *);
};

#endif // FILEITEMPARSER_H
