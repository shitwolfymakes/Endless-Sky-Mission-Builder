// SPDX-License-Identifier: GPL-3.0-only
/*
 * itemphrase.h
 *
 * Copyright (c) 2021, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef ITEMPHRASE_H
#define ITEMPHRASE_H

#include "fileitem.h"

class ItemPhrase : public FileItem
{
public:
    ItemPhrase();

    json parse();
};

#endif // ITEMPHRASE_H
