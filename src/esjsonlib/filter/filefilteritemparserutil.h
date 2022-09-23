// SPDX-License-Identifier: GPL-3.0-only
/*
 * filefilteritemparserutil.h
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef FILEFILTERITEMPARSERUTIL_H
#define FILEFILTERITEMPARSERUTIL_H

#include <string>
#include <vector>

class FileFilterItemParser;

struct FileFilterItemParserUtil {
    FileFilterItemParser* create(std::vector<std::string> lines);
};

#endif // FILEFILTERITEMPARSERUTIL_H
