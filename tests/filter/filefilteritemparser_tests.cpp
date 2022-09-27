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
    std::string parent = "planets";
    std::string constraint = "planet";
    std::string modifier = "";

    json expected, expected2, expected3;
    parser = FileFilterItemParser(minimum_filter_lines);
    expected2[constraint].emplace_back("Earth");
    expected2[constraint].emplace_back("Luna");
    expected3[constraint].emplace_back("Mars");
    expected[parent].emplace_back(expected2);
    expected[parent].emplace_back(expected3);

    tokens = { constraint, "Earth", "Luna" };
    parser.parsePlanets(tokens, 1, modifier);
    tokens = { constraint, "Mars" };
    parser.parsePlanets(tokens, 1, modifier);
    ASSERT_EQ(parser.getData(), expected);

    modifier = "not";
    json expectedNot, expectedNot2, expectedNot3;
    parser = FileFilterItemParser(minimum_filter_lines);
    expectedNot2[constraint].emplace_back("Earth");
    expectedNot2[constraint].emplace_back("Luna");
    expectedNot3[constraint].emplace_back("Mars");
    expectedNot[modifier][parent].emplace_back(expectedNot2);
    expectedNot[modifier][parent].emplace_back(expectedNot3);

    tokens = { modifier, constraint, "Earth", "Luna" };
    parser.parsePlanets(tokens, 2, modifier);
    tokens = { modifier, constraint, "Mars" };
    parser.parsePlanets(tokens, 2, modifier);
    ASSERT_EQ(parser.getData(), expectedNot);

    modifier = "neighbor";
    json expectedNeighbor, expectedNeighbor2, expectedNeighbor3;
    parser = FileFilterItemParser(minimum_filter_lines);
    expectedNeighbor2[constraint].emplace_back("Earth");
    expectedNeighbor2[constraint].emplace_back("Luna");
    expectedNeighbor3[constraint].emplace_back("Mars");
    expectedNeighbor[modifier]["planets"].emplace_back(expectedNeighbor2);
    expectedNeighbor[modifier]["planets"].emplace_back(expectedNeighbor3);

    tokens = { modifier, constraint, "Earth", "Luna" };
    parser.parsePlanets(tokens, 2, modifier);
    tokens = { modifier, constraint, "Mars" };
    parser.parsePlanets(tokens, 2, modifier);
    ASSERT_EQ(parser.getData(), expectedNeighbor);
}

TEST_F(FileFilterItemParserTest, TestParseSystems) {
    std::vector<std::string> tokens;
    std::string parent = "systems";
    std::string constraint = "system";
    std::string modifier = "";

    json expected, expected2, expected3;
    parser = FileFilterItemParser(minimum_filter_lines);
    expected2[constraint].emplace_back("Sol");
    expected2[constraint].emplace_back("Alpha Centauri");
    expected3[constraint].emplace_back("Wolf 359");
    expected[parent].emplace_back(expected2);
    expected[parent].emplace_back(expected3);

    tokens = { constraint, "Sol", "Alpha Centauri" };
    parser.parseSystems(tokens, 1, modifier);
    tokens = { constraint, "Wolf 359" };
    parser.parseSystems(tokens, 1, modifier);
    ASSERT_EQ(parser.getData(), expected);

    modifier = "not";
    json expectedNot, expectedNot2, expectedNot3;
    parser = FileFilterItemParser(minimum_filter_lines);
    expectedNot2[constraint].emplace_back("Sol");
    expectedNot2[constraint].emplace_back("Alpha Centauri");
    expectedNot3[constraint].emplace_back("Wolf 359");
    expectedNot[modifier][parent].emplace_back(expectedNot2);
    expectedNot[modifier][parent].emplace_back(expectedNot3);

    tokens = { modifier, constraint, "Sol", "Alpha Centauri" };
    parser.parseSystems(tokens, 2, modifier);
    tokens = { modifier, constraint, "Wolf 359" };
    parser.parseSystems(tokens, 2, modifier);
    ASSERT_EQ(parser.getData(), expectedNot);

    modifier = "neighbor";
    json expectedNeighbor, expectedNeighbor2, expectedNeighbor3;
    parser = FileFilterItemParser(minimum_filter_lines);
    expectedNeighbor2[constraint].emplace_back("Sol");
    expectedNeighbor2[constraint].emplace_back("Alpha Centauri");
    expectedNeighbor3[constraint].emplace_back("Wolf 359");
    expectedNeighbor[modifier][parent].emplace_back(expectedNeighbor2);
    expectedNeighbor[modifier][parent].emplace_back(expectedNeighbor3);

    tokens = { modifier, constraint, "Sol", "Alpha Centauri" };
    parser.parseSystems(tokens, 2, modifier);
    tokens = { modifier, constraint, "Wolf 359" };
    parser.parseSystems(tokens, 2, modifier);
    ASSERT_EQ(parser.getData(), expectedNeighbor);
}

TEST_F(FileFilterItemParserTest, TestParseGovernments) {
    std::vector<std::string> tokens;
    std::string parent = "governments";
    std::string constraint = "government";
    std::string modifier = "";

    json expected, expected2, expected3;
    parser = FileFilterItemParser(minimum_filter_lines);
    expected2[constraint].emplace_back("Republic");
    expected2[constraint].emplace_back("Syndicate");
    expected3[constraint].emplace_back("Pirate");
    expected[parent].emplace_back(expected2);
    expected[parent].emplace_back(expected3);

    tokens = { constraint, "Republic", "Syndicate" };
    parser.parseGovernments(tokens, 1, modifier);
    tokens = { constraint, "Pirate" };
    parser.parseGovernments(tokens, 1, modifier);
    ASSERT_EQ(parser.getData(), expected);

    modifier = "not";
    json expectedNot, expectedNot2, expectedNot3;
    parser = FileFilterItemParser(minimum_filter_lines);
    expectedNot2[constraint].emplace_back("Republic");
    expectedNot2[constraint].emplace_back("Syndicate");
    expectedNot3[constraint].emplace_back("Pirate");
    expectedNot[modifier][parent].emplace_back(expectedNot2);
    expectedNot[modifier][parent].emplace_back(expectedNot3);

    tokens = { modifier, constraint, "Republic", "Syndicate" };
    parser.parseGovernments(tokens, 2, modifier);
    tokens = { modifier, constraint, "Pirate" };
    parser.parseGovernments(tokens, 2, modifier);
    ASSERT_EQ(parser.getData(), expectedNot);

    modifier = "neighbor";
    json expectedNeighbor, expectedNeighbor2, expectedNeighbor3;
    parser = FileFilterItemParser(minimum_filter_lines);
    expectedNeighbor2[constraint].emplace_back("Republic");
    expectedNeighbor2[constraint].emplace_back("Syndicate");
    expectedNeighbor3[constraint].emplace_back("Pirate");
    expectedNeighbor[modifier]["governments"].emplace_back(expectedNeighbor2);
    expectedNeighbor[modifier]["governments"].emplace_back(expectedNeighbor3);

    tokens = { modifier, constraint, "Republic", "Syndicate" };
    parser.parseGovernments(tokens, 2, modifier);
    tokens = { modifier, constraint, "Pirate" };
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
