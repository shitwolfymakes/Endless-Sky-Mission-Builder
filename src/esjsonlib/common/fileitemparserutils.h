// SPDX-License-Identifier: GPL-3.0-only
/*
 * fileitemparserutils.h
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef FILEITEMPARSERUTILS_H
#define FILEITEMPARSERUTILS_H

#include <iosfwd>
#include <string>
#include <vector>

#include "nlohmann/json_fwd.hpp"
using json = nlohmann::json;

struct FileItemParserUtils {
    static std::vector<std::string> tokenize(std::string);
    static bool isOneOf(std::string, std::vector<std::string>);
    static int getIndentLevel(std::string);
    static int collectNodeLines(std::vector<std::string> *, int, json *);
};

#endif // FILEITEMPARSERUTILS_H
