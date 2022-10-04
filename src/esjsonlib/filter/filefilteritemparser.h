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

class FileFilterItemParser : public FileItemParserImpl {
    json filter;

public:
    // CREATORS
    FileFilterItemParser(std::vector<std::string>);

    // MANIPULATORS
    json run();

    // Take the lines and the starting index of a filter node, and
    // return the index of the last line of the filter
    void parseFilter(std::vector<std::string> *);;
    void parsePlanets(std::vector<std::string> *, std::string);
    void parseSystems(std::vector<std::string> *, std::string);
    void parseGovernments(std::vector<std::string> *, std::string);
    void parseAttributes(std::vector<std::string> *, std::string);
    void parseOutfits(std::vector<std::string> *, int, std::string);
    void parseCategories(std::vector<std::string> *, std::string);

    // ACCESSORS
    // Returns true if the string is a valid filter modifier.
    // If not, false is returned
    static bool isModifier(std::string);
    json getData() const;
};

#endif // FILEFILTERITEMPARSER_H
