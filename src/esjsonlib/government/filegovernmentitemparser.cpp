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
            parseDisplayName(tokens.at(1));
        } else if (tokens.at(0).compare("swizzle") == 0) {
            parseSwizzle(tokens.at(1));
        } else if (tokens.at(0).compare("color") == 0) {
            parseColor(tokens);
        } else if (tokens.at(0).compare("player reputation") == 0) {
            parsePlayerRep(tokens.at(1));
        } else if (tokens.at(0).compare("reputation") == 0) {
            json nodeLines;
            i = FileItemParserUtils::collectNodeLines(&lines, i, &nodeLines);
            parseReputation(nodeLines);
        } else if (tokens.at(0).compare("crew attack") == 0) {
            parseCrewAttack(tokens.at(1));
        } else if (tokens.at(0).compare("reputation") == 0) {
            json nodeLines;
            i = FileItemParserUtils::collectNodeLines(&lines, i, &nodeLines);
            parseAttitudeToward(nodeLines);
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
    std::cout << "\tGovernment display name is: " << token << std::endl;
    govt["display_name"] = token;
}

void FileGovernmentItemParser::parseSwizzle(std::string token) {
    std::cout << "\tGovernment swizzle is: " << token << std::endl;
    govt["swizzle"] = std::stoi(token);
}

void FileGovernmentItemParser::parseColor(std::vector<std::string> tokens) {
    std::cout << "\tGovernment color is: " << boost::join(tokens, " ") << std::endl;
    if (tokens.size() == 4) {
        govt["color"]["R"] = std::stoi(tokens.at(1));
        govt["color"]["G"] = std::stoi(tokens.at(2));
        govt["color"]["B"] = std::stoi(tokens.at(3));
    } else {
        govt["color"] = tokens.at(1);
    }
}

void FileGovernmentItemParser::parsePlayerRep(std::string token) {
    std::cout << "\tGovernment player reputation is: " << token << std::endl;
    govt["player_reputation"] = std::stoi(token);
}

void FileGovernmentItemParser::parseReputation(std::vector<std::string> lines) {
    std::cout << "\tGovernment reputation is: \n" << boost::join(lines, "\n") << std::endl;

    std::vector<std::string> tokens = utils::tokenize(lines.at(0));
    govt["reputation"]["player_reputation"] = std::stoi(tokens.at(1));

    tokens = utils::tokenize(lines.at(1));
    govt["reputation"]["min"] = std::stoi(tokens.at(1));

    tokens = utils::tokenize(lines.at(2));
    govt["reputation"]["max"] = std::stoi(tokens.at(1));
}

void FileGovernmentItemParser::parseCrewAttack(std::string token) {
    std::cout << "\tGovernment crew attack is: " << token << std::endl;
    govt["crew_attack"] = std::stoi(token);
}

void FileGovernmentItemParser::parseCrewDefense(std::string token) {
    std::cout << "\tGovernment crew defnse is: " << token << std::endl;
    govt["crew_defense"] = std::stoi(token);
}

void FileGovernmentItemParser::parseAttitudeToward(std::vector<std::string> lines) {
    std::cout << "\tGovernment attitude towards is: \n" << boost::join(lines, "\n") << std::endl;

    for (std::string &line : lines) {
        std::vector<std::string> tokens = utils::tokenize(line);
        json attitude;
        attitude["government"] = tokens.at(0);
        attitude["rep-modifier"] = std::stoi(tokens.at(1));
        govt["attitude_toward"].emplace_back(attitude);
    }
}

json FileGovernmentItemParser::getData() const {
    return govt;
}
