// SPDX-License-Identifier: GPL-3.0-only
/*
 * itemship.h
 *
 * Copyright (c) 2021, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef ITEMSHIP_H
#define ITEMSHIP_H

#include "fileitem.h"

class ItemShip : public FileItem
{
public:
    ItemShip();

    void parse();
};

#endif // ITEMSHIP_H
