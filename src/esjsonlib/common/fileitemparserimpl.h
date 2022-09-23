// SPDX-License-Identifier: GPL-3.0-only
/*
 * fileitemparserimpl.h
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef FILEITEMPARSERIMPL_H
#define FILEITEMPARSERIMPL_H

#include "fileitemparser.h"

#include <string>
#include <vector>

class FileItemParserImpl : public FileItemParser {
    std::vector<std::string> lines;

public:
    // CREATORS
    FileItemParserImpl();

    // MANIPULATORS
    void setLines(std::vector<std::string>);

    // ACCESSORS
    std::vector<std::string> getLines() const;
};

#endif // FILEITEMPARSERIMPL_H
