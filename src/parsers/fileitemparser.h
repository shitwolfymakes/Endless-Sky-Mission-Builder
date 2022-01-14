// SPDX-License-Identifier: GPL-3.0-only
/*
 * fileitemparser.h
 *
 * Copyright (c) 2021, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef FILEITEMPARSER_H
#define FILEITEMPARSER_H

#include <string>
#include <vector>

#include <QDebug>
#include <QString>
#include <boost/algorithm/string.hpp>
#include <boost/tokenizer.hpp>
#include "nlohmann/json.hpp"

#include "model/fileitemconstants.h"

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
    virtual json get_data() = 0;

    static int getIndentLevel(std::string);
    static int collectNodeLines(std::vector<std::string> *, int, json *);
};

#endif // FILEITEMPARSER_H
