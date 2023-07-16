// SPDX-License-Identifier: GPL-3.0-only
/*
 * filefleetitemparserutil.h
 *
 * Copyright (c) 2023, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef FILEFLEETITEMPARSERUTIL_H
#define FILEFLEETITEMPARSERUTIL_H

#include <string>
#include <vector>

class FileFleetItemParser;

struct FileFleetItemParserUtil {
    static FileFleetItemParser* create(std::vector<std::string> lines);
};

#endif // FILEFLEETITEMPARSERUTIL_H
