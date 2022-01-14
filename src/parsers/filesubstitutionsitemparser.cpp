// SPDX-License-Identifier: GPL-3.0-only
/*
 * filesubstitutionsitemparser.cpp
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "filesubstitutionsitemparser.h"

FileSubstitutionsItemParser::FileSubstitutionsItemParser(std::vector<std::string> lines)
    : FileItemParser(lines)
{

}

json FileSubstitutionsItemParser::run() {
    return substitutions;
}

json FileSubstitutionsItemParser::get_data() {
    return substitutions;
}
