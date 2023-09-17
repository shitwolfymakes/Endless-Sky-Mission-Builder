// SPDX-License-Identifier: GPL-3.0-only
/*
 * filepersonalityitemparser.cpp
 *
 * Copyright (c) 2023, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "filepersonalityitemparser.h"

FilePersonalityItemParser::FilePersonalityItemParser(std::vector<std::string> lines)
{
    setLines(lines);
}

json FilePersonalityItemParser::run() {
    return personality;
}
