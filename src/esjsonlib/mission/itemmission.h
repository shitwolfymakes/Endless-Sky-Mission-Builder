// SPDX-License-Identifier: GPL-3.0-only
/*
 * itemmission.h
 *
 * Copyright (c) 2021, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef ITEMMISSION_H
#define ITEMMISSION_H

#include "common/fileitem.h"
#include "mission/filemissionitemparser.h"

class ItemMission : public FileItem
{
public:
    ItemMission();

    json parse();
};

#endif // ITEMMISSION_H
