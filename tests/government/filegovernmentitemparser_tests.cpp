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

TEST_F(FileGovernmentItemParserTest, TestParseSwizzle) {
    std::string token = "6";
    parser.parseSwizzle(token);
    ASSERT_EQ(parser.getData()["swizzle"], 6);
}

TEST_F(FileGovernmentItemParserTest, TestParseColorRGB) {
    std::vector<std::string> tokens = {"color", "128", "128", "128"};
    json color;
    color["R"] = 128;
    color["G"] = 128;
    color["B"] = 128;
    parser.parseColor(tokens);
    ASSERT_EQ(parser.getData()["color"], color);
}

TEST_F(FileGovernmentItemParserTest, TestParseColorName) {
    std::vector<std::string> tokens = {"color", "Red"};
    json color;
    color = "Red";
    parser.parseColor(tokens);
    ASSERT_EQ(parser.getData()["color"], "Red");
}

TEST_F(FileGovernmentItemParserTest, TestParsePlayerRep) {
    std::string token = "100";
    parser.parsePlayerRep(token);
    ASSERT_EQ(parser.getData()["player_reputation"], 100);
}

} // namespace parsertests
