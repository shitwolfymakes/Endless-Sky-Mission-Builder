// SPDX-License-Identifier: GPL-3.0-only
/*
 * itemphrase.cpp
 *
 * Copyright (c) 2021-2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "itemphrase.h"

ItemPhrase::ItemPhrase()
{

}

json ItemPhrase::parse() {
    FilePhraseItemParser parser = FilePhraseItemParser(lines);
    json phrase = parser.run();
    std::cout << "finished parsing phrase" << std::endl;
    return phrase;
}
