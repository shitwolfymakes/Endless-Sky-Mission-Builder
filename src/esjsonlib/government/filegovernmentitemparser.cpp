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
namespace utils = FileItemParserUtils;

FileGovernmentItemParser::FileGovernmentItemParser(std::vector<std::string> lines) {
    setLines(lines);
}

json FileGovernmentItemParser::run() {
    std::cout << "Parsing government node to JSON" << std::endl;
    std::vector<std::string> tokens;

    // set flags that appear only if true to false to ensure they don't persist
    govt["provoked_on_scan"] = false;
    govt["send_untranslated_hails"] = false;
    std::vector<std::string> lines = getLines();
    for (int i = 0; i < static_cast<int>(lines.size()); i++) {
        // start by tokenizing each line
        tokens = utils::tokenize(lines.at(i));
        std::vector<std::string> nodeLines;

        if (tokens.empty()) {
            std::cout << "\tERROR: NO TOKENS FOUND ON LINE: " << lines.at(i) << std::endl;
        } else if (tokens.size() == 1) {
            if (utils::is(tokens.at(0), "provoked on scan")) {
                govt["provoked_on_scan"] = true;
            } else if (utils::is(tokens.at(0), "send untranslated hails")) {
                govt["send_untranslated_hails"] = true;
            }
        } else if (tokens.size() == 2) {
            if (utils::is(tokens.at(0), "government")) {
                std::cout << "\tGovernment ID is: " << tokens.at(1) << std::endl;
                govt["id"] = tokens.at(1);
            }
            else if (utils::is(tokens.at(0), "display name")) {
                std::cout << "\tGovernment display name is: " << tokens.at(1) << std::endl;
                govt["display_name"] = tokens.at(1);
            }
            else if (utils::is(tokens.at(0), "swizzle")) {
                parseSwizzle(tokens.at(1));
            } else if (utils::is(tokens.at(0), "color")) {
                parseColor(tokens);
            } else if (utils::is(tokens.at(0), "player reputation") == 0) {
                parsePlayerRep(tokens.at(1));
            } else if (utils::is(tokens.at(0), "reputation")) {
                i = utils::collectNodeLines(&nodeLines, i, &nodeLines);
                parseReputation(nodeLines);
            } else if (utils::is(tokens.at(0), "crew attack")) {
                parseCrewAttack(tokens.at(1));
            } else if (utils::is(tokens.at(0), "crew defense")) {
                parseCrewDefense(tokens.at(1));
            } else if (utils::is(tokens.at(0), "attitude toward")) {
                i = utils::collectNodeLines(&nodeLines, i, &nodeLines);
                parseAttitudeToward(nodeLines);
            } else if (utils::is(tokens.at(0), "penalty for")) {
                i = utils::collectNodeLines(&nodeLines, i, &nodeLines);
                parsePenaltyFor(nodeLines);
            } else if (utils::is(tokens.at(0), "foreign penalties for")) {
                i = utils::collectNodeLines(&nodeLines, i, &nodeLines);
                parseForeignPenaltiesFor(nodeLines);
            } else if (utils::is(tokens.at(0), "custom penalties for")) {
                i = utils::collectNodeLines(&nodeLines, i, &nodeLines);
                parseCustomPenaltiesFor(nodeLines);
            } else if (utils::is(tokens.at(0), "bribe")) {
                parseBribe(tokens.at(1));
            } else if (utils::is(tokens.at(0), "fine")) {
                parseFine(tokens.at(1));
            } else if (utils::is(tokens.at(0), "death sentence")) {
                parseDeathSentence(tokens.at(1));
            } else if (utils::is(tokens.at(0), "friendly hail")) {
                parseFriendlyHail(tokens.at(1));
            } else if (utils::is(tokens.at(0), "friendly disabled hail")) {
                parseFriendlyDisabledHail(tokens.at(1));
            } else if (utils::is(tokens.at(0), "hostile hail")) {
                parseHostileHail(tokens.at(1));
            } else if (utils::is(tokens.at(0), "hostile disabled hail")) {
                parseHostileDisabledHail(tokens.at(1));
            } else if (utils::is(tokens.at(0), "language")) {
                parseHostileDisabledHail(tokens.at(1));
            } else if (utils::is(tokens.at(0), "enforces")) {
                i = utils::collectNodeLines(&nodeLines, i, &nodeLines);
                parseCustomPenaltiesFor(nodeLines);
            }
        }
    }
    return govt;
}
/*
void FileGovernmentItemParser::parseId(std::string token) {
    std::cout << "\tGovernment ID is: " << token << std::endl;
    govt["id"] = token;
}

void FileGovernmentItemParser::parseDisplayName(std::string token) {
    std::cout << "\tGovernment display name is: " << token << std::endl;
    govt["display_name"] = token;
}
*/
void FileGovernmentItemParser::parseSwizzle(std::string token) {
    std::cout << "\tGovernment swizzle is: " << token << std::endl;
    govt["swizzle"] = std::stoi(token);
}

void FileGovernmentItemParser::parseColor(std::vector<std::string> tokens) {
    std::cout << "\tGovernment color is: " << boost::join(tokens, " ") << std::endl;
    if (tokens.size() == 4) {
        govt["color"]["R"] = std::stod(tokens.at(1));
        govt["color"]["G"] = std::stod(tokens.at(2));
        govt["color"]["B"] = std::stod(tokens.at(3));
    } else {
        govt["color"] = tokens.at(1);
    }
}

void FileGovernmentItemParser::parsePlayerRep(std::string token) {
    std::cout << "\tGovernment player reputation is: " << token << std::endl;
    govt["player_reputation"] = std::stod(token);
}

