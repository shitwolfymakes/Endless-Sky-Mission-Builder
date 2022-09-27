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
    std::vector<std::string> tokens;
    std::string modifier = "";

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

    modifier = "not";
    json expectedNot, expectedNot2, expectedNot3;
    parser = FileFilterItemParser(minimum_filter_lines);
    expectedNot2["planet"].emplace_back("Earth");
    expectedNot2["planet"].emplace_back("Luna");
    expectedNot3["planet"].emplace_back("Mars");
    expectedNot[modifier]["planets"].emplace_back(expectedNot2);
    expectedNot[modifier]["planets"].emplace_back(expectedNot3);

    tokens = { modifier, "planet", "Earth", "Luna" };
    parser.parsePlanets(tokens, 2, modifier);
    tokens = { modifier, "planet", "Mars" };
    parser.parsePlanets(tokens, 2, modifier);
    ASSERT_EQ(parser.getData(), expectedNot);

    modifier = "neighbor";
    json expectedNeighbor, expectedNeighbor2, expectedNeighbor3;
    parser = FileFilterItemParser(minimum_filter_lines);
    expectedNeighbor2["planet"].emplace_back("Earth");
    expectedNeighbor2["planet"].emplace_back("Luna");
    expectedNeighbor3["planet"].emplace_back("Mars");
    expectedNeighbor[modifier]["planets"].emplace_back(expectedNeighbor2);
    expectedNeighbor[modifier]["planets"].emplace_back(expectedNeighbor3);

    tokens = { modifier, "planet", "Earth", "Luna" };
    parser.parsePlanets(tokens, 2, modifier);
    tokens = { modifier, "planet", "Mars" };
    parser.parsePlanets(tokens, 2, modifier);
    ASSERT_EQ(parser.getData(), expectedNeighbor);
}

TEST_F(FileFilterItemParserTest, TestParseSystems) {
    std::vector<std::string> tokens;
    std::string modifier = "";

    json expected, expected2, expected3;
    parser = FileFilterItemParser(minimum_filter_lines);
    expected2["system"].emplace_back("Sol");
    expected2["system"].emplace_back("Alpha Centauri");
    expected3["system"].emplace_back("Wolf 359");
    expected["systems"].emplace_back(expected2);
    expected["systems"].emplace_back(expected3);

    tokens = { "system", "Sol", "Alpha Centauri" };
    parser.parseSystems(tokens, 1, modifier);
    tokens = { "system", "Wolf 359" };
    parser.parseSystems(tokens, 1, modifier);
    ASSERT_EQ(parser.getData(), expected);

    modifier = "not";
    json expectedNot, expectedNot2, expectedNot3;
    parser = FileFilterItemParser(minimum_filter_lines);
    expectedNot2["system"].emplace_back("Sol");
    expectedNot2["system"].emplace_back("Alpha Centauri");
    expectedNot3["system"].emplace_back("Wolf 359");
    expectedNot[modifier]["systems"].emplace_back(expectedNot2);
    expectedNot[modifier]["systems"].emplace_back(expectedNot3);

    tokens = { modifier, "system", "Sol", "Alpha Centauri" };
    parser.parseSystems(tokens, 2, modifier);
    tokens = { modifier, "system", "Wolf 359" };
    parser.parseSystems(tokens, 2, modifier);
    ASSERT_EQ(parser.getData(), expectedNot);

    modifier = "neighbor";
    json expectedNeighbor, expectedNeighbor2, expectedNeighbor3;
    parser = FileFilterItemParser(minimum_filter_lines);
    expectedNeighbor2["system"].emplace_back("Sol");
    expectedNeighbor2["system"].emplace_back("Alpha Centauri");
    expectedNeighbor3["system"].emplace_back("Wolf 359");
    expectedNeighbor[modifier]["systems"].emplace_back(expectedNeighbor2);
    expectedNeighbor[modifier]["systems"].emplace_back(expectedNeighbor3);

    tokens = { modifier, "system", "Sol", "Alpha Centauri" };
    parser.parseSystems(tokens, 2, modifier);
    tokens = { modifier, "system", "Wolf 359" };
    parser.parseSystems(tokens, 2, modifier);
    ASSERT_EQ(parser.getData(), expectedNeighbor);
}

TEST_F(FileFilterItemParserTest, TestParseGovernments) {
    std::vector<std::string> tokens;
    std::string modifier = "";

    json expected, expected2, expected3;
    parser = FileFilterItemParser(minimum_filter_lines);
    expected2["government"].emplace_back("Republic");
    expected2["government"].emplace_back("Syndicate");
    expected3["government"].emplace_back("Pirate");
    expected["governments"].emplace_back(expected2);
    expected["governments"].emplace_back(expected3);

    tokens = { "government", "Republic", "Syndicate" };
    parser.parseGovernments(tokens, 1, modifier);
    tokens = { "government", "Pirate" };
    parser.parseGovernments(tokens, 1, modifier);
    ASSERT_EQ(parser.getData(), expected);

    modifier = "not";
    json expectedNot, expectedNot2, expectedNot3;
    parser = FileFilterItemParser(minimum_filter_lines);
    expectedNot2["government"].emplace_back("Republic");
    expectedNot2["government"].emplace_back("Syndicate");
    expectedNot3["government"].emplace_back("Pirate");
    expectedNot[modifier]["governments"].emplace_back(expectedNot2);
    expectedNot[modifier]["governments"].emplace_back(expectedNot3);

    tokens = { modifier, "government", "Republic", "Syndicate" };
    parser.parseGovernments(tokens, 2, modifier);
    tokens = { modifier, "government", "Pirate" };
    parser.parseGovernments(tokens, 2, modifier);
    ASSERT_EQ(parser.getData(), expectedNot);

    modifier = "neighbor";
    json expectedNeighbor, expectedNeighbor2, expectedNeighbor3;
    parser = FileFilterItemParser(minimum_filter_lines);
    expectedNeighbor2["government"].emplace_back("Republic");
    expectedNeighbor2["government"].emplace_back("Syndicate");
    expectedNeighbor3["government"].emplace_back("Pirate");
    expectedNeighbor[modifier]["governments"].emplace_back(expectedNeighbor2);
    expectedNeighbor[modifier]["governments"].emplace_back(expectedNeighbor3);

    tokens = { modifier, "government", "Republic", "Syndicate" };
    parser.parseGovernments(tokens, 2, modifier);
    tokens = { modifier, "government", "Pirate" };
    parser.parseGovernments(tokens, 2, modifier);
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
