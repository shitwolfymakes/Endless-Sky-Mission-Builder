// SPDX-License-Identifier: GPL-3.0-only
/*
 * filefilteritemparser_tests.cpp
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */
#include "filefilteritemparser_tests.h"

using namespace testing;

namespace parsertests {

TEST_F(FileFilterItemParserTest, TestParsePlanets) {
    std::string modifier = "";

    json expected;
    parser = FileFilterItemParser(minimum_filter_lines);
    expected["planets"]["planet"].emplace_back("Earth");
    expected["planets"]["planet"].emplace_back("Luna");
    expected["planets"]["planet"].emplace_back("Mars");
    std::vector<std::string> tokens = { "planet", "Earth", "Luna", "Mars" };
    parser.parsePlanets(tokens, 1, modifier);
    ASSERT_EQ(parser.getData(), expected);

    json expectedNot;
    parser = FileFilterItemParser(minimum_filter_lines);
    modifier = "not";
    expectedNot["not"]["planets"]["planet"].emplace_back("Earth");
    expectedNot["not"]["planets"]["planet"].emplace_back("Luna");
    expectedNot["not"]["planets"]["planet"].emplace_back("Mars");
    std::vector<std::string> tokensNot = { "not", "planet", "Earth", "Luna", "Mars" };
    parser.parsePlanets(tokensNot, 2, modifier);
    ASSERT_EQ(parser.getData(), expectedNot);

    json expectedNeighbor;
    parser = FileFilterItemParser(minimum_filter_lines);
    modifier = "neighbor";
    expectedNeighbor["neighbor"]["planets"]["planet"].emplace_back("Earth");
    expectedNeighbor["neighbor"]["planets"]["planet"].emplace_back("Luna");
    expectedNeighbor["neighbor"]["planets"]["planet"].emplace_back("Mars");
    std::vector<std::string> tokensNeighbor = { "neighbor", "planet", "Earth", "Luna", "Mars" };
    parser.parsePlanets(tokensNeighbor, 2, modifier);
    ASSERT_EQ(parser.getData(), expectedNeighbor);
}

TEST_F(FileFilterItemParserTest, TestIsModifier) {
    bool result = FileFilterItemParser::isModifier("not");
    ASSERT_EQ(result, true);

    result = FileFilterItemParser::isModifier("neighbor");
    ASSERT_EQ(result, true);

    result = FileFilterItemParser::isModifier("asdf");
    ASSERT_EQ(result, false);
}

} // namespace parsertests
