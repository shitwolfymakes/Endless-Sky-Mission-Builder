// SPDX-License-Identifier: GPL-3.0-only
/*
 * fileeventitemparser.cpp
 *
 * Copyright (c) 2023, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "fileeventitemparser.h"

#include <iostream>

#include <boost/algorithm/string.hpp>

#include "common/fileitemparserutils.h"
using utils = FileItemParserUtils;

FileEventItemParser::FileEventItemParser(std::vector<std::string> lines) {
    setLines(lines);
}

json FileEventItemParser::run() {
    std::cout << "Parsing substitutions node to JSON" << std::endl;
    std::vector<std::string> tokens;

    std::vector<std::string> lines = getLines();
    for (int i = 0; i < static_cast<int>(lines.size()); i++) {
        // start by tokenizing each line
        tokens = utils::tokenize(lines.at(i));
        //std::cout << "LINE: " << tokens.at(0) << std::endl;

        if (tokens.size() == 0) {
            std::cout << "\tERROR: NO TOKENS FOUND ON LINE: " << lines.at(i) << std::endl;
        }
        else if (tokens.at(0).compare("date") == 0) {
            parseDate(tokens);
        }
    }
    //std::cout << "Mission data: " << mission.dump(4) << std::endl;
    return event;
}

void FileEventItemParser::parseDate(std::vector<std::string> tokens) {
    std::cout << "\tFound date: " << boost::join(tokens, " ") << std::endl;
    event["date"]["day"] = std::stoi(tokens.at(1));
    event["date"]["month"] = std::stoi(tokens.at(2));
    event["date"]["year"] = std::stoi(tokens.at(3));
}

void FileEventItemParser::parseVisitSystem(std::string token) {
    std::cout << "\tFound visit (system): " << token << std::endl;
    event["visit"].emplace_back(token);
}

void FileEventItemParser::parseUnvisitSystem(std::string token) {
    std::cout << "\tFound unvisit (system): " << token << std::endl;
    event["unvisit"].emplace_back(token);
}

void FileEventItemParser::parseVisitPlanet(std::string token) {
    std::cout << "\tFound visit (planet): " << token << std::endl;
    event["visit planet"].emplace_back(token);
}

void FileEventItemParser::parseUnvisitPlanet(std::string token) {
    std::cout << "\tFound unvisit (planet): " << token << std::endl;
    event["unvisit planet"].emplace_back(token);
}

void FileEventItemParser::parseLink(std::vector<std::string> tokens) {
    std::cout << "\tFound link: " << boost::join(tokens, " ") << std::endl;
    json link;
    link["system"] = tokens.at(1);
    link["other"] = tokens.at(2);
    event["link"].emplace_back(link);
}

void FileEventItemParser::parseUnlink(std::vector<std::string> tokens) {
    std::cout << "\tFound unlink: " << boost::join(tokens, " ") << std::endl;
    json unlink;
    unlink["system"] = tokens.at(1);
    unlink["other"] = tokens.at(2);
    event["unlink"].emplace_back(unlink);
}

json FileEventItemParser::getData() const {
    return event;
}
