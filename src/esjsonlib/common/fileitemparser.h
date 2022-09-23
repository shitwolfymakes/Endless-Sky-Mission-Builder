// SPDX-License-Identifier: GPL-3.0-only
/*
 * fileitemparser.h
 *
 * Copyright (c) 2021-2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef FILEITEMPARSER_H
#define FILEITEMPARSER_H

#include <string>
#include <vector>

#include "nlohmann/json_fwd.hpp"
using json = nlohmann::json;

class FileItemParser {
    std::vector<std::string> lines;

protected:
    // CREATORS
    FileItemParser();

    // MANIPULATORS
    virtual json run() = 0;
    void setLines(std::vector<std::string>);

    // ACCESSORS
    std::vector<std::string> getLines() const;
    virtual json getData() const = 0;
};

#endif // FILEITEMPARSER_H
