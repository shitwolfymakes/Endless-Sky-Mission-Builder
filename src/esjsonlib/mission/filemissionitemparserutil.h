// SPDX-License-Identifier: GPL-3.0-only
/*
 * filemissionitemparserutil.h
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef FILEMISSIONITEMPARSERUTIL_H
#define FILEMISSIONITEMPARSERUTIL_H

#include <string>
#include <vector>

class FileMissionItemParser;

struct FileMissionItemParserUtil {
    static FileMissionItemParser* create(std::vector<std::string> lines);
};

#endif // FILEMISSIONITEMPARSERUTIL_H
