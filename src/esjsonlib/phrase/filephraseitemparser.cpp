// SPDX-License-Identifier: GPL-3.0-only
/*
 * filephraseitemparser.cpp
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "filephraseitemparser.h"

#include <iostream>

#include "common/fileitemparserutils.h"
namespace utils = FileItemParserUtils;

FilePhraseItemParser::FilePhraseItemParser(std::vector<std::string> lines)
{
    setLines(lines);
}

json FilePhraseItemParser::run() {
    std::cout << "Parsing phrase node to JSON" << std::endl;
    std::vector<std::string> tokens;

    std::vector<std::string> lines = getLines();
    for (int i = 1; i < static_cast<int>(lines.size()); i++) {
        tokens = utils::tokenize(lines.at(i));
        //std::cout << "LINE: " << tokens.at(0) << std::endl;
        if (utils::is(tokens.at(0), "word")) {
            i = parseWords(&lines, i);
        } else if (utils::is(tokens.at(0), "phrase")) {
            i = parseSubPhrase(&lines, i);
        } else if (utils::is(tokens.at(0), "replace")) {
            i = parseReplace(&lines, i);
        } else {
            std::cout << "\tERROR: INCORRECT NUMBER OF TOKENS FOUND ON LINE: " << lines.at(i) << std::endl;
        }
    }
    //std::cout << "Phrase data: " << phrase.dump(4) << std::endl;
    return phrase;
}

int FilePhraseItemParser::parseWords(std::vector<std::string> *nodeLines, int startingIndex) {
    std::cout << "\tParsing word node" << std::endl;
    std::vector<std::string> lines = *nodeLines;
    int index = startingIndex;

    int cur = utils::getIndentLevel(lines.at(index));
    int nxt = utils::getIndentLevel(lines.at(index + 1));
    while (true) {
        if (nxt <= cur) {
            break;
        }
        index++;

        std::vector<std::string> tokens = utils::tokenize(lines.at(index));
        if (tokens.size() == 1) {
            phrase["words"].emplace_back(tokens.at(0));
        } else if (tokens.size() == 2) {
            json weighted_word;
            weighted_word["text"] = tokens.at(0);
            weighted_word["weight"] = std::stoi(tokens.at(1));
            phrase["words_weighted"].emplace_back(weighted_word);
        } else {
            std::cout << "\tERROR: INCORRECT NUMBER OF TOKENS FOUND ON LINE: " << lines.at(index) << std::endl;
        }

        // handle getting the depth of the next line
        try {
            nxt = utils::getIndentLevel(lines.at(index + 1));
        }  catch (const std::out_of_range& ex) {
            break;
        }
    }
    return index;
}

int FilePhraseItemParser::parseSubPhrase(std::vector<std::string> *nodeLines, int startingIndex) {
    std::cout << "\tParsing sub-phrase node" << std::endl;
    std::vector<std::string> lines = *nodeLines;
    int index = startingIndex;

    int cur = utils::getIndentLevel(lines.at(index));
    int nxt = utils::getIndentLevel(lines.at(index + 1));
    while (true) {
        if (nxt <= cur) {
            break;
        }
        index++;

        std::vector<std::string> tokens = utils::tokenize(lines.at(index));
        if (tokens.size() == 1) {
            phrase["phrases"].emplace_back(tokens.at(0));
        } else if (tokens.size() == 2) {
            json weighted_phrase;
            weighted_phrase["phrase"] = tokens.at(0);
            weighted_phrase["weight"] = std::stoi(tokens.at(1));
            phrase["phrases_weighted"].emplace_back(weighted_phrase);
        } else {
            std::cout << "\tERROR: INCORRECT NUMBER OF TOKENS FOUND ON LINE: " << lines.at(index) << std::endl;
        }

        // handle getting the depth of the next line
        try {
            nxt = utils::getIndentLevel(lines.at(index + 1));
        }  catch (const std::out_of_range& ex) {
            break;
        }
    }
    return index;
}

int FilePhraseItemParser::parseReplace(std::vector<std::string> *nodeLines, int startingIndex) {
    std::cout << "\tParsing replace node" << std::endl;
    std::vector<std::string> lines = *nodeLines;
    int index = startingIndex;

    int cur = utils::getIndentLevel(lines.at(index));
    int nxt = utils::getIndentLevel(lines.at(index + 1));
    while (true) {
        if (nxt <= cur) {
            break;
        }
        index++;

        std::vector<std::string> tokens = utils::tokenize(lines.at(index));
        if (tokens.size() != 2) {
            std::cout << "\tERROR: INCORRECT NUMBER OF TOKENS FOUND ON LINE: " << lines.at(index) << std::endl;
        }

        json replace;
        replace["text"] = tokens.at(0);
        replace["replacement"] = tokens.at(1);
        phrase["replace"].emplace_back(replace);

        // handle getting the depth of the next line
        try {
            nxt = utils::getIndentLevel(lines.at(index + 1));
        }  catch (const std::out_of_range& ex) {
            break;
        }
    }
    return index;
}

json FilePhraseItemParser::getData() const {
    return phrase;
}
