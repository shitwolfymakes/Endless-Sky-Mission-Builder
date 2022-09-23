// SPDX-License-Identifier: GPL-3.0-only
/*
 * filephraseitemparserutil.h
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef FILEPHRASEITEMPARSERUTIL_H
#define FILEPHRASEITEMPARSERUTIL_H

#include <string>
#include <vector>

class FilePhraseItemParser;

struct FilePhraseItemParserUtil {
    static FilePhraseItemParser* create(std::vector<std::string> lines);
};

#endif // FILEPHRASEITEMPARSERUTIL_H
