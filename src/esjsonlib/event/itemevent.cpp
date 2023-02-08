// SPDX-License-Identifier: GPL-3.0-only
/*
 * itemevent.cpp
 *
 * Copyright (c) 2021, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "itemevent.h"

ItemEvent::ItemEvent()
{

}

json ItemEvent::parse() {
    FileEventItemParser parser = FileEventItemParser(lines);
    json event = parser.run();
    std::cout << "finished parsing event" << std::endl;
    return event;
}
