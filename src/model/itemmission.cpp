// SPDX-License-Identifier: GPL-3.0-only
/*
 * itemmission.cpp
 *
 * Copyright (c) 2021, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "itemmission.h"

ItemMission::ItemMission()
{

}

json ItemMission::parse() {
    qDebug() << "parsing mission item to JSON";
    FileMissionItemParser parser = FileMissionItemParser(lines);
    json mission = parser.run();
    qDebug() << "finished parsing mission";
    return mission;
}
