// SPDX-License-Identifier: GPL-3.0-only
/*
 * itemsubstitution.cpp
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "itemsubstitution.h"

ItemSubstitution::ItemSubstitution()
{

}

json ItemSubstitution::parse() {
    // TODO: Implement this
    qDebug() << "parsing mission item to JSON";
    FileSubstitutionItemParser parser = FileSubstitutionItemParser(lines);
    json mission = parser.run();
    qDebug() << "finished parsing mission";
    return mission;
}
