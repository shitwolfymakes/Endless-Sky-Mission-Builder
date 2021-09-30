// SPDX-License-Identifier: GPL-3.0-only
/*
 * itemgovernment.h
 *
 * Copyright (c) 2021, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef ITEMGOVERNMENT_H
#define ITEMGOVERNMENT_H

#include "fileitem.h"

class ItemGovernment : public FileItem
{
public:
    ItemGovernment();

    void parse();
};

#endif // ITEMGOVERNMENT_H
