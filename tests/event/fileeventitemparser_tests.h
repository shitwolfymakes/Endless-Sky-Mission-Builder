// SPDX-License-Identifier: GPL-3.0-only
/*
 * fileeventitemparser_tests.h
 *
 * Copyright (c) 2023, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef FILEEVENTITEMPARSER_TESTS_H
#define FILEEVENTITEMPARSER_TESTS_H

#include <gtest/gtest.h>
#include <gmock/gmock.h>

#include "event/fileeventitemparser.h"

namespace parsertests {

std::string EVENT_NODE_HEADER = "event \"The Savior's Return\"\n";

std::vector<std::string> empty_event_node = {
    "event \"The Savior's Return\"\n"
};

std::vector<std::string> sample_event_node = {
    "event \"The Savior's Return\"",
    "\tdate 4 20 69",
    "\tvisit \"Heaven\"",
    "\tunvisit \"Big Chungus\"",
    "\t\"visit planet\" Harambe",
    "\t\"unvisit planet\" \"Absolute Unit\"",
    "\tgalaxy \"My Ass\"",
    "\tsystem \"Eat It\"",
    "\tlink Heaven Sol",
    "\tunlink \"Big Chungus\" \"Beta Capriconi\"",
    "\tgovernment \"Apes Together Strong\"",
    "\tfleet \"Harambe's Bois\"",
    "\tplanet \"Heaven 2\"",
    "\tnews \"Harambe Alive\"",
    "\tshipyard \"Bog Standard\"",
    "\toutfitter \"Marcus Munitions\""
};

// Fixture for testing a node
class FileEventItemParserTest : public ::testing::Test {
protected:
    FileEventItemParser parser = FileEventItemParser(empty_event_node);
};

} // namespace parsertests

#endif // FILEEVENTITEMPARSER_TESTS_H
