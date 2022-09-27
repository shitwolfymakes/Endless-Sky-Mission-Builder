// SPDX-License-Identifier: GPL-3.0-only
/*
 * filefilteritemparser.cpp
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "filefilteritemparser.h"

#include <iostream>

#include "common/fileitemparserutils.h"
using utils = FileItemParserUtils;

FileFilterItemParser::FileFilterItemParser(std::vector<std::string> lines) {
    setLines(lines);
}

json FileFilterItemParser::run() {
    std::cout << "Parsing filter node to JSON" << std::endl;
    std::vector<std::string> tokens;

    std::vector<std::string> lines = getLines();
    for (int i = 1; i < static_cast<int>(lines.size()); i++) {
        tokens = utils::tokenize(lines.at(i));
        //std::cout << "LINE: " << tokens.at(0) << std::endl;
        // ES Logic:
        // if not or neighbor
        //    add empty filter obj to not or not neighbors
        //    if num tokens is 1
        //        recurse, storing in last filter in list
        //    else
        //        save value of in last filter in list
        // else
        //    save value in this filter

        // ESMB logic
        // if not or neighbor
        //    if num tokens is 1
        //        i = collectNodeLines
        //        create new parser
        //        add parsed json to list
        //    else
        //        save constraint to the list of nots or neighbors
        // else
        //     save constraint to the list
    }
    //std::cout << "Filter data: " << substitutions.dump(4) << std::endl;
    return filter;
}

void FileFilterItemParser::parseFilter(std::vector<std::string> *nodeLines, int startingIndex) {
    std::cout << "FILTER PARSING NOT IMPLEMENTED YET" << std::endl;
}

// Determine whether or not the string passed is a valid filter modifier
bool FileFilterItemParser::isModifier(std::string token) {
    bool result = false;
    if (token.compare("not") == 0) {
        result = true;
    } else if (token.compare("neighbor") == 0) {
        result = true;
    }
    return result;
}

json FileFilterItemParser::getData() const {
    return filter;
}
