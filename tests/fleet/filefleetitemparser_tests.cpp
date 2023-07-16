// SPDX-License-Identifier: GPL-3.0-only
/*
 * filefleetitemparser_tests.cpp
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */
#include "filefleetitemparser_tests.h"
#include "common/fileitemparserutils.h"

using namespace testing;

namespace parsertests {

TEST_F(FileFleetItemParserTest, TestEmptyFleetParsing) {
    // declare an empty fleet node
    json fleet = parser.run();

    json expected;
    expected["name"] = "Black Swan";

    ASSERT_EQ(fleet, expected);
}

TEST_F(FileFleetItemParserTest, TestParseGovernment) {
    std::vector<std::string> nodeLines = {FLEET_NODE_HEADER,
                                          "\tgovernment \"Free Worlds\"\n"};
    parser.setLines(nodeLines);

    json fleet = parser.run();
    ASSERT_EQ(fleet["government"], "Free Worlds");
}

} // namespace parsertests
