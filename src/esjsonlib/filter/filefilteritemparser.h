// SPDX-License-Identifier: GPL-3.0-only
/*
 * filefilteritemparser.h
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef FILEFILTERITEMPARSER_H
#define FILEFILTERITEMPARSER_H

#include "common/fileitemparserimpl.h"

#include <iosfwd>

#include "nlohmann/json.hpp"
using json = nlohmann::json;

class FileFilterItemParser : public FileItemParserImpl
{
    json filter;
public:
    // CREATORS
    FileFilterItemParser(std::vector<std::string>);

    // MANIPULATORS
    json run();

    int parseFilter(std::vector<std::string> *, int);

    // ACCESSORS
    json getData() const;
};

#endif // FILEFILTERITEMPARSER_H
