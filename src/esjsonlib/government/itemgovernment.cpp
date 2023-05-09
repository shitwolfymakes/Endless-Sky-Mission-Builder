// SPDX-License-Identifier: GPL-3.0-only
/*
 * itemgovernment.cpp
 *
 * Copyright (c) 2021, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "itemgovernment.h"

ItemGovernment::ItemGovernment()
{

}

json ItemGovernment::parse() {
    FileGovernmentItemParser parser = FileGovernmentItemParser(lines);
    json govt = parser.run();
    std::cout << "finished parsing government" << std::endl;
    return govt;
}
