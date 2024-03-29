// SPDX-License-Identifier: GPL-3.0-only
/*
 * itemsubstitutions.h
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef ITEMSUBSTITUTIONS_H
#define ITEMSUBSTITUTIONS_H

#include "common/fileitem.h"
#include "substitutions/filesubstitutionsitemparser.h"

class ItemSubstitutions : public FileItem
{
public:
    ItemSubstitutions();

    json parse();
};

#endif // ITEMSUBSTITUTIONS_H
