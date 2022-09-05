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

    std::vector<std::string> tokens = tokenize(lines.at(index));

    // check if next line exists
    try {
        getIndentLevel(lines.at(index + 1));
    }  catch (const std::out_of_range& ex) {
        //substitutions.emplace_back(substitution);
        return index;
    }

    int cur = getIndentLevel(lines.at(index));
    int nxt = getIndentLevel(lines.at(index + 1));
    while (true) {
        if (nxt <= cur) {
            break;
        }
        index++;

        //std::string conditionSet = lines.at(index);
        //boost::trim(conditionSet);
        //std::cout << "\tFound condition set: " << conditionSet << std::endl;
        //substitution["condition_sets"].emplace_back(conditionSet);

        // handle getting the depth of the next line
        try {
            nxt = getIndentLevel(lines.at(index + 1));
        }  catch (const std::out_of_range& ex) {
            break;
        }
    }
    //substitutions.emplace_back(substitution);
    return index;
}

json FilePhraseItemParser::get_data() {
    return phrase;
}
