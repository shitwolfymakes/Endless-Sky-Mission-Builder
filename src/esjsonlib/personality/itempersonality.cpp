// SPDX-License-Identifier: GPL-3.0-only
/*
 * itempersonality.cpp
 *
 * Copyright (c) 2023, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "itempersonality.h"

ItemPersonality::ItemPersonality()
{

}

json ItemPersonality::parse() {
    FilePersonalityItemParser parser = FilePersonalityItemParser(lines);
    json personality = parser.run();
    std::cout << "finished parsing personality" << std::endl;
    return personality;
}
