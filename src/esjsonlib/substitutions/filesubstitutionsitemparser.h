// SPDX-License-Identifier: GPL-3.0-only
/*
 * filesubstitutionsitemparser.h
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef FILESUBSTITUTIONSITEMPARSER_H
#define FILESUBSTITUTIONSITEMPARSER_H

#include "common/fileitemparserimpl.h"

#include "nlohmann/json.hpp"
using json = nlohmann::json;

class FileSubstitutionsItemParser : public FileItemParserImpl
{
private:
    // DATA
    json substitutions;

public:
    // CREATORS
    FileSubstitutionsItemParser(std::vector<std::string>);

    // MANIPULATORS
    json run();

    int parseSubstitution(std::vector<std::string> *, int);

    // ACCESSORS
    json getData() const;
};

#endif // FILESUBSTITUTIONSITEMPARSER_H
