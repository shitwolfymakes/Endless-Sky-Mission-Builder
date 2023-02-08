// SPDX-License-Identifier: GPL-3.0-only
/*
 * fileeventitemparser.cpp
 *
 * Copyright (c) 2023, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "fileeventitemparser.h"

#include <iostream>

FileEventItemParser::FileEventItemParser(std::vector<std::string> lines) {
    setLines(lines);
}

json FileEventItemParser::run() {
    std::cout << "Parsing substitutions node to JSON" << std::endl;

    // TODO: Implement this

    return event;
}
