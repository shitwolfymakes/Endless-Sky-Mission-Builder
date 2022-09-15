// SPDX-License-Identifier: GPL-3.0-only
/*
 * itemevent.h
 *
 * Copyright (c) 2021, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef ITEMEVENT_H
#define ITEMEVENT_H

#include "model/fileitem.h"

class ItemEvent : public FileItem
{
public:
    ItemEvent();

    json parse();
};

#endif // ITEMEVENT_H
