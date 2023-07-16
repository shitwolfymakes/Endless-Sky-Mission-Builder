// SPDX-License-Identifier: GPL-3.0-only
/*
 * filefleetitemparserutil.cpp
 *
 * Copyright (c) 2023, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "filefleetitemparserutil.h"

#include "filefleetitemparser.h"

FileFleetItemParser* FileFleetItemParserUtil::create(std::vector<std::string> lines) {
    FileFleetItemParser *parser = new FileFleetItemParser(lines);
    return parser;
}
