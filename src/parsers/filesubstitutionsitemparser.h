// SPDX-License-Identifier: GPL-3.0-only
/*
 * filesubstitutionsitemparser.h
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef FILESUBSTITUTIONSITEMPARSER_H
#define FILESUBSTITUTIONSITEMPARSER_H

#include "fileitemparser.h"

class FileSubstitutionsItemParser : public FileItemParser
{
private:
    json substitutions;

public:
    FileSubstitutionsItemParser(std::vector<std::string>);

    json run();
};

#endif // FILESUBSTITUTIONSITEMPARSER_H
