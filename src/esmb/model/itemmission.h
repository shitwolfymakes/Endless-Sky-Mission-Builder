// SPDX-License-Identifier: GPL-3.0-only
/*
 * itemmission.h
 *
 * Copyright (c) 2021, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef ITEMMISSION_H
#define ITEMMISSION_H

#include "fileitem.h"

class ItemMission : public FileItem
{
public:
    ItemMission();

    void parse();
};

#endif // ITEMMISSION_H
