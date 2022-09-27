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
    std::vector<std::string> tokens;

    json expected, expected2, expected3;
    parser = FileFilterItemParser(minimum_filter_lines);
    expected2["planet"].emplace_back("Earth");
    expected2["planet"].emplace_back("Luna");
    expected3["planet"].emplace_back("Mars");
    expected["planets"].emplace_back(expected2);
    expected["planets"].emplace_back(expected3);

    tokens = { "planet", "Earth", "Luna" };
    parser.parsePlanets(tokens, 1, modifier);
    tokens = { "planet", "Mars" };
    parser.parsePlanets(tokens, 1, modifier);
    ASSERT_EQ(parser.getData(), expected);

    json expectedNot, expectedNot2, expectedNot3;
    parser = FileFilterItemParser(minimum_filter_lines);
    expectedNot2["planet"].emplace_back("Earth");
    expectedNot2["planet"].emplace_back("Luna");
    expectedNot3["planet"].emplace_back("Mars");
    expectedNot["not"]["planets"].emplace_back(expectedNot2);
    expectedNot["not"]["planets"].emplace_back(expectedNot3);

    modifier = "not";
    tokens = { "not", "planet", "Earth", "Luna" };
    parser.parsePlanets(tokens, 2, modifier);
    tokens = { "not", "planet", "Mars" };
    parser.parsePlanets(tokens, 2, modifier);
    ASSERT_EQ(parser.getData(), expectedNot);

    json expectedNeighbor, expectedNeighbor2, expectedNeighbor3;
    parser = FileFilterItemParser(minimum_filter_lines);
    expectedNeighbor2["planet"].emplace_back("Earth");
    expectedNeighbor2["planet"].emplace_back("Luna");
    expectedNeighbor3["planet"].emplace_back("Mars");
    expectedNeighbor["neighbor"]["planets"].emplace_back(expectedNeighbor2);
    expectedNeighbor["neighbor"]["planets"].emplace_back(expectedNeighbor3);

    modifier = "neighbor";
    tokens = { "neighbor", "planet", "Earth", "Luna" };
    parser.parsePlanets(tokens, 2, modifier);
    tokens = { "neighbor", "planet", "Mars" };
    parser.parsePlanets(tokens, 2, modifier);
    ASSERT_EQ(parser.getData(), expectedNeighbor);
}

TEST_F(FileFilterItemParserTest, TestParseSystems) {
    std::string modifier = "";

    json expected;
    parser = FileFilterItemParser(minimum_filter_lines);
    expected["systems"]["system"].emplace_back("Sol");
    expected["systems"]["system"].emplace_back("Alpha Centauri");
    std::vector<std::string> tokens = { "system", "Sol", "Alpha Centauri" };
    parser.parseSystems(tokens, 1, modifier);
    ASSERT_EQ(parser.getData(), expected);

    json expectedNot;
    parser = FileFilterItemParser(minimum_filter_lines);
    modifier = "not";
    expectedNot["not"]["systems"]["system"].emplace_back("Sol");
    expectedNot["not"]["systems"]["system"].emplace_back("Alpha Centauri");
    std::vector<std::string> tokensNot = { "not", "system", "Sol", "Alpha Centauri" };
    parser.parseSystems(tokensNot, 2, modifier);
    ASSERT_EQ(parser.getData(), expectedNot);

    json expectedNeighbor;
    parser = FileFilterItemParser(minimum_filter_lines);
    modifier = "neighbor";
    expectedNeighbor["neighbor"]["systems"]["system"].emplace_back("Sol");
    expectedNeighbor["neighbor"]["systems"]["system"].emplace_back("Alpha Centauri");
    std::vector<std::string> tokensNeighbor = { "neighbor", "system", "Sol", "Alpha Centauri" };
    parser.parseSystems(tokensNeighbor, 2, modifier);
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
