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
    // define common data
    std::vector<std::string> tokens;
    std::string modifier   = "";
    std::string group      = "planets";
    std::string constraint = "planet";
    std::string elem1      = "Earth";
    std::string elem2      = "Luna";
    std::string elem3      = "Mars";

    json parent, constraint1, constraint2;
    constraint1[constraint] = { elem1, elem2 };
    constraint2[constraint] = { elem3 };
    parent                  = { constraint1, constraint2 };

    // test handling for no modifier
    json expected;
    expected[group] = parent;

    tokens = { constraint, elem1, elem2 };
    parser.parsePlanets(&tokens, 1, modifier);
    tokens = { constraint, elem3 };
    parser.parsePlanets(&tokens, 1, modifier);
    ASSERT_EQ(parser.getData(), expected);

    // test handling for "not" modifier
    modifier = "not";
    json expectedNot;
    expectedNot[modifier][group] = parent;

    // reset parser before testing
    parser = FileFilterItemParser(minimum_filter_lines);
    tokens = { modifier, constraint, elem1, elem2 };
    parser.parsePlanets(&tokens, 2, modifier);
    tokens = { modifier, constraint, elem3 };
    parser.parsePlanets(&tokens, 2, modifier);
    ASSERT_EQ(parser.getData(), expectedNot);

    // test handling for "neighbor" modifier
    modifier = "neighbor";
    json expectedNeighbor;
    expectedNeighbor[modifier][group] = parent;

    // reset parser before testing
    parser = FileFilterItemParser(minimum_filter_lines);
    tokens = { modifier, constraint, elem1, elem2 };
    parser.parsePlanets(&tokens, 2, modifier);
    tokens = { modifier, constraint, elem3 };
    parser.parsePlanets(&tokens, 2, modifier);
    ASSERT_EQ(parser.getData(), expectedNeighbor);
}

TEST_F(FileFilterItemParserTest, TestParseSystems) {
    // define common data
    std::vector<std::string> tokens;
    std::string modifier   = "";
    std::string group      = "systems";
    std::string constraint = "system";
    std::string elem1      = "Sol";
    std::string elem2      = "Alpha Centauri";
    std::string elem3      = "Wolf 359";

    json parent, constraint1, constraint2;
    constraint1[constraint] = { elem1, elem2 };
    constraint2[constraint] = { elem3 };
    parent                  = { constraint1, constraint2 };

    // test handling for no modifier
    json expected;
    expected[group] = parent;

    tokens = { constraint, elem1, elem2 };
    parser.parseSystems(&tokens, 1, modifier);
    tokens = { constraint, elem3 };
    parser.parseSystems(&tokens, 1, modifier);
    ASSERT_EQ(parser.getData(), expected);

    // test handling for "not" modifier
    modifier = "not";
    json expectedNot;
    expectedNot[modifier][group] = parent;

    // reset parser before testing
    parser = FileFilterItemParser(minimum_filter_lines);
    tokens = { modifier, constraint, elem1, elem2 };
    parser.parseSystems(&tokens, 2, modifier);
    tokens = { modifier, constraint, elem3 };
    parser.parseSystems(&tokens, 2, modifier);
    ASSERT_EQ(parser.getData(), expectedNot);

    // test handling for "neighbor" modifier
    modifier = "neighbor";
    json expectedNeighbor;
    expectedNeighbor[modifier][group] = parent;

    // reset parser before testing
    parser = FileFilterItemParser(minimum_filter_lines);
    tokens = { modifier, constraint, elem1, elem2 };
    parser.parseSystems(&tokens, 2, modifier);
    tokens = { modifier, constraint, elem3 };
    parser.parseSystems(&tokens, 2, modifier);
    ASSERT_EQ(parser.getData(), expectedNeighbor);
}

TEST_F(FileFilterItemParserTest, TestParseGovernments) {
    // define common data
    std::vector<std::string> tokens;
    std::string modifier   = "";
    std::string group      = "governments";
    std::string constraint = "government";
    std::string elem1      = "Republic";
    std::string elem2      = "Syndicate";
    std::string elem3      = "Pirate";

    json parent, constraint1, constraint2;
    constraint1[constraint] = { elem1, elem2 };
    constraint2[constraint] = { elem3 };
    parent                  = { constraint1, constraint2 };

    // test handling for no modifier
    json expected;
    expected[group] = parent;

    tokens = { constraint, elem1, elem2 };
    parser.parseAttributes(&tokens, 1, modifier);
    tokens = { constraint, elem3 };
    parser.parseAttributes(&tokens, 1, modifier);
    ASSERT_EQ(parser.getData(), expected);

    // test handling for "not" modifier
    modifier = "not";
    json expectedNot;
    expectedNot[modifier][group] = parent;

    // reset parser before testing
    parser = FileFilterItemParser(minimum_filter_lines);
    tokens = { modifier, constraint, elem1, elem2 };
    parser.parseAttributes(&tokens, 2, modifier);
    tokens = { modifier, constraint, elem3 };
    parser.parseAttributes(&tokens, 2, modifier);
    ASSERT_EQ(parser.getData(), expectedNot);

    // test handling for "neighbor" modifier
    modifier = "neighbor";
    json expectedNeighbor;
    expectedNeighbor[modifier][group] = parent;

    // reset parser before testing
    parser = FileFilterItemParser(minimum_filter_lines);
    tokens = { modifier, constraint, elem1, elem2 };
    parser.parseAttributes(&tokens, 2, modifier);
    tokens = { modifier, constraint, elem3 };
    parser.parseAttributes(&tokens, 2, modifier);
    ASSERT_EQ(parser.getData(), expectedNeighbor);
}

TEST_F(FileFilterItemParserTest, TestParseAttributes) {
    // define common data
    std::vector<std::string> tokens;
    std::string modifier   = "";
    std::string group      = "attributes";
    std::string constraint = "attributes";
    std::string elem1      = "urban";
    std::string elem2      = "tourism";
    std::string elem3      = "dirt belt";

    json parent, constraint1, constraint2;
    constraint1[constraint] = { elem1, elem2 };
    constraint2[constraint] = { elem3 };
    parent                  = { constraint1, constraint2 };

    // test handling for no modifier
    json expected;
    expected[group] = parent;

    tokens = { constraint, elem1, elem2 };
    parser.parseAttributes(&tokens, 1, modifier);
    tokens = { constraint, elem3 };
    parser.parseAttributes(&tokens, 1, modifier);
    ASSERT_EQ(parser.getData(), expected);

    // test handling for "not" modifier
    modifier = "not";
    json expectedNot;
    expectedNot[modifier][group] = parent;

    // reset parser before testing
    parser = FileFilterItemParser(minimum_filter_lines);
    tokens = { modifier, constraint, elem1, elem2 };
    parser.parseAttributes(&tokens, 2, modifier);
    tokens = { modifier, constraint, elem3 };
    parser.parseAttributes(&tokens, 2, modifier);
    ASSERT_EQ(parser.getData(), expectedNot);

    // test handling for "neighbor" modifier
    modifier = "neighbor";
    json expectedNeighbor;
    expectedNeighbor[modifier][group] = parent;

    // reset parser before testing
    parser = FileFilterItemParser(minimum_filter_lines);
    tokens = { modifier, constraint, elem1, elem2 };
    parser.parseAttributes(&tokens, 2, modifier);
    tokens = { modifier, constraint, elem3 };
    parser.parseAttributes(&tokens, 2, modifier);
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
