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
    // DATA
    json substitutions;\

public:
    // CREATORS
    FileSubstitutionsItemParser(std::vector<std::string>);

    // MANIPULATORS
    json run();

    int parseSubstitution(std::vector<std::string> *, int);

    // ACCESSORS
    json get_data() const;
};

#endif // FILESUBSTITUTIONSITEMPARSER_H
