// SPDX-License-Identifier: GPL-3.0-only
/*
 * filefilteritemparser.cpp
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "filefilteritemparser.h"

#include <iostream>

FileFilterItemParser::FileFilterItemParser(std::vector<std::string> lines) {
    setLines(lines);
}

json FileFilterItemParser::run() {
    std::cout << "FILTER PARSING NOT IMPLEMENTED YET" << std::endl;
    return filter;
}

int FileFilterItemParser::parseFilter(std::vector<std::string> *nodeLines, int startingIndex) {
    return -1;
}

json FileFilterItemParser::getData() const {
    return filter;
}
