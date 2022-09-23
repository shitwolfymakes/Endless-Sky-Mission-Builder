// SPDX-License-Identifier: GPL-3.0-only
/*
 * filephraseitemparserutil.h
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "filephraseitemparserutil.h"

#include "filephraseitemparser.h"

FilePhraseItemParser* FilePhraseItemParserUtil::create(std::vector<std::string> lines) {
    FilePhraseItemParser *parser = new FilePhraseItemParser(lines);
    return parser;
}
