// SPDX-License-Identifier: GPL-3.0-only
/*
 * filesubstitutionsitemparserutil.h
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef FILESUBSTITUTIONSITEMPARSERUTIL_H
#define FILESUBSTITUTIONSITEMPARSERUTIL_H

#include <string>
#include <vector>

class FileSubstitutionsItemParser;

struct FileSubstitutionsItemParserUtil {
    FileSubstitutionsItemParser* create(std::vector<std::string> lines);
};

#endif // FILESUBSTITUTIONSITEMPARSERUTIL_H
