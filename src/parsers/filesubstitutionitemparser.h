// SPDX-License-Identifier: GPL-3.0-only
/*
 * filesubstitutionitemparser.h
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef FILESUBSTITUTIONITEMPARSER_H
#define FILESUBSTITUTIONITEMPARSER_H

#include "fileitemparser.h"

class FileSubstitutionItemParser : public FileItemParser
{
private:
    json substitution;

public:
    FileSubstitutionItemParser(std::vector<std::string>);

    json run();
};

#endif // FILESUBSTITUTIONITEMPARSER_H
