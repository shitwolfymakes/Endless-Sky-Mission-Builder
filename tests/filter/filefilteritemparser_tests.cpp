// SPDX-License-Identifier: GPL-3.0-only
/*
 * filefilteritemparser_tests.cpp
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */
#include "filefilteritemparser_tests.h"
#include "common/fileitemparserutils.h"

using namespace testing;

namespace parsertests {

TEST_F(FileFilterItemParserTest, TestParseFilter) {
    /** Text representation:
     * planet "Earth"
     * system "Sol"
     * government "Republic"
     * attributes "urban"
     * outfits "Hyperdrive"
     * category "Heavy Freighter"
     * near "Sol" 10 20
     * distance 10 20
     */
    std::vector<std::string> lines = {
        "planet \"Earth\"",
        "system \"Sol\"",
        "government \"Republic\"",
        "attributes \"urban\"",
        "outfits \"Hyperdrive\"",
        "category \"Heavy Freighter\"",
        "near \"Sol\" 10 20",
        "distance 10 20"
    };

    /** JSON representation:
     * {
     *     "planet": [
     *         "Earth"
     *     ],
     *     "system": [
     *         "Sol"
     *     ],
     *     "government": [
     *         "Republic"
     *     ],
     *     "attribute_set": [
     *         { "attributes": [ "urban" ]  }
     *     ],
     *     "outfit_set": [
     *         { "outfits": [ "Hyberdrive" ]  }
     *     ],
     *     "category": [
     *         "Heavy Freighter"
     *     ],
     *     near: {
     *         "system": "Sol",
     *         "min": 10,
     *         "max": 20
     *     },
     *     distance: {
     *         "min": 10,
     *         "max": 20
     *     }
     * }
     */
    json expected;
    expected["planet"].emplace_back("Earth");
    expected["system"].emplace_back("Sol");
    expected["government"].emplace_back("Republic");
    json attributes;
    attributes["attributes"].emplace_back("urban");
    expected["attribute_set"].emplace_back(attributes);
    json outfits;
    outfits["outfits"].emplace_back("Hyperdrive");
    expected["outfit_set"].emplace_back(outfits);
    expected["category"].emplace_back("Heavy Freighter");
    json near;
    near["system"] = "Sol";
    near["min"] = 10;
    near["max"] = 20;
    expected["near"] = near;
    json distance;
    distance["min"] = 10;
    distance["max"] = 20;
    expected["distance"] = distance;

    // Run it twice to ensure nodes are stored as a list
    parser.parseFilter(&lines);
    ASSERT_EQ(parser.getData(), expected);
}

TEST_F(FileFilterItemParserTest, TestParseFilterWithModifiedConstraints) {
    /** Text representation:
     * planet "Earth"
     * system "Sol"
     * not government "Republic"
     * not government "Free Worlds"
     * not attributes "urban"
     * not attributes "rich"
     * neighbor outfits "Hyperdrive"
     * neighbor outfits "Ramscoop"
     * neighbor category "Light Warship"
     * near "Sol" 10 20
     * distance 10 20
     */
    std::vector<std::string> lines = {
        "planet \"Earth\"",
        "system \"Sol\"",
        "not government \"Republic\"",
        "not government \"Free Worlds\"",
        "not attributes \"urban\"",
        "not attributes \"rich\"",
        "neighbor outfits \"Hyperdrive\"",
        "neighbor outfits \"Ramscoop\"",
        "neighbor category \"Heavy Freighter\"",
        "neighbor category \"Light Warship\"",
        "near \"Sol\" 10 20",
        "distance 10 20"
    };

    /** JSON representation:
     * {
     *     "planet": [
     *         "Earth"
     *     ],
     *     "system": [
     *         "Sol"
     *     ],
     *     "near": {
     *         "system": "Sol",
     *         "min": 10,
     *         "max": 20
     *     },
     *     "distance": {
     *         "min": 10,
     *         "max": 20
     *     },
     *     "not": [
     *         {
     *             "government": [
     *                 "Republic",
     *                 "Free Worlds"
     *             ],
     *             "attribute_set": [
     *                 { "attributes": [ "urban" ]  },
     *                 { "attributes": [ "rich" ]  }
     *             ]
     *         }
     *     ],
     *     "neighbor": [
     *         {
     *             "category": [
     *                 "Heavy Freighter",
     *                 "Light Warship"
     *             ],
     *             "outfit_set": [
     *                 { "outfits": [ "Hyberdrive" ]  },
     *                 { "outfits": [ "Ramscoop" ]  }
     *             ],
     *         }
     *     }
     * }
     */
    json expected;
    expected["planet"].emplace_back("Earth");
    expected["system"].emplace_back("Sol");
    expected["not"]["government"].emplace_back("Republic");
    expected["not"]["government"].emplace_back("Free Worlds");
    json attributes, attributes2;
    attributes["attributes"].emplace_back("urban");
    attributes2["attributes"].emplace_back("rich");
    expected["not"]["attribute_set"].emplace_back(attributes);
    expected["not"]["attribute_set"].emplace_back(attributes2);
    json outfits, outfits2;
    outfits["outfits"].emplace_back("Hyperdrive");
    outfits2["outfits"].emplace_back("Ramscoop");
    expected["neighbor"]["outfit_set"].emplace_back(outfits);
    expected["neighbor"]["outfit_set"].emplace_back(outfits2);
    expected["neighbor"]["category"].emplace_back("Heavy Freighter");
    expected["neighbor"]["category"].emplace_back("Light Warship");
    json near;
    near["system"] = "Sol";
    near["min"] = 10;
    near["max"] = 20;
    expected["near"] = near;
    json distance;
    distance["min"] = 10;
    distance["max"] = 20;
    expected["distance"] = distance;

    // Run it twice to ensure nodes are stored as a list
    parser.parseFilter(&lines);
    ASSERT_EQ(parser.getData(), expected);
}

TEST_F(FileFilterItemParserTest, TestParsePlanets) {
    // define common variables
    std::string modifier   = "";
    std::string constraint = "planet";

    std::string elem1      = "Earth";
    std::string elem2      = "Luna";
    std::string elem3      = "Mars";
    json constraints = { elem1, elem2, elem3 };

    std::string line1      = constraint + " \"" + elem1 + "\"";
    std::string line2      = "\t\"" + elem2 + "\"";
    std::string line3      = constraint + " \"" + elem3 + "\"";
    std::vector<std::string> lines;

    // test handling for no modifier
    json expected;
    expected[constraint] = constraints;
    lines = { line1, line2 };
    parser.parsePlanets(&lines, modifier);
    lines = { line3 };
    parser.parsePlanets(&lines, modifier);
    ASSERT_EQ(parser.getData(), expected);

    // test handling for "not" modifier
    modifier = "not";
    parser = FileFilterItemParser(minimum_filter_lines);

    json expectedNot;
    expectedNot[modifier][constraint] = constraints;
    lines = { modifier + " " + line1, line2 };
    parser.parsePlanets(&lines, modifier);
    lines = { modifier + " " + line3 };
    parser.parsePlanets(&lines, modifier);
    ASSERT_EQ(parser.getData(), expectedNot);

    // test handling for "neighbor" modifier
    modifier = "neighbor";
    parser = FileFilterItemParser(minimum_filter_lines);

    json expectedNeighbor;
    expectedNeighbor[modifier][constraint] = constraints;
    lines = { modifier + " " + line1, line2 };
    parser.parsePlanets(&lines, modifier);
    lines = { modifier + " " + line3 };
    parser.parsePlanets(&lines, modifier);
    ASSERT_EQ(parser.getData(), expectedNeighbor);
}

TEST_F(FileFilterItemParserTest, TestParseSystems) {
    // define common variables
    std::string modifier   = "";
    std::string constraint = "system";

    std::string elem1      = "Sol";
    std::string elem2      = "Alpha Centauri";
    std::string elem3      = "Wolf 359";
    json constraints = { elem1, elem2, elem3 };

    std::string line1      = constraint + " \"" + elem1 + "\"";
    std::string line2      = "\t\"" + elem2 + "\"";
    std::string line3      = constraint + " \"" + elem3 + "\"";
    std::vector<std::string> lines;

    // test handling for no modifier
    json expected;
    expected[constraint] = constraints;
    lines = { line1, line2 };
    parser.parseSystems(&lines, modifier);
    lines = { line3 };
    parser.parseSystems(&lines, modifier);
    ASSERT_EQ(parser.getData(), expected);

    // test handling for "not" modifier
    modifier = "not";
    parser = FileFilterItemParser(minimum_filter_lines);

    json expectedNot;
    expectedNot[modifier][constraint] = constraints;
    lines = { modifier + " " + line1, line2 };
    parser.parseSystems(&lines, modifier);
    lines = { modifier + " " + line3 };
    parser.parseSystems(&lines, modifier);
    ASSERT_EQ(parser.getData(), expectedNot);

    // test handling for "neighbor" modifier
    modifier = "neighbor";
    parser = FileFilterItemParser(minimum_filter_lines);

    json expectedNeighbor;
    expectedNeighbor[modifier][constraint] = constraints;
    lines = { modifier + " " + line1, line2 };
    parser.parseSystems(&lines, modifier);
    lines = { modifier + " " + line3 };
    parser.parseSystems(&lines, modifier);
    ASSERT_EQ(parser.getData(), expectedNeighbor);
}

TEST_F(FileFilterItemParserTest, TestParseGovernments) {
    // define common variables
    std::string modifier   = "";
    std::string constraint = "government";

    std::string elem1      = "Republic";
    std::string elem2      = "Syndicate";
    std::string elem3      = "Pirate";
    json constraints = { elem1, elem2, elem3 };

    std::string line1      = constraint + " \"" + elem1 + "\"";
    std::string line2      = "\t\"" + elem2 + "\"";
    std::string line3      = constraint + " \"" + elem3 + "\"";
    std::vector<std::string> lines;

    // test handling for no modifier
    json expected;
    expected[constraint] = constraints;
    lines = { line1, line2 };
    parser.parseGovernments(&lines, modifier);
    lines = { line3 };
    parser.parseGovernments(&lines, modifier);
    ASSERT_EQ(parser.getData(), expected);

    // test handling for "not" modifier
    modifier = "not";
    parser = FileFilterItemParser(minimum_filter_lines);

    json expectedNot;
    expectedNot[modifier][constraint] = constraints;
    lines = { modifier + " " + line1, line2 };
    parser.parseGovernments(&lines, modifier);
    lines = { modifier + " " + line3 };
    parser.parseGovernments(&lines, modifier);
    ASSERT_EQ(parser.getData(), expectedNot);

    // test handling for "neighbor" modifier
    modifier = "neighbor";
    parser = FileFilterItemParser(minimum_filter_lines);

    json expectedNeighbor;
    expectedNeighbor[modifier][constraint] = constraints;
    lines = { modifier + " " + line1, line2 };
    parser.parseGovernments(&lines, modifier);
    lines = { modifier + " " + line3 };
    parser.parseGovernments(&lines, modifier);
    ASSERT_EQ(parser.getData(), expectedNeighbor);
}

TEST_F(FileFilterItemParserTest, TestParseAttributes) {
    // define common variables
    std::string modifier   = "";
    std::string group      = "attribute_set";
    std::string constraint = "attributes";

    std::string elem1      = "urban";
    std::string elem2      = "tourism";
    std::string elem3      = "dirt belt";

    json parent, constraint1, constraint2;
    constraint1[constraint] = { elem1, elem2 };
    constraint2[constraint] = { elem3 };
    parent                  = { constraint1, constraint2 };

    std::string line1      = constraint + " \"" + elem1 + "\"";
    std::string line2      = "\t\"" + elem2 + "\"";
    std::string line3      = constraint + " \"" + elem3 + "\"";
    std::vector<std::string> lines;

    // test handling for no modifier
    json expected;
    expected[group] = parent;
    lines = { line1, line2 };
    parser.parseAttributes(&lines, modifier);
    lines = { line3 };
    parser.parseAttributes(&lines, modifier);
    ASSERT_EQ(parser.getData(), expected);

    // test handling for "not" modifier
    modifier = "not";
    parser = FileFilterItemParser(minimum_filter_lines);

    json expectedNot;
    expectedNot[modifier][group] = parent;
    lines = { modifier + " " + line1, line2 };
    parser.parseAttributes(&lines, modifier);
    lines = { modifier + " " + line3 };
    parser.parseAttributes(&lines, modifier);
    ASSERT_EQ(parser.getData(), expectedNot);

    // test handling for "neighbor" modifier
    modifier = "neighbor";
    parser = FileFilterItemParser(minimum_filter_lines);

    json expectedNeighbor;
    expectedNeighbor[modifier][group] = parent;
    lines = { modifier + " " + line1, line2 };
    parser.parseAttributes(&lines, modifier);
    lines = { modifier + " " + line3 };
    parser.parseAttributes(&lines, modifier);
    ASSERT_EQ(parser.getData(), expectedNeighbor);
}

TEST_F(FileFilterItemParserTest, TestParseOutfits) {
    // define common variables
    std::string modifier   = "";
    std::string group      = "outfit_set";
    std::string constraint = "outfits";

    std::string elem1      = "Hyperdrive";
    std::string elem2      = "Jump Drive";
    std::string elem3      = "Ramscoop";

    json parent, constraint1, constraint2;
    constraint1[constraint] = { elem1, elem2 };
    constraint2[constraint] = { elem3 };
    parent                  = { constraint1, constraint2 };

    std::string line1      = constraint + " \"" + elem1 + "\"";
    std::string line2      = "\t\"" + elem2 + "\"";
    std::string line3      = constraint + " \"" + elem3 + "\"";
    std::vector<std::string> lines;

    // test handling for no modifier
    json expected;
    expected[group] = parent;
    lines = { line1, line2 };
    parser.parseOutfits(&lines, modifier);
    lines = { line3 };
    parser.parseOutfits(&lines, modifier);
    ASSERT_EQ(parser.getData(), expected);

    // test handling for "not" modifier
    modifier = "not";
    parser = FileFilterItemParser(minimum_filter_lines);

    json expectedNot;
    expectedNot[modifier][group] = parent;
    lines = { modifier + " " + line1, line2 };
    parser.parseOutfits(&lines, modifier);
    lines = { modifier + " " + line3 };
    parser.parseOutfits(&lines, modifier);
    ASSERT_EQ(parser.getData(), expectedNot);

    // test handling for "neighbor" modifier
    modifier = "neighbor";
    parser = FileFilterItemParser(minimum_filter_lines);

    json expectedNeighbor;
    expectedNeighbor[modifier][group] = parent;
    lines = { modifier + " " + line1, line2 };
    parser.parseOutfits(&lines, modifier);
    lines = { modifier + " " + line3 };
    parser.parseOutfits(&lines, modifier);
    ASSERT_EQ(parser.getData(), expectedNeighbor);
}

TEST_F(FileFilterItemParserTest, TestParseCategories) {
    // define common variables
    std::string modifier   = "";
    std::string constraint = "category";

    std::string elem1      = "Heavy Freighter";
    std::string elem2      = "Light Warship";
    std::string elem3      = "Medium Freighter";
    json constraints = { elem1, elem2, elem3 };

    std::string line1      = constraint + " \"" + elem1 + "\"";
    std::string line2      = "\t\"" + elem2 + "\"";
    std::string line3      = constraint + " \"" + elem3 + "\"";
    std::vector<std::string> lines;

    // test handling for no modifier
    json expected;
    expected[constraint] = constraints;
    lines = { line1, line2 };
    parser.parseCategories(&lines, modifier);
    lines = { line3 };
    parser.parseCategories(&lines, modifier);
    ASSERT_EQ(parser.getData(), expected);

    // test handling for "not" modifier
    modifier = "not";
    parser = FileFilterItemParser(minimum_filter_lines);

    json expectedNot;
    expectedNot[modifier][constraint] = constraints;
    lines = { modifier + " " + line1, line2 };
    parser.parseCategories(&lines, modifier);
    lines = { modifier + " " + line3 };
    parser.parseCategories(&lines, modifier);
    ASSERT_EQ(parser.getData(), expectedNot);

    // test handling for "neighbor" modifier
    modifier = "neighbor";
    parser = FileFilterItemParser(minimum_filter_lines);

    json expectedNeighbor;
    expectedNeighbor[modifier][constraint] = constraints;
    lines = { modifier + " " + line1, line2 };
    parser.parseCategories(&lines, modifier);
    lines = { modifier + " " + line3 };
    parser.parseCategories(&lines, modifier);
    ASSERT_EQ(parser.getData(), expectedNeighbor);
}

TEST_F(FileFilterItemParserTest, TestParseNear) {
    // define common variables
    std::string modifier   = "";
    std::string constraint = "near";
    std::string system     = "Republic";
    int min                = 10;
    int max                = 20;

    json constraints;
    constraints["system"]    = system;

    json constraintsMax      = constraints;
    constraintsMax["max"]    = max;

    json constraintsMinMax   = constraintsMax;
    constraintsMinMax["min"] = min;


    std::string line       = constraint + " \"" + system + "\"";
    std::string lineMax    = line + " " + std::to_string(max);
    std::string lineMinMax = line + " " + std::to_string(min) + " " + std::to_string(max);

    // test handling for no modifier
    json expected, expectedMax, expectedMinMax;
    expected[constraint]       = constraints;
    expectedMax[constraint]    = constraintsMax;
    expectedMinMax[constraint] = constraintsMinMax;

    // vanilla
    parser = FileFilterItemParser(minimum_filter_lines);
    parser.parseNear(line, modifier);
    ASSERT_EQ(parser.getData(), expected);

    // max included
    parser = FileFilterItemParser(minimum_filter_lines);
    parser.parseNear(lineMax, modifier);
    ASSERT_EQ(parser.getData(), expectedMax);

    // min and max included
    parser = FileFilterItemParser(minimum_filter_lines);
    parser.parseNear(lineMinMax, modifier);
    ASSERT_EQ(parser.getData(), expectedMinMax);


    // test handling for "not" modifier
    modifier = "not";
    json expectedNot, expectedNotMax, expectedNotMinMax;
    expectedNot[modifier][constraint]       = constraints;
    expectedNotMax[modifier][constraint]    = constraintsMax;
    expectedNotMinMax[modifier][constraint] = constraintsMinMax;

    // vanilla
    parser = FileFilterItemParser(minimum_filter_lines);
    parser.parseNear(modifier + " " + line, modifier);
    ASSERT_EQ(parser.getData(), expectedNot);

    // max included
    parser = FileFilterItemParser(minimum_filter_lines);
    parser.parseNear(modifier + " " + lineMax, modifier);
    ASSERT_EQ(parser.getData(), expectedNotMax);

    // min and max included
    parser = FileFilterItemParser(minimum_filter_lines);
    parser.parseNear(modifier + " " + lineMinMax, modifier);
    ASSERT_EQ(parser.getData(), expectedNotMinMax);


    // test handling for "neighbor" modifier
    modifier = "neighbor";
    json expectedNeighbor, expectedNeighborMax, expectedNeighborMinMax;
    expectedNeighbor[modifier][constraint]       = constraints;
    expectedNeighborMax[modifier][constraint]    = constraintsMax;
    expectedNeighborMinMax[modifier][constraint] = constraintsMinMax;

    // vanilla
    parser = FileFilterItemParser(minimum_filter_lines);
    parser.parseNear(modifier + " " + line, modifier);
    ASSERT_EQ(parser.getData(), expectedNeighbor);

    // max included
    parser = FileFilterItemParser(minimum_filter_lines);
    parser.parseNear(modifier + " " + lineMax, modifier);
    ASSERT_EQ(parser.getData(), expectedNeighborMax);

    // min and max included
    parser = FileFilterItemParser(minimum_filter_lines);
    parser.parseNear(modifier + " " + lineMinMax, modifier);
    ASSERT_EQ(parser.getData(), expectedNeighborMinMax);
}

TEST_F(FileFilterItemParserTest, TestParseDistance) {
    // define common variables
    std::string modifier   = "";
    std::string constraint = "distance";
    int min                = 10;
    int max                = 20;

    json constraintsMax;
    constraintsMax["max"]    = max;

    json constraintsMinMax   = constraintsMax;
    constraintsMinMax["min"] = min;

    std::string lineMax    = constraint + " " + std::to_string(max);
    std::string lineMinMax = constraint + " " + std::to_string(min) + " " + std::to_string(max);

    // test handling for no modifier
    json expectedMax, expectedMinMax;
    expectedMax[constraint]    = constraintsMax;
    expectedMinMax[constraint] = constraintsMinMax;

    // max included
    parser = FileFilterItemParser(minimum_filter_lines);
    parser.parseDistance(lineMax, modifier);
    ASSERT_EQ(parser.getData(), expectedMax);

    // min and max included
    parser = FileFilterItemParser(minimum_filter_lines);
    parser.parseDistance(lineMinMax, modifier);
    ASSERT_EQ(parser.getData(), expectedMinMax);


    // test handling for "not" modifier
    modifier = "not";
    json expectedNotMax, expectedNotMinMax;
    expectedNotMax[modifier][constraint]    = constraintsMax;
    expectedNotMinMax[modifier][constraint] = constraintsMinMax;

    // max included
    parser = FileFilterItemParser(minimum_filter_lines);
    parser.parseDistance(modifier + " " + lineMax, modifier);
    ASSERT_EQ(parser.getData(), expectedNotMax);

    // min and max included
    parser = FileFilterItemParser(minimum_filter_lines);
    parser.parseDistance(modifier + " " + lineMinMax, modifier);
    ASSERT_EQ(parser.getData(), expectedNotMinMax);


    // test handling for "neighbor" modifier
    modifier = "neighbor";
    json expectedNeighborMax, expectedNeighborMinMax;
    expectedNeighborMax[modifier][constraint]    = constraintsMax;
    expectedNeighborMinMax[modifier][constraint] = constraintsMinMax;

    // max included
    parser = FileFilterItemParser(minimum_filter_lines);
    parser.parseDistance(modifier + " " + lineMax, modifier);
    ASSERT_EQ(parser.getData(), expectedNeighborMax);

    // min and max included
    parser = FileFilterItemParser(minimum_filter_lines);
    parser.parseDistance(modifier + " " + lineMinMax, modifier);
    ASSERT_EQ(parser.getData(), expectedNeighborMinMax);
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
