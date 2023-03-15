// SPDX-License-Identifier: GPL-3.0-only
/*
 * fileeventitemparser_tests.cpp
 *
 * Copyright (c) 2023, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "fileeventitemparser_tests.h"

using namespace testing;

namespace parsertests {

// Test top level field parsing
TEST_F(FileEventItemParserTest, TestEventParsing) {
    // TODO: Implement this
    ASSERT_EQ(0, 0);
}

TEST_F(FileEventItemParserTest, TestEventDateParsing) {
    /** JSON representation:
     *  {
     *     "date": {
     *         "day": 4,
     *         "month": 20,
     *         "year": 69
     *     }
     *  }
     */
    std::vector<std::string> tokens = {"date", "4", "20", "69"};
    json date;
    date["day"] = 4;
    date["month"] = 20;
    date["year"] = 69;

    parser.parseDate(tokens);
    ASSERT_EQ(parser.getData()["date"], date);
}

TEST_F(FileEventItemParserTest, TestEventVisitSystemParsing) {
    /** JSON representation:
     *  {
     *     "visit": [
     *         "Heaven",
     *         "Valhalla"
     *     ]
     *  }
     */
    json visit;

    // test single instance
    visit.emplace_back("Heaven");
    parser.parseVisitSystem("Heaven");
    ASSERT_EQ(parser.getData()["visit"], visit);

    // test multiple instance
    visit.emplace_back("Valhalla");
    parser.parseVisitSystem("Valhalla");
    ASSERT_EQ(parser.getData()["visit"], visit);
}

TEST_F(FileEventItemParserTest, TestEventUnvisitSystemParsing) {
    /** JSON representation:
     *  {
     *     "unvisit": [
     *         "Heaven",
     *         "Valhalla"
     *     ]
     *  }
     */
    json unvisit;

    // test single instance
    unvisit.emplace_back("Heaven");
    parser.parseUnvisitSystem("Heaven");
    ASSERT_EQ(parser.getData()["unvisit"], unvisit);

    // test multiple instance
    unvisit.emplace_back("Valhalla");
    parser.parseUnvisitSystem("Valhalla");
    ASSERT_EQ(parser.getData()["unvisit"], unvisit);
}

TEST_F(FileEventItemParserTest, TestEventVisitPlanetParsing) {
    /** JSON representation:
     *  {
     *     "visit planet": [
     *         "Harambe",
     *         "Uranus"
     *     ]
     *  }
     */
    json visit;

    // test single instance
    visit.emplace_back("Harambe");
    parser.parseVisitPlanet("Harambe");
    ASSERT_EQ(parser.getData()["visit planet"], visit);

    // test multiple instance
    visit.emplace_back("Uranus");
    parser.parseVisitPlanet("Uranus");
    ASSERT_EQ(parser.getData()["visit planet"], visit);
}

TEST_F(FileEventItemParserTest, TestEventUnvisitPlanetParsing) {
    /** JSON representation:
     *  {
     *     "unvisit planet": [
     *         "Harambe",
     *         "Uranus"
     *     ]
     *  }
     */
    json unvisit;

    // test single instance
    unvisit.emplace_back("Harambe");
    parser.parseUnvisitPlanet("Harambe");
    ASSERT_EQ(parser.getData()["unvisit planet"], unvisit);

    // test multiple instance
    unvisit.emplace_back("Uranus");
    parser.parseUnvisitPlanet("Uranus");
    ASSERT_EQ(parser.getData()["unvisit planet"], unvisit);
}

} // namespace parsertests
