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
        std::vector<std::string> nodeLines;
        tokens = utils::tokenize(lines.at(i));
        //std::cout << "LINE: " << tokens.at(0) << std::endl;

        if (isModifier(tokens.at(0))) {
            // if not or neighbor
            if (tokens.size() == 1) {
                // parse recursively
                i = utils::collectNodeLines(&lines, i, &nodeLines);
                FileFilterItemParser p = FileFilterItemParser(nodeLines);
                json f;
                f = p.run();

                // add parsed json to list
                if (tokens.at(0).compare("not") == 0) {
                    filter["not_nodes"].emplace_back(f);
                } else if (tokens.at(0).compare("neighbor") == 0) {
                    filter["neighbor_nodes"].emplace_back(f);
                }
            } else {
                // save constraint to the list of nots or neighbors
                // TODO: collectNodeLines and pass to ParseFilter
                //i = utils::collectNodeLines(&lines, i, &nodeLines);
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
        //parsePlanets(&tokens, i, modifier);
    } else if (key.compare("system") == 0) {
        parseSystems(&tokens, i, modifier);
    }
}

void FileFilterItemParser::parsePlanets(std::vector<std::string> *lines, std::string modifier) {
    // The list of names can either be all on one line, or split between
    // multiple lines if it is particularly long; the subsequent lines
    // must be indented so that they are "children"
    std::string constraint = "planet";

    for (int i = 0; i < lines->size(); i++) {
        std::vector<std::string> tokens = utils::tokenize(lines->at(i));
        int index = 0;
        if (i == 0) { index = 1 + isModifier(modifier); }

        // store all name tokens
        for (int j = index; j < tokens.size(); j++) {
            if (modifier.compare("") == 0) {
                filter[constraint].emplace_back(tokens.at(j));
            } else {
                filter[modifier][constraint].emplace_back(tokens.at(j));
            }
        }
    }
}

void FileFilterItemParser::parseSystems(std::vector<std::string> *tokens, int index, std::string modifier) {
    // TODO: refactor to combine into one list of all discovered options
    // The list of names can either be all on one line, or split between
    // multiple lines if it is particularly long; the subsequent lines
    // must be indented so that they are "children"
    std::string group      = "systems";
    std::string constraint = "system";
    json constraint_list;
    for (int i = index; i < tokens->size(); i++) {
        constraint_list[constraint].emplace_back(tokens->at(i));
    }

    if (modifier.compare("") == 0) {
        filter[group].emplace_back(constraint_list);
    } else {
        filter[modifier][group].emplace_back(constraint_list);
    }
}

void FileFilterItemParser::parseGovernments(std::vector<std::string> *tokens, int index, std::string modifier) {
    // TODO: refactor to combine into one list of all discovered options
    // The list of names can either be all on one line, or split between
    // multiple lines if it is particularly long; the subsequent lines
    // must be indented so that they are "children"
    std::string group      = "governments";
    std::string constraint = "government";
    json constraint_list;
    for (int i = index; i < tokens->size(); i++) {
        constraint_list[constraint].emplace_back(tokens->at(i));
    }

    if (modifier.compare("") == 0) {
        filter[group].emplace_back(constraint_list);
    } else {
        filter[modifier][group].emplace_back(constraint_list);
    }
}

void FileFilterItemParser::parseAttributes(std::vector<std::string> *tokens, int index, std::string modifier) {
    // Each instance of this constraint must be stored as a separate list of options
    std::string group      = "attributes";
    std::string constraint = "attributes";
    json constraint_list;
    for (int i = index; i < tokens->size(); i++) {
        constraint_list[constraint].emplace_back(tokens->at(i));
    }

    if (modifier.compare("") == 0) {
        filter[group].emplace_back(constraint_list);
    } else {
        filter[modifier][group].emplace_back(constraint_list);
    }
}

void FileFilterItemParser::parseOutfits(std::vector<std::string> *tokens, int index, std::string modifier) {
    // Each instance of this constraint must be stored as a separate list of options
    std::string group      = "outfits";
    std::string constraint = "outfits";
    json constraint_list;
    for (int i = index; i < tokens->size(); i++) {
        constraint_list[constraint].emplace_back(tokens->at(i));
    }

    if (modifier.compare("") == 0) {
        filter[group].emplace_back(constraint_list);
    } else {
        filter[modifier][group].emplace_back(constraint_list);
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
