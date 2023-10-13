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
                std::cout << "\tPersonality is declaration only" << std::endl;

                return personality;
            }
            for (int i = 1; i < static_cast<int>(tokens.size()); i++) {
                addPersonalityType(&personality, tokens.at(i));
            }
        //} else if (utils::is(tokens.at(0), "confusion")) {
        } else {
            for (std::string &token: tokens) {
                addPersonalityType(&personality, token);
            }
        }
    }

    return personality;
}

void FilePersonalityItemParser::addPersonalityType(json *personality, std::string type) {
    if ((*personality)["types"].contains(type)) {
        std::cout << "\tPersonality type already exists, skipping..." << std::endl;
        return;
    } else {
        std::cout << "\tPersonality type found: " << type << std::endl;
        (*personality)["types"].emplace_back(type);
    }
}

json FilePersonalityItemParser::getData() const {
    json personality;
    return personality;
}
