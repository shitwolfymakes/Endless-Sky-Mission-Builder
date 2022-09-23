// SPDX-License-Identifier: GPL-3.0-only
/*
 * fileitemparser.h
 *
 * Copyright (c) 2021-2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef FILEITEMPARSER_H
#define FILEITEMPARSER_H

#include "nlohmann/json_fwd.hpp"
using json = nlohmann::json;

class FileItemParser {
public:
    // CREATORS
    virtual ~FileItemParser();

    // MANIPULATORS
    virtual json run() = 0;

    // ACCESSORS
    virtual json getData() const = 0;
};

#endif // FILEITEMPARSER_H
