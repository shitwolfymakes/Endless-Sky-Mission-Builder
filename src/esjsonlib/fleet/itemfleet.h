// SPDX-License-Identifier: GPL-3.0-only
/*
 * itemfleet.h
 *
 * Copyright (c) 2023, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef ITEMFLEET_H
#define ITEMFLEET_H

#include "common/fileitem.h"

class ItemFleet : public FileItem
{
public:
    ItemFleet();

    json parse();
};

#endif // ITEMFLEET_H
