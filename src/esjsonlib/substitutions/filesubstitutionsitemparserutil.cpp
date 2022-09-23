// SPDX-License-Identifier: GPL-3.0-only
/*
 * filesubstitutionsitemparserutil.cpp
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "filesubstitutionsitemparserutil.h"

#include "filesubstitutionsitemparser.h"

FileSubstitutionsItemParser* FileSubstitutionsItemParserUtil::create(std::vector<std::string> lines) {
    FileSubstitutionsItemParser *parser = new FileSubstitutionsItemParser(lines);
    return parser;
}
