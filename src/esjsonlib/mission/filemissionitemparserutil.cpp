// SPDX-License-Identifier: GPL-3.0-only
/*
 * filemissionitemparserutil.cpp
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "filemissionitemparserutil.h"

#include "filemissionitemparser.h"

FileMissionItemParser* FileMissionItemParserUtil::create(std::vector<std::string> lines) {
    FileMissionItemParser *parser = new FileMissionItemParser(lines);
    return parser;
}
