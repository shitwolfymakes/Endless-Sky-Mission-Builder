// SPDX-License-Identifier: GPL-3.0-only
/*
 * itemsubstitutions.cpp
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "itemsubstitutions.h"

ItemSubstitutions::ItemSubstitutions()
{

}

json ItemSubstitutions::parse() {
    FileSubstitutionsItemParser parser = FileSubstitutionsItemParser(lines);
    json substitutions = parser.run();
    qDebug() << "finished parsing substitutions";
    return substitutions;
}
