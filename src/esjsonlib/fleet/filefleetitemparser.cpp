// SPDX-License-Identifier: GPL-3.0-only
/*
 * filefleetitemparser.cpp
 *
 * Copyright (c) 2023, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "filefleetitemparser.h"

#include <iostream>

#include <boost/algorithm/string.hpp>

#include "common/fileitemparserutils.h"
namespace utils = FileItemParserUtils;

FileFleetItemParser::FileFleetItemParser(std::vector<std::string> lines) {
    setLines(lines);
}

json FileFleetItemParser::run() {
    std::cout << "Parsing fleet node to JSON" << std::endl;
    std::vector<std::string> tokens;
    std::vector<std::string> lines = getLines();
    tokens = utils::tokenize(lines.at(0));
    fleet["name"] = tokens.at(1);

    for (int i = 1; i < static_cast<int>(lines.size()); i++) {
        // start by tokenizing each line
        tokens = utils::tokenize(lines.at(i));
        std::vector<std::string> nodeLines;

        // TODO: IMPLEMENT THIS
        if (utils::is(tokens.at(0), "government")) {
            std::cout << "\tFleet government is: " << tokens.at(1) << std::endl;
            fleet["government"] = tokens.at(1);
        } else if (utils::is(tokens.at(0), "names")) {
            std::cout << "\tFleet names is: " << tokens.at(1) << std::endl;
            fleet["names"] = tokens.at(1);
        } else if (utils::is(tokens.at(0), "fighters")) {
            i = utils::collectNodeLines(&lines, i, &nodeLines);
            std::cout << "\tFleet fighters is: \n" << boost::join(nodeLines, "") << std::endl;

            json fighters;
            for (int j = 1; j < static_cast<int>(nodeLines.size()); j++) {
                std::vector<std::string> fighters_tokens = utils::tokenize(nodeLines.at(j));
                if (utils::is(fighters_tokens.at(0), "names")) {
                    fighters["names"] = fighters_tokens.at(1);
                }
            }
            fleet["fighters"] = fighters;
        }
    }

    std::cout << "Fleet data: " << fleet.dump(4) << std::endl;
    return fleet;
}

json FileFleetItemParser::getData() const {
    return fleet;
}
