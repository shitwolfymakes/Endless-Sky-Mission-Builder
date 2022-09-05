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
    for (int i = 0; i < static_cast<int>(lines.size()); i++) {
        // start by tokenizing each line
        tokens = tokenize(lines.at(i));
        //std::cout << "LINE: " << tokens.at(0) << std::endl;
    }

    //std::cout << "Phrase data: " << phrase.dump(4) << std::endl;
    return phrase;
}

json FilePhraseItemParser::get_data() {
    return phrase;
}
