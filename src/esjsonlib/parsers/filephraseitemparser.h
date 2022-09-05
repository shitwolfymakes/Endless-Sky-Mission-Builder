// SPDX-License-Identifier: GPL-3.0-only
/*
 * filephraseitemparser.h
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef FILEPHRASEITEMPARSER_H
#define FILEPHRASEITEMPARSER_H

#include "parsers/fileitemparser.h"

class FilePhraseItemParser : public FileItemParser
{
private:
    json phrase;

public:
    // CONSTRUCTORS
    FilePhraseItemParser(std::vector<std::string>);

    // MANIPULATORS
    json run();
    int parseWords(std::vector<std::string> *, int);
    int parseSubPhrase(std::vector<std::string> *, int);
    int parseReplace(std::vector<std::string> *, int);

    // ACCESSORS
    json get_data();
};

#endif // FILEPHRASEITEMPARSER_H
