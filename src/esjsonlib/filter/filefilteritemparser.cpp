// SPDX-License-Identifier: GPL-3.0-only
/*
 * filefilteritemparser.cpp
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "filefilteritemparser.h"

#include <iostream>

#include <boost/algorithm/string.hpp>

#include "common/fileitemparserutils.h"
namespace utils = FileItemParserUtils;

FileFilterItemParser::FileFilterItemParser(std::vector<std::string> lines) {
    setLines(lines);
}

json FileFilterItemParser::run() {
    std::cout << "Parsing filter node to JSON" << std::endl;
    std::vector<std::string> tokens;
    std::vector<std::string> lines = getLines();
    for (int i = 1; i < static_cast<int>(lines.size()); i++) {
        tokens = utils::tokenize(lines.at(i));

        std::vector<std::string> nodeLines;
        i = utils::collectNodeLines(&lines, i, &nodeLines);
        if (tokens.size() == 1 && isModifier(tokens.at(0))) {
            // parse recursively
            std::cout << "\tParsing recursive node: " << tokens.at(0) << std::endl;
            FileFilterItemParser p = FileFilterItemParser(nodeLines);
            json child_filter = p.run();

            // add parsed filiter to the appropriate list of child filters
            if (utils::is(tokens.at(0), "not")) {
                filter["not_filters"].emplace_back(child_filter);
            } else if (utils::is(tokens.at(0), "neighbor")) {
                filter["neighbor_filters"].emplace_back(child_filter);
            }
        } else {
            // parse the constriants
            parseFilter(&nodeLines);
        }
    }
    std::cout << "Filter data: " << filter.dump(4) << std::endl;
    return filter;
}

void FileFilterItemParser::parseFilter(std::vector<std::string> *lines) {
    // Take in the lines that make up a filter - be it normal, a not child node, or a neighbor child node
    // for each line:
    //  - calculate if there is a modifier
    //  - determine the type of constraint
    //  - collect the line(s) in the constraint, if multiple is an option
    //  - pass the collected lines to a function that parses that specific constraint
    for (int i = 0; i < lines->size(); i++) {
        std::vector<std::string> tokens = utils::tokenize(lines->at(i));
        std::string modifier = "";
        int j = 0;
        if (isModifier(tokens.at(0))) {
            modifier = tokens.at(0);
            j += 1;
        }
        const std::string key = tokens.at(j);

        std::vector<std::string> nodeLines;
        i = utils::collectNodeLines(lines, i, &nodeLines);
        if (utils::is(key, "planet")) {
            parsePlanets(&nodeLines, modifier);
        } else if (utils::is(key, "system")) {
            parseSystems(&nodeLines, modifier);
        } else if (utils::is(key, "government")) {
            parseGovernments(&nodeLines, modifier);
        } else if (utils::is(key, "attributes")) {
            parseAttributes(&nodeLines, modifier);
        } else if (utils::is(key, "outfits")) {
            parseOutfits(&nodeLines, modifier);
        } else if (utils::is(key, "category")) {
            parseCategories(&nodeLines, modifier);
        } else if (utils::is(key, "near")) {
            parseNear(nodeLines, modifier);
        } else if (utils::is(key, "distance")) {
            parseDistance(nodeLines, modifier);
        }
    }
}

void FileFilterItemParser::parsePlanets(std::vector<std::string> *lines, std::string modifier) {
    // The list of names can either be all on one line, or split between
    // multiple lines if it is particularly long; the subsequent lines
    // must be indented so that they are "children"
    std::string constraint = "planet";
    std::cout << "\tFound " << constraint << ": " << boost::join(*lines, " ") << std::endl;
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

void FileFilterItemParser::parseSystems(std::vector<std::string> *lines, std::string modifier) {
    // The list of names can either be all on one line, or split between
    // multiple lines if it is particularly long; the subsequent lines
    // must be indented so that they are "children"
    std::string constraint = "system";
    std::cout << "\tFound " << constraint << ": " << boost::join(*lines, " ") << std::endl;
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

void FileFilterItemParser::parseGovernments(std::vector<std::string> *lines, std::string modifier) {
    // The list of names can either be all on one line, or split between
    // multiple lines if it is particularly long; the subsequent lines
    // must be indented so that they are "children"
    std::string constraint = "government";
    std::cout << "\tFound " << constraint << ": " << boost::join(*lines, " ") << std::endl;
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

void FileFilterItemParser::parseAttributes(std::vector<std::string> *lines, std::string modifier) {
    // Each instance of this constraint must be stored as a separate list of options
    std::string group      = "attribute_set";
    std::string constraint = "attributes";
    std::cout << "\tFound " << constraint << ": " << boost::join(*lines, " ") << std::endl;
    json constraint_list;
    for (int i = 0; i < lines->size(); i++) {
        std::vector<std::string> tokens = utils::tokenize(lines->at(i));
        int index = 0;
        if (i == 0) { index = 1 + isModifier(modifier); }

        // store all name tokens
        for (int j = index; j < tokens.size(); j++) {
            constraint_list[constraint].emplace_back(tokens.at(j));
        }
    }

    if (modifier.compare("") == 0) {
        filter[group].emplace_back(constraint_list);
    } else {
        filter[modifier][group].emplace_back(constraint_list);
    }
}

void FileFilterItemParser::parseOutfits(std::vector<std::string> *lines, std::string modifier) {
    // Each instance of this constraint must be stored as a separate list of options
    std::string group      = "outfit_set";
    std::string constraint = "outfits";
    std::cout << "\tFound " << constraint << ": " << boost::join(*lines, " ") << std::endl;
    json constraint_list;
    for (int i = 0; i < lines->size(); i++) {
        std::vector<std::string> tokens = utils::tokenize(lines->at(i));
        int index = 0;
        if (i == 0) { index = 1 + isModifier(modifier); }

        // store all name tokens
        for (int j = index; j < tokens.size(); j++) {
            constraint_list[constraint].emplace_back(tokens.at(j));
        }
    }

    if (modifier.compare("") == 0) {
        filter[group].emplace_back(constraint_list);
    } else {
        filter[modifier][group].emplace_back(constraint_list);
    }
}

void FileFilterItemParser::parseCategories(std::vector<std::string> *lines, std::string modifier) {
    // The list of names can either be all on one line, or split between
    // multiple lines if it is particularly long; the subsequent lines
    // must be indented so that they are "children"
    std::string constraint = "category";
    std::cout << "\tFound " << constraint << ": " << boost::join(*lines, " ") << std::endl;
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

json FileFilterItemParser::parseDistanceCalculationSettings(std::vector<std::string> lines) {
    std::cout << "\t\tparsing distance calculation settings" << std::endl;
    json settings;
    std::vector<std::string> wormhole_opts = {"all wormholes", "only restricted wormholes", "no wormholes"};

    // set flags that appear only if true to false to ensure they don't persist
    settings["assumes_jump_drive"] = false;
    for (int i = 1; i < lines.size(); i++) {
        std::vector<std::string> tokens = utils::tokenize(lines.at(i));
        std::cout << "\t\t\ttokens: " << boost::join(tokens, ", ")  << std::endl;
        if (tokens.at(0).compare("distance calculation settings") == 0) {
            continue;
        } else if (utils::isOneOf(tokens.at(0), wormhole_opts) == true) {
            settings["wormholes_used"] = tokens.at(0);
        } else if (tokens.at(0).compare("assumes jump drive") == 0) {
            settings["assumes_jump_drive"] = true;
        }
    }
    return settings;
}

void FileFilterItemParser::parseNear(std::vector<std::string> lines, std::string modifier) {
    std::string constraint = "near";
    std::cout << "\tFound " << constraint << "node: \n" << boost::join(lines, "\n") << std::endl;
    std::vector<std::string> tokens = utils::tokenize(lines.at(0));

    // shift index based on presence of modifiers
    int i = 0 + isModifier(modifier);

    json constraint_data;
    // store the system name from tokens[1], or 2 if isModifier returns true
    constraint_data["system"] = tokens.at(1 + i);

    if (tokens.size() == 3 + i) {
        // if the line contains only one optional token
        constraint_data["max"] = std::stoi(tokens.at(2 + i));
    } else if (tokens.size() == 4 + i) {
        // if the line contains both optional tokens
        constraint_data["min"] = std::stoi(tokens.at(2 + i));
        constraint_data["max"] = std::stoi(tokens.at(3 + i));
    }

    // handle any calculation settings
    if (lines.size() >= 2) {
        constraint_data["distance_calculation_settings"] = parseDistanceCalculationSettings(lines);
    }

    // store based on modifier
    if (modifier.compare("") == 0) {
        filter[constraint] = constraint_data;
    } else {
        filter[modifier][constraint] = constraint_data;
    }
}

void FileFilterItemParser::parseDistance(std::vector<std::string> lines, std::string modifier) {
    // This node is a single line, containing multiple tokens, some potentially optional
    std::string constraint = "distance";
    std::cout << "\tFound " << constraint << "node: \n" << boost::join(lines, "\n") << std::endl;
    std::vector<std::string> tokens = utils::tokenize(lines.at(0));

    // shift index based on presence of modifiers
    int i = 0 + isModifier(modifier);

    json constraint_data;
    if (tokens.size() == 2 + i) {
        // if the line contains only one optional token
        constraint_data["max"] = std::stoi(tokens.at(1 + i));
    } else if (tokens.size() == 3 + i) {
        // if the line contains both optional tokens
        constraint_data["min"] = std::stoi(tokens.at(1 + i));
        constraint_data["max"] = std::stoi(tokens.at(2 + i));
    }

    // handle any calculation settings
    if (lines.size() >= 2) {
        constraint_data["distance_calculation_settings"] = parseDistanceCalculationSettings(lines);
    }

    // store based on modifier
    if (modifier.compare("") == 0) {
        filter[constraint] = constraint_data;
    } else {
        filter[modifier][constraint] = constraint_data;
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
