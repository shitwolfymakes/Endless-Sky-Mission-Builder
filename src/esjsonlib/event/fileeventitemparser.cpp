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
    }
    //std::cout << "Mission data: " << mission.dump(4) << std::endl;
    return event;
}

json FileEventItemParser::getData() const {
    return event;
}
