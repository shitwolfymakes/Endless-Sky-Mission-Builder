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

} // namespace parsertests
