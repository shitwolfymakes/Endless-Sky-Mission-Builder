// SPDX-License-Identifier: GPL-3.0-only
/*
 * datafileparser.cpp
 *
 * Copyright (c) 2021, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "datafileparser.h"

#include <iostream>

#include <boost/algorithm/string.hpp>

#include "event/itemevent.h"
#include "government/itemgovernment.h"
#include "mission/itemmission.h"
#include "phrase/itemphrase.h"
#include "ship/itemship.h"
#include "substitutions/itemsubstitutions.h"

DataFileParser::DataFileParser(std::string rawData)
{
    this->rawData = rawData;

    std::vector<std::string> result;
    boost::split(result, rawData, boost::is_any_of("\n"));
    this->lines = result;
}

void DataFileParser::run() {
    std::cout << "Parsing data file..." << std::endl;
    int i = 0;
    for (const std::string &line: lines) {
        // account for whitespace between file items
        if (line == "") {
            i++;
            continue;
        }

        // search for lines starting file items
        if (std::regex_match(line, matchEvent))
        {
            std::cout << "\tEVENT FOUND: " << line << std::endl;
            storeItemForParsing(i, line, Event);
        }
        else if (std::regex_match(line, matchGovernment)) {
            std::cout << "\tGOVERNMENT FOUND: " << line << std::endl;
            storeItemForParsing(i, line, Government);
        }
        else if (std::regex_match(line, matchMission)) {
            std::cout << "\tMISSION FOUND: " << line << std::endl;
            storeItemForParsing(i, line, Mission);
        }
        else if (std::regex_match(line, matchPhrase)) {
            std::cout << "\tPHRASE FOUND: " << line << std::endl;
            storeItemForParsing(i, line, Phrase);
        }
        else if (std::regex_match(line, matchShip)) {
            std::cout << "\tSHIP FOUND: " << line << std::endl;
            storeItemForParsing(i, line, Ship);
        }
        else if (std::regex_match(line, matchSubstitutions)) {
            std::cout << "\tSUBSTITUTION FOUND: " << line << std::endl;
            storeItemForParsing(i, line, Substitutions);
        }

        i++;
    }

    for (const auto &item: fileItems) {
        item->printLines();
    }

    // loop through fileItems, calling the parser for each one
    for (const auto &item: fileItems) {
        jsonItems.emplace_back(item->parse());
    }
}

void DataFileParser::storeItemForParsing(int i, std::string line, ItemType itemType) {
    FileItem *fileItem;
    switch (itemType) {
        case Event :
            fileItem = new ItemEvent();
            break;
        case Government :
            fileItem = new ItemGovernment();
            break;
        case Mission :
            fileItem = new ItemMission();
            break;
        case Phrase :
            fileItem = new ItemPhrase();
            break;
        case Ship :
            fileItem = new ItemShip();
            break;
        case Substitutions :
            fileItem = new ItemSubstitutions();
            break;
    }
    fileItem->appendLine(line);

    // safer to cast i to size_t as the loop calling this only increments,
    // whereas the mission file could in theory have more than MAX_INT
    // number of lines
    i += 1;
    for (size_t j = i; j < lines.size(); j++) {
        const std::string line = lines.at(j);
        if (isFileItemStartLine(line)) {
            // check if current line is the start of a new FileItem
            // add the fileItem to the list of FileItems
            fileItems.push_back(std::unique_ptr<FileItem>(fileItem));
            return;
        } else if (line == "") {
            // if the current line is blank
            // add the fileItem to the list of FileItems
            fileItems.push_back(std::unique_ptr<FileItem>(fileItem));
            return;
        } else {
            fileItem->appendLine(line);
        }
    }
}

void DataFileParser::printRawData() const {
    std::cout << "BEGIN RAW DATA" << std::endl;
    for(const std::string &line: lines){
        std::cout << line << std::endl;
    }
    std::cout << "END RAW DATA" << std::endl;
}

bool DataFileParser::isFileItemStartLine(std::string line) const {
    // search for lines starting file items
    if (std::regex_match(line, matchEvent)) {
        return true;
    } else if (std::regex_match(line, matchGovernment)) {
        return true;
    } else if (std::regex_match(line, matchMission)) {
        return true;
    } else if (std::regex_match(line, matchPhrase)) {
        return true;
    } else if (std::regex_match(line, matchShip)) {
        return true;
    } else if (std::regex_match(line, matchSubstitutions)) {
        return true;
    }
    return false;
}

json DataFileParser::getJsonItems() const {
    return jsonItems;
}
