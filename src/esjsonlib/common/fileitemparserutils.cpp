// SPDX-License-Identifier: GPL-3.0-only
/*
 * fileitemparserutils.cpp
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "fileitemparserutils.h"

#include <iostream>

#include <boost/algorithm/string.hpp>
#include <boost/format.hpp>
#include <boost/tokenizer.hpp>

#include "nlohmann/json.hpp"
using json = nlohmann::json;

std::vector<std::string> FileItemParserUtils::tokenize(std::string line) {
    // strip whitespace/tabs from line
    boost::trim(line);
    boost::trim_if(line, boost::is_any_of("\t"));

    std::vector<std::string> tokens;
    std::string token;

    // define the separators
    std::string separator1("");    //dont let quoted arguments escape themselves
    std::string separator2(" ");   //split on spaces
    std::string separator3("`\""); //let it have quoted arguments

    boost::escaped_list_separator<char> els(separator1,separator2,separator3);
    boost::tokenizer<boost::escaped_list_separator<char>> tok(line, els);
    for(boost::tokenizer<boost::escaped_list_separator<char>>::iterator beg=tok.begin(); beg!=tok.end();++beg)
    {
        token = *beg;
        boost::trim(token);
        tokens.push_back(token);
    }
    return tokens;
}

int FileItemParserUtils::getIndentLevel(std::string line) {
    int level = 0;
    for (char c: line) {
        if (c == '\t') {
            level++;
        } else {
            break;
        }
    }
    return level;
}

bool FileItemParserUtils::isOneOf(std::string token, std::vector<std::string> options) {
    for (std::string &option: options) {
        if (token.compare(option) == 0) {
            return true;
        }
    }
    return false;
}

int FileItemParserUtils::collectNodeLines(std::vector<std::string> *lines, int startingIndex, json *nodeLines) {
    int index = startingIndex;
    std::cout << "\tCollecting lines in node: " << lines->at(index) << std::endl;

    // collect the first line in the node
    (*nodeLines).emplace_back(lines->at(index));

    // return early to avoid exception if there is only one line in the node
    if (startingIndex + 1 == lines->size()) { return startingIndex; }

    int cur = getIndentLevel(lines->at(index));
    int nxt = getIndentLevel(lines->at(index + 1));
    while (true) {
        if (nxt <= cur) {
            break;
        }
        index++;

        (*nodeLines).emplace_back(lines->at(index));

        // handle getting the depth of the next line
        try {
            nxt = getIndentLevel(lines->at(index + 1));
        }  catch (const std::out_of_range& ex) {
            break;
        }
    }
    //std::cout << "\tNode Lines: " << nodeLines->dump(4) << std::endl;
    return index;
}

int FileItemParserUtils::collectNodeLines(std::vector<std::string> *lines, int startingIndex, std::vector<std::string> *nodeLines) {
    int index = startingIndex;
    std::cout << "\tCollecting lines in node: " << lines->at(index) << std::endl;

    // collect the first line in the node
    (*nodeLines).emplace_back(lines->at(index));

    // return early to avoid exception if there is only one line in the node
    if (startingIndex + 1 == lines->size()) { return startingIndex; }

    int cur = getIndentLevel(lines->at(index));
    int nxt = getIndentLevel(lines->at(index + 1));
    while (true) {
        if (nxt <= cur) {
            break;
        }
        index++;

        (*nodeLines).emplace_back(lines->at(index));

        // handle getting the depth of the next line
        try {
            nxt = getIndentLevel(lines->at(index + 1));
        }  catch (const std::out_of_range& ex) {
            break;
        }
    }
    //std::cout << "\tNode Lines: " << nodeLines->dump(4) << std::endl;
    return index;
}
