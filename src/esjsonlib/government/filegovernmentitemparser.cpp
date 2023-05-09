// SPDX-License-Identifier: GPL-3.0-only
/*
 * filegovernmentitemparser.cpp
 *
 * Copyright (c) 2023, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "filegovernmentitemparser.h"

#include <iostream>

#include <boost/algorithm/string.hpp>

#include "common/fileitemparserutils.h"
using utils = FileItemParserUtils;

FileGovernmentItemParser::FileGovernmentItemParser(std::vector<std::string> lines) {
    setLines(lines);
}

json FileGovernmentItemParser::run() {
    std::cout << "Parsing government node to JSON" << std::endl;
    std::vector<std::string> tokens;

    std::vector<std::string> lines = getLines();
    for (int i = 0; i < static_cast<int>(lines.size()); i++) {
        // start by tokenizing each line
        tokens = utils::tokenize(lines.at(i));
        //std::cout << "LINE: " << tokens.at(0) << std::endl;

        if (tokens.size() == 0) {
            std::cout << "\tERROR: NO TOKENS FOUND ON LINE: " << lines.at(i) << std::endl;
        }
        else if (tokens.at(0).compare("government") == 0) {
            parseId(tokens.at(1));
        } else if (tokens.at(0).compare("display name") == 0) {
            parseId(tokens.at(1));
        }
    }
    //std::cout << "Government data: " << govt.dump(4) << std::endl;
    return govt;
}

void FileGovernmentItemParser::parseId(std::string token) {
    std::cout << "\tGovernment ID is: " << token << std::endl;
    govt["id"] = token;
}

void FileGovernmentItemParser::parseDisplayName(std::string token) {
    std::cout << "\tGovernment ID is: " << token << std::endl;
    govt["display_name"] = token;
}

json FileGovernmentItemParser::getData() const {
    return govt;
}
