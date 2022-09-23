// SPDX-License-Identifier: GPL-3.0-only
/*
 * fileitemparser.cpp
 *
 * Copyright (c) 2021-2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "fileitemparser.h"

FileItemParser::FileItemParser() {}

void FileItemParser::setLines(std::vector<std::string> lines) {
    this->lines = lines;
}

std::vector<std::string> FileItemParser::getLines() const {
    return lines;
}
