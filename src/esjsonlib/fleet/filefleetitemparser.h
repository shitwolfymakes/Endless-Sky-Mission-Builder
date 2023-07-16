// SPDX-License-Identifier: GPL-3.0-only
/*
 * fileleetitemparser.h
 *
 * Copyright (c) 2023, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef FILEFLEETITEMPARSER_H
#define FILEFLEETITEMPARSER_H

#include <common/fileitemparserimpl.h>

#include "nlohmann/json.hpp"
using json = nlohmann::json;

class FileFleetItemParser : public FileItemParserImpl {
    json fleet;

public:
    // CREATORS
    FileFleetItemParser(std::vector<std::string>);

    // MANIPULATORS
    json run();

    // ACCESSORS
    json getData() const;
};

#endif // FILEFLEETITEMPARSER_H
