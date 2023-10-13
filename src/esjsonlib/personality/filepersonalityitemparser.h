// SPDX-License-Identifier: GPL-3.0-only
/*
 * filepersonalityitemparser.h
 *
 * Copyright (c) 2023, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef FILEPERSONALITYITEMPARSER_H
#define FILEPERSONALITYITEMPARSER_H

#include <common/fileitemparserimpl.h>

#include <iosfwd>

#include "nlohmann/json.hpp"
using json = nlohmann::json;

class FilePersonalityItemParser : public FileItemParserImpl {
    //json personality;

public:
    // CREATORS
    FilePersonalityItemParser(std::vector<std::string>);

    // MANIPULATORS
    json run();
    void addPersonalityType(json *, std::string) const;

    // ACCESSORS
    json getData() const;
};

#endif // FILEPERSONALITYITEMPARSER_H
