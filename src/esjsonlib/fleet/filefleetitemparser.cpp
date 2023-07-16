// SPDX-License-Identifier: GPL-3.0-only
/*
 * fileleetitemparser.cpp
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
    // TODO: IMPLEMENT THIS

    std::cout << "Fleet data: " << fleet.dump(4) << std::endl;
    return fleet;
}

json FileFleetItemParser::getData() const {
    return fleet;
}
