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
        if (tokens.size() == 0) {
            std::cout << "\tERROR: NO TOKENS FOUND ON LINE: " << lines.at(i) << std::endl;
        } else {
            std::cout << "\tERROR: INCORRECT NUMBER OF TOKENS FOUND ON LINE: " << lines.at(i) << std::endl;
        }

        //i = parseFilter(&lines, i);
    }
    //std::cout << "Filter data: " << substitutions.dump(4) << std::endl;
    return filter;
}

int FileFilterItemParser::parseFilter(std::vector<std::string> *nodeLines, int startingIndex) {
    std::cout << "FILTER PARSING NOT IMPLEMENTED YET" << std::endl;
    return -1;
}

bool FileFilterItemParser::isModifier(std::string token) const {
    bool result = false;
    return result;
}

json FileFilterItemParser::getData() const {
    return filter;
}
