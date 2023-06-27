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

namespace FileItemParserUtils {
    std::vector<std::string> tokenize(std::string);
    bool isOneOf(std::string, std::vector<std::string>);
    int getIndentLevel(std::string);

    // Takes in a pointer to a list of strings and the index of the first
    // line in that lis, and pass a pointer to either a json or string list
    // to store the node lines in.
    // Returns the index of the last line stored. If the list of strings it
    // collects from contains only 1 element, or the string it starts from
    // is the last in the list, returns the integer that was passed in
    int collectNodeLines(std::vector<std::string> *, int, json *);
    int collectNodeLines(std::vector<std::string> *, int, std::vector<std::string> *);
}

#endif // FILEITEMPARSERUTILS_H
