// SPDX-License-Identifier: GPL-3.0-only
/*
 * fileitemparserimpl.cpp
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "fileitemparserimpl.h"

FileItemParserImpl::FileItemParserImpl() {}

void FileItemParserImpl::setLines(std::vector<std::string> lines) {
    this->lines = lines;
}

std::vector<std::string> FileItemParserImpl::getLines() const {
    return lines;
}
