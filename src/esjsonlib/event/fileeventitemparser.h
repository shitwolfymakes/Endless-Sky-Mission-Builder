// SPDX-License-Identifier: GPL-3.0-only
/*
 * fileeventitemparser.h
 *
 * Copyright (c) 2023, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef FILEEVENTITEMPARSER_H
#define FILEEVENTITEMPARSER_H

#include "common/fileitemparserimpl.h"

#include "nlohmann/json.hpp"
using json = nlohmann::json;

class FileEventItemParser : public FileItemParserImpl {
    json event;

public:
    // CREATORS
    FileEventItemParser(std::vector<std::string>);

    // MANIPULATORS
    json run();

    void parseDate(std::vector<std::string>);

    // ACCESSORS
    json getData() const;
};

#endif // FILEEVENTITEMPARSER_H
