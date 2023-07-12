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
    std::vector<std::string> nodeLines = {EVENT_NODE_HEADER,
                                          "\tdate 4 20 69\n"};
    parser.setLines(nodeLines);

    json date;
    date["day"] = 4;
    date["month"] = 20;
    date["year"] = 69;

    json event = parser.run();
    ASSERT_EQ(event["date"], date);
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
    std::vector<std::string> nodeLines = {EVENT_NODE_HEADER,
                                          "\tvisit Heaven\n",
                                          "\tvisit Valhalla\n"};
    parser.setLines(nodeLines);

    json visit;
    visit.emplace_back("Heaven");
    visit.emplace_back("Valhalla");
    json event = parser.run();
    ASSERT_EQ(event["visit"], visit);
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

TEST_F(FileEventItemParserTest, TestEventLinkSystemParsing) {
    /** JSON representation:
     *  {
     *     "link": [
     *         {
     *             "system": "Sol",
     *             "other": "Heaven"
     *         }
     *     ]
     *  }
     */
    std::vector<std::string> tokens = {"link", "Sol", "Heaven"};
    json event, link;

    // test single instance
    link["system"] = "Sol";
    link["other"] = "Heaven";
    event.emplace_back(link);
    parser.parseLink(tokens);
    ASSERT_EQ(parser.getData()["link"], event);

    // test multiple instances
    event.emplace_back(link);
    parser.parseLink(tokens);
    ASSERT_EQ(parser.getData()["link"], event);
}

TEST_F(FileEventItemParserTest, TestEventUnlinkSystemParsing) {
    /** JSON representation:
     *  {
     *     "unlink": [
     *         {
     *             "system": "Heaven",
     *             "other": "Sol"
     *         }
     *     ]
     *  }
     */
    std::vector<std::string> tokens = {"link", "Heaven", "Sol"};
    json event, unlink;

    // test single instance
    unlink["system"] = "Heaven";
    unlink["other"] = "Sol";
    event.emplace_back(unlink);
    parser.parseUnlink(tokens);
    ASSERT_EQ(parser.getData()["unlink"], event);

    // test multiple instances
    event.emplace_back(unlink);
    parser.parseUnlink(tokens);
    ASSERT_EQ(parser.getData()["unlink"], event);
}

} // namespace parsertests
