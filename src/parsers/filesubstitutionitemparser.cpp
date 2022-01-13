// SPDX-License-Identifier: GPL-3.0-only
/*
 * filesubstitutionitemparser.cpp
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "filesubstitutionitemparser.h"

FileSubstitutionItemParser::FileSubstitutionItemParser(std::vector<std::string> lines)
    : FileItemParser(lines)
{

}

json FileSubstitutionItemParser::run() {
    return substitution;
}