void FileGovernmentItemParser::parseReputation(std::vector<std::string> lines) {
    std::cout << "\tGovernment reputation is: \n" << boost::join(lines, "\n") << std::endl;

    std::vector<std::string> tokens = utils::tokenize(lines.at(1));
    govt["reputation"]["player_reputation"] = std::stod(tokens.at(1));

    tokens = utils::tokenize(lines.at(2));
    govt["reputation"]["min"] = std::stod(tokens.at(1));

    tokens = utils::tokenize(lines.at(3));
    govt["reputation"]["max"] = std::stod(tokens.at(1));
}

void FileGovernmentItemParser::parseCrewAttack(std::string token) {
    std::cout << "\tGovernment crew attack is: " << token << std::endl;
    govt["crew_attack"] = std::stod(token);
}

void FileGovernmentItemParser::parseCrewDefense(std::string token) {
    std::cout << "\tGovernment crew defnse is: " << token << std::endl;
    govt["crew_defense"] = std::stod(token);
}

void FileGovernmentItemParser::parseAttitudeToward(std::vector<std::string> lines) {
    std::cout << "\tGovernment attitude towards is: \n" << boost::join(lines, "\n") << std::endl;

    for (int i = 1; i < static_cast<int>(lines.size()); i++) {
        std::vector<std::string> tokens = utils::tokenize(lines.at(i));
        json attitude;
        attitude["government"] = tokens.at(0);
        attitude["rep-modifier"] = std::stod(tokens.at(1));
        govt["attitude_toward"].emplace_back(attitude);
    }
}

json FileGovernmentItemParser::parseActionsAndModifiers(std::vector<std::string> lines) const {
    json list;
    for (int i = 1; i < static_cast<int>(lines.size()); i++) {
        std::vector<std::string> tokens = utils::tokenize(lines.at(i));

        json penalty;
        penalty["action"] = tokens.at(0);
        penalty["rep-modifier"] = std::stod(tokens.at(1));
        list.emplace_back(penalty);
    }
    return list;
}

void FileGovernmentItemParser::parsePenaltyFor(std::vector<std::string> lines) {
    std::cout << "\tGovernment penalty for is: \n" << boost::join(lines, "\n") << std::endl;
    govt["penalty_for"] = parseActionsAndModifiers(lines);
}

void FileGovernmentItemParser::parseForeignPenaltiesFor(std::vector<std::string> lines) {
    std::cout << "\tGovernment foreign penalties for is: \n" << boost::join(lines, "\n") << std::endl;

    for (int i = 1; i < static_cast<int>(lines.size()); i++) {
        std::vector<std::string> tokens = utils::tokenize(lines.at(i));
        govt["foreign_penalties_for"].emplace_back(tokens.at(0));
    }
}

void FileGovernmentItemParser::parseCustomPenaltiesFor(std::vector<std::string> lines) {
    std::cout << "\tGovernment custom penalties for is: \n" << boost::join(lines, "\n") << std::endl;

    for (int i = 1; i < static_cast<int>(lines.size()); i++) {
        std::vector<std::string> tokens = utils::tokenize(lines.at(i));
        std::string govt_name = tokens.at(0);
        std::vector<std::string> nodeLines;
        json govt_penalties;

        i = utils::collectNodeLines(&lines, i, &nodeLines);
        govt_penalties["government"] = govt_name;
        govt_penalties["penalties"] = parseActionsAndModifiers(nodeLines);
        govt["custom_penalties_for"].emplace_back(govt_penalties);
    }
}

void FileGovernmentItemParser::parseBribe(std::string token) {
    std::cout << "\tGovernment bribe is: " << token << std::endl;
    govt["bribe"] = std::stod(token);
}

void FileGovernmentItemParser::parseFine(std::string token) {
    std::cout << "\tGovernment fine is: " << token << std::endl;
    govt["fine"] = std::stod(token);
}

void FileGovernmentItemParser::parseDeathSentence(std::string token) {
    std::cout << "\tGovernment death sentence is: " << token << std::endl;
    govt["death_sentence"] = token;
}

void FileGovernmentItemParser::parseFriendlyHail(std::string token) {
    std::cout << "\tGovernment friendly hail is: " << token << std::endl;
    govt["friendly_hail"] = token;
}

void FileGovernmentItemParser::parseFriendlyDisabledHail(std::string token) {
    std::cout << "\tGovernment friendly disabled hail is: " << token << std::endl;
    govt["friendly_disabled_hail"] = token;
}

void FileGovernmentItemParser::parseHostileHail(std::string token) {
    std::cout << "\tGovernment hostile hail is: " << token << std::endl;
    govt["hostile_hail"] = token;
}

void FileGovernmentItemParser::parseHostileDisabledHail(std::string token) {
    std::cout << "\tGovernment hostile disabled hail is: " << token << std::endl;
    govt["hostile_disabled_hail"] = token;
}

void FileGovernmentItemParser::parseLanguage(std::string token) {
    std::cout << "\tGovernment language is: " << token << std::endl;
    govt["language"] = token;
}

void FileGovernmentItemParser::parseRaid(std::vector<std::string> tokens) {
    std::cout << "\tGovernment raid is: " << boost::join(tokens, " ") << std::endl;
    json raid;
    raid["fleet"] = tokens.at(1);
    if (tokens.size() >= 3) {
        raid["min-attraction"] = std::stod(tokens.at(2));
        if (tokens.size() == 4) {
            raid["max-attraction"] = std::stod(tokens.at(3));
        }
    }
    govt["raid"] = raid;
}

void FileGovernmentItemParser::parseEnforces(std::vector<std::string>) {

}

json FileGovernmentItemParser::getData() const {
    return govt;
}
