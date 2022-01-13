// SPDX-License-Identifier: GPL-3.0-only
/*
 * itemsubstitution.h
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef ITEMSUBSTITUTION_H
#define ITEMSUBSTITUTION_H

#include "fileitem.h"
#include "parsers/filesubstitutionitemparser.h"

class ItemSubstitution : public FileItem
{
public:
    ItemSubstitution();

    json parse();
};

#endif // ITEMSUBSTITUTION_H
