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
    FilePhraseItemParser(std::vector<std::string>);

    json run();

    json get_data();
};

#endif // FILEPHRASEITEMPARSER_H
