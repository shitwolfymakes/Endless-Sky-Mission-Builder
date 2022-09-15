// SPDX-License-Identifier: GPL-3.0-only
/*
 * filesubstitutionsitemparser.h
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef FILESUBSTITUTIONSITEMPARSER_H
#define FILESUBSTITUTIONSITEMPARSER_H

#include "common/fileitemparser.h"

class FileSubstitutionsItemParser : public FileItemParser
{
private:
    json substitutions;

    int parseSubstitution(std::vector<std::string> *, int);

public:
    FileSubstitutionsItemParser(std::vector<std::string>);

    json run();
    json get_data();
};

#endif // FILESUBSTITUTIONSITEMPARSER_H
