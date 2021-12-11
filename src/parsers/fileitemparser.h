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

    FileItemParser(std::vector<std::string>);

    virtual json run() = 0;
    std::vector<std::string> tokenize(std::string);
    int getIndentLevel(std::string);
    bool isOneOf(std::string, std::vector<std::string>);
    // TODO: Implement parseFilter here
};

#endif // FILEITEMPARSER_H
