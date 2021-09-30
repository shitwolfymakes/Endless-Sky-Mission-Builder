// SPDX-License-Identifier: GPL-3.0-only
/*
 * event.h
 *
 * Copyright (c) 2021, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef EVENT_H
#define EVENT_H

#include "fileitem.h"

class Event : public FileItem
{
public:
    Event();

    void parse();
};

#endif // EVENT_H
