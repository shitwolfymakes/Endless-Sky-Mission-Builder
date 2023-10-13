// SPDX-License-Identifier: GPL-3.0-only
/*
 * filepersonalityitemparser.cpp
 *
 * Copyright (c) 2023, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "filepersonalityitemparser.h"

#include <iostream>

#include "common/fileitemparserutils.h"
namespace utils = FileItemParserUtils;

FilePersonalityItemParser::FilePersonalityItemParser(std::vector<std::string> lines)
{
    setLines(lines);
}

json FilePersonalityItemParser::run() {
    std::cout << "Parsing fleet node to JSON" << std::endl;
    std::vector<std::string> tokens;
    std::vector<std::string> lines = getLines();

    json personality;
    for (int i = 0; i < static_cast<int>(lines.size()); i++) {
        // start by tokenizing each line
        tokens = utils::tokenize(lines.at(i));
        std::vector<std::string> nodeLines;

        if (utils::is(tokens.at(0), "personality")) {
            if (lines.size() == 1) {
                // empty node was passed, return the empty object
                return personality;
            }
        }
    }

    return personality;
}

json FilePersonalityItemParser::getData() const {
    json personality;
    return personality;
}
