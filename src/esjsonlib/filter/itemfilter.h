// SPDX-License-Identifier: GPL-3.0-only
/*
 * itemfilter.h
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef ITEMFILTER_H
#define ITEMFILTER_H

#include <common/fileitem.h>

class ItemFilter : public FileItem
{
public:
    ItemFilter();

    json parse();
};

#endif // ITEMFILTER_H
