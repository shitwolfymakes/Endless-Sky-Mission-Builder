// SPDX-License-Identifier: GPL-3.0-only
/*
 * filesubstitutionsitemparser.cpp
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "filesubstitutionsitemparser.h"

FileSubstitutionsItemParser::FileSubstitutionsItemParser(std::vector<std::string> lines)
    : FileItemParser(lines)
{

}

json FileSubstitutionsItemParser::run() {
    std::cout << "Parsing substitutions node to JSON" << std::endl;
    std::vector<std::string> tokens;
    for (int i = 1; i < static_cast<int>(lines.size()); i++) {
        tokens = tokenize(lines.at(i));
        //std::cout << "LINE: " << tokens.at(0) << std::endl;
        if (tokens.size() != 2) {
            std::cout << "\tERROR: INCORRECT NUMBER OF TOKENS FOUND ON LINE: " << lines.at(i) << std::endl;
        }

        i = parseSubstitution(&lines, i);
    }
    //std::cout << "Substitution data: " << substitutions.dump(4) << std::endl;
    return substitutions;
}

int FileSubstitutionsItemParser::parseSubstitution(std::vector<std::string> *nodeLines, int startingIndex) {
    std::cout << "Parsing substitution: " << lines.at(startingIndex) << std::endl;
    std::vector<std::string> lines = *nodeLines;
    int index = startingIndex;
    json substitution; // create a json obect to store trigger data, pass ref to this when necessary


    std::vector<std::string> tokens = tokenize(lines.at(index));
    substitution["key"] = tokens.at(0);
    substitution["replacement_text"] = tokens.at(1);

    // check if next line exists
    try {
        getIndentLevel(lines.at(index + 1));
    }  catch (const std::out_of_range& ex) {
        substitutions.emplace_back(substitution);
        return index;
    }

    int cur = getIndentLevel(lines.at(index));
    int nxt = getIndentLevel(lines.at(index + 1));
    while (true) {
        if (nxt <= cur) {
            break;
        }
        index++;

        std::string conditionSet = lines.at(index);
        boost::trim(conditionSet);
        std::cout << "\tFound condition set: " << conditionSet << std::endl;
        substitution["condition_sets"].emplace_back(conditionSet);

        // handle getting the depth of the next line
        try {
            nxt = getIndentLevel(lines.at(index + 1));
        }  catch (const std::out_of_range& ex) {
            break;
        }
    }
    substitutions.emplace_back(substitution);

    return index;
}

json FileSubstitutionsItemParser::get_data() const {
    return substitutions;
}
