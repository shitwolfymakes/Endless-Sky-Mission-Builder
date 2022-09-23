// SPDX-License-Identifier: GPL-3.0-only
/*
 * filefilteritemparserutil.cpp
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "filefilteritemparserutil.h"

#include "filefilteritemparser.h"

FileFilterItemParser* FileFilterItemParserUtil::create(std::vector<std::string> lines) {
    FileFilterItemParser *parser = new FileFilterItemParser(lines);
    return parser;
}
