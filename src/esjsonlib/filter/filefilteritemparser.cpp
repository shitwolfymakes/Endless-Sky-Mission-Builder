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

        if (isModifier(tokens.at(0))) {
            // if not or neighbor
            if (tokens.size() == 1) {
                // parse recursively
                std::vector<std::string> nodeLines;
                i = utils::collectNodeLines(&lines, i, &nodeLines);
                FileFilterItemParser p = FileFilterItemParser(nodeLines);
                json f;
                f = p.run();

                // add parsed json to list
                if (tokens.at(0).compare("not") == 0) {
                    filter["not_nodes"].emplace_back(f);
                } else if (tokens.at(0).compare("neighbor") == 0) {
                    filter["neigbor_nodes"].emplace_back(f);
                }
            } else {
                // save constraint to the list of nots or neighbors
                parseFilter(tokens);
            }
        } else {
            // save constraint to the list
            parseFilter(tokens);
        }
    }
    //std::cout << "Filter data: " << substitutions.dump(4) << std::endl;
    return filter;
}

void FileFilterItemParser::parseFilter(std::vector<std::string> tokens) {
    std::string modifier = "";
    int i = 1;
    if (isModifier(tokens.at(0))) {
        modifier = tokens.at(0);
        i += 1;
    }

    const std::string key = tokens.at(i);
    if (key.compare("planet") == 0) {
        parsePlanets(tokens, i, modifier);
    }
}

void FileFilterItemParser::parsePlanets(std::vector<std::string> tokens, int index, std::string modifier) {
    for (int i = index; i < tokens.size(); i++) {
        if (modifier.compare("") == 0) {
            filter["planets"]["planet"].emplace_back(tokens.at(i));
        } else {
            filter[modifier]["planets"]["planet"].emplace_back(tokens.at(i));
        }
    }
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
