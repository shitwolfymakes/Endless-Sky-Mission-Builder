// SPDX-License-Identifier: GPL-3.0-only
/*
 * filegovernmentitemparser_tests.cpp
 *
 * Copyright (c) 2023, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "filegovernmentitemparser_tests.h"

using namespace testing;

namespace parsertests {

// Test top level field parsing
TEST_F(FileGovernmentItemParserTest, TestEventParsing) {
    // TODO: Implement this
    ASSERT_EQ(0, 0);
}

TEST_F(FileGovernmentItemParserTest, TestParseId) {
    std::string token = "GalacticFederation";
    parser.parseId(token);
    ASSERT_EQ(parser.getData()["id"], "GalacticFederation");
}

TEST_F(FileGovernmentItemParserTest, TestParseDisplayName) {
    std::string token = "Galactic Federation";
    parser.parseDisplayName(token);
    ASSERT_EQ(parser.getData()["display_name"], "Galactic Federation");
}

} // namespace parsertests
