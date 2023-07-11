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
        }
        else if (utils::is(tokens.at(0), "send untranslated hails")) {
            govt["send_untranslated_hails"] = true;
        }
        else if (utils::is(tokens.at(0), "government")) {
            std::cout << "\tGovernment ID is: " << tokens.at(1) << std::endl;
            govt["id"] = tokens.at(1);
        }
        else if (utils::is(tokens.at(0), "display name")) {
            std::cout << "\tGovernment display name is: " << tokens.at(1) << std::endl;
            govt["display_name"] = tokens.at(1);
        }
        else if (utils::is(tokens.at(0), "swizzle")) {
            std::cout << "\tGovernment swizzle is: " << tokens.at(1) << std::endl;
            govt["swizzle"] = std::stoi(tokens.at(1));
        }
        else if (utils::is(tokens.at(0), "color")) {
            std::cout << "\tGovernment color is: " << boost::join(tokens, " ") << std::endl;
            if (tokens.size() == 4) {
                govt["color"]["R"] = std::stod(tokens.at(1));
                govt["color"]["G"] = std::stod(tokens.at(2));
                govt["color"]["B"] = std::stod(tokens.at(3));
            } else {
                govt["color"] = tokens.at(1);
            }
        }
        else if (utils::is(tokens.at(0), "player reputation")) {
            std::cout << "\tGovernment player reputation is: " << tokens.at(1) << std::endl;
            govt["player_reputation"] = std::stod(tokens.at(1));
        }
        else if (utils::is(tokens.at(0), "reputation")) {
            i = utils::collectNodeLines(&lines, i, &nodeLines);
            std::cout << "\tGovernment reputation is: \n" << boost::join(nodeLines, "") << std::endl;

            std::vector<std::string> rep_tokens = utils::tokenize(nodeLines.at(1));
            govt["reputation"]["player_reputation"] = std::stod(rep_tokens.at(1));

            rep_tokens = utils::tokenize(nodeLines.at(2));
            govt["reputation"]["min"] = std::stod(rep_tokens.at(1));

            rep_tokens = utils::tokenize(nodeLines.at(3));
            govt["reputation"]["max"] = std::stod(rep_tokens.at(1));
        }
        else if (utils::is(tokens.at(0), "crew attack")) {
            std::cout << "\tGovernment crew attack is: " << tokens.at(1) << std::endl;
            govt["crew_attack"] = std::stod(tokens.at(1));
        }
        else if (utils::is(tokens.at(0), "crew defense")) {
            std::cout << "\tGovernment crew defnse is: " << tokens.at(1) << std::endl;
            govt["crew_defense"] = std::stod(tokens.at(1));
        }
        else if (utils::is(tokens.at(0), "attitude toward")) {
            i = utils::collectNodeLines(&lines, i, &nodeLines);
            std::cout << "\tGovernment attitude towards is: \n" << boost::join(nodeLines, "") << std::endl;

            for (int j = 1; j < static_cast<int>(nodeLines.size()); j++) {
                std::vector<std::string> attitude_tokens = utils::tokenize(nodeLines.at(j));
                json attitude;
                attitude["government"] = attitude_tokens.at(0);
                attitude["rep-modifier"] = std::stod(attitude_tokens.at(1));
                govt["attitude_toward"].emplace_back(attitude);
            }
        }
        else if (utils::is(tokens.at(0), "penalty for")) {
            i = utils::collectNodeLines(&lines, i, &nodeLines);
            std::cout << "\tGovernment penalty for is: \n" << boost::join(nodeLines, "") << std::endl;
            govt["penalty_for"] = parseActionsAndModifiers(nodeLines);
        }
        else if (utils::is(tokens.at(0), "foreign penalties for")) {
            i = utils::collectNodeLines(&lines, i, &nodeLines);
            std::cout << "\tGovernment foreign penalties for is: \n" << boost::join(nodeLines, "") << std::endl;

            for (int j = 1; j < static_cast<int>(nodeLines.size()); j++) {
                std::vector<std::string> penalties_tokens = utils::tokenize(nodeLines.at(j));
                govt["foreign_penalties_for"].emplace_back(penalties_tokens.at(0));
            }
        }
        else if (utils::is(tokens.at(0), "custom penalties for")) {
            i = utils::collectNodeLines(&lines, i, &nodeLines);
            govt["custom_penalties_for"] = parseCustomPenaltiesFor(nodeLines);
        }
        else if (utils::is(tokens.at(0), "provoked on scan")) {
            govt["provoked_on_scan"] = true;
        }
        else if (utils::is(tokens.at(0), "bribe")) {
            std::cout << "\tGovernment bribe is: " << tokens.at(1) << std::endl;
            govt["bribe"] = std::stod(tokens.at(1));
        }
        else if (utils::is(tokens.at(0), "fine")) {
            std::cout << "\tGovernment fine is: " << tokens.at(1) << std::endl;
            govt["fine"] = std::stod(tokens.at(1));
        }
        else if (utils::is(tokens.at(0), "death sentence")) {
            std::cout << "\tGovernment death sentence is: " << tokens.at(1) << std::endl;
            govt["death_sentence"] = tokens.at(1);
        }
        else if (utils::is(tokens.at(0), "provoked on scan")) {
            govt["provoked_on_scan"] = true;
        }
        else if (utils::is(tokens.at(0), "friendly hail")) {
            std::cout << "\tGovernment friendly hail is: " << tokens.at(1) << std::endl;
            govt["friendly_hail"] = tokens.at(1);
        }
        else if (utils::is(tokens.at(0), "friendly disabled hail")) {
            std::cout << "\tGovernment friendly disabled hail is: " << tokens.at(1) << std::endl;
            govt["friendly_disabled_hail"] = tokens.at(1);
        }
        else if (utils::is(tokens.at(0), "hostile hail")) {
            std::cout << "\tGovernment hostile hail is: " << tokens.at(1) << std::endl;
            govt["hostile_hail"] = tokens.at(1);
        }
        else if (utils::is(tokens.at(0), "hostile disabled hail")) {
            std::cout << "\tGovernment hostile disabled hail is: " << tokens.at(1) << std::endl;
            govt["hostile_disabled_hail"] = tokens.at(1);
        }
        else if (utils::is(tokens.at(0), "language")) {
            std::cout << "\tGovernment language is: " << tokens.at(1) << std::endl;
            govt["language"] = tokens.at(1);
        }
        else if (utils::is(tokens.at(0), "raid")) {
            govt["raid"] = parseRaid(tokens);
        }
        else if (utils::is(tokens.at(0), "enforces")) {
            std::cout << "\tGovernment enforces is: " << lines.at(i) << std::endl;
            i = utils::collectNodeLines(&lines, i, &nodeLines);
            if (nodeLines.size() == 1) {
                // parse without filter
                govt["enforces"].emplace_back("ALL");
            } else {
                // TODO: implement parse with filter
                std::cout << "\t\tNOT IMPLEMENTED YET" << std::endl;
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
*/
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
/*
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
*/
json FileGovernmentItemParser::parseCustomPenaltiesFor(std::vector<std::string> lines) const {
    std::cout << "\tGovernment custom penalties for is: \n" << boost::join(lines, "") << std::endl;
    json custom_penalties_for;
    for (int i = 1; i < static_cast<int>(lines.size()); i++) {
        std::vector<std::string> tokens = utils::tokenize(lines.at(i));
        std::string govt_name = tokens.at(0);
        std::vector<std::string> nodeLines;
        json govt_penalties;

        i = utils::collectNodeLines(&lines, i, &nodeLines);
        govt_penalties["government"] = govt_name;
        govt_penalties["penalties"] = parseActionsAndModifiers(nodeLines);
        custom_penalties_for.emplace_back(govt_penalties);
    }
    return custom_penalties_for;
}
/*
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
*/
json FileGovernmentItemParser::parseRaid(std::vector<std::string> tokens) const {
    std::cout << "\tGovernment raid is: " << boost::join(tokens, " ") << std::endl;
    json raid;
    raid["fleet"] = tokens.at(1);
    if (tokens.size() >= 3) {
        raid["min-attraction"] = std::stod(tokens.at(2));
        if (tokens.size() == 4) {
            raid["max-attraction"] = std::stod(tokens.at(3));
        }
    }
    return raid;
}

void FileGovernmentItemParser::parseEnforces(std::vector<std::string>) {

}

json FileGovernmentItemParser::getData() const {
    return govt;
}
