// SPDX-License-Identifier: GPL-3.0-only
/*
 * filephraseitemparser.cpp
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "filephraseitemparser.h"

FilePhraseItemParser::FilePhraseItemParser(std::vector<std::string> lines)
    : FileItemParser(lines)
{

}

json FilePhraseItemParser::run() {
    std::cout << "Parsing phrase node to JSON" << std::endl;
    std::vector<std::string> tokens;
    for (int i = 1; i < static_cast<int>(lines.size()); i++) {
        tokens = tokenize(lines.at(i));
        std::cout << "LINE: " << tokens.at(0) << std::endl;
        if (tokens.at(0).compare("word") == 0) {
            i = parseWords(&lines, i);
            std::cout << "i is: " << i << std::endl;
        }

    }
    //std::cout << "Phrase data: " << phrase.dump(4) << std::endl;
    return phrase;
}

int FilePhraseItemParser::parseWords(std::vector<std::string> *nodeLines, int startingIndex) {
    std::cout << "Parsing word node" << std::endl;
    std::vector<std::string> lines = *nodeLines;
    int index = startingIndex;
    json word;

    int cur = getIndentLevel(lines.at(index));
    int nxt = getIndentLevel(lines.at(index + 1));
    while (true) {
        if (nxt <= cur) {
            break;
        }
        index++;

        std::vector<std::string> tokens = tokenize(lines.at(index));
        if (tokens.size() == 1) {
            phrase["words"].emplace_back(tokens.at(0));
        } else if (tokens.size() == 2) {
            json weighted_word;
            weighted_word["text"] = tokens.at(0);
            weighted_word["weight"] = std::stoi(tokens.at(0));
        } else {
            std::cout << "\tERROR: INCORRECT NUMBER OF TOKENS FOUND ON LINE: " << lines.at(index) << std::endl;
        }

        // handle getting the depth of the next line
        try {
            nxt = getIndentLevel(lines.at(index + 1));
        }  catch (const std::out_of_range& ex) {
            break;
        }
    }
    return index;
}

json FilePhraseItemParser::get_data() {
    return phrase;
}
