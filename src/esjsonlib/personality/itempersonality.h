// SPDX-License-Identifier: GPL-3.0-only
/*
 * itempersonality.h
 *
 * Copyright (c) 2023, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef ITEMPERSONALITY_H
#define ITEMPERSONALITY_H

#include <common/fileitem.h>
#include <personality/filepersonalityitemparser.h>

class ItemPersonality : public FileItem
{
public:
    ItemPersonality();

    json parse();
};

#endif // ITEMPERSONALITY_H
