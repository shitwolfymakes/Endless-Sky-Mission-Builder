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
    std::cout << "parsing mission item to JSON" << std::endl;
    FileMissionItemParser parser = FileMissionItemParser(lines);
    json mission = parser.run();
    std::cout << "finished parsing mission" << std::endl;
    return mission;
}
