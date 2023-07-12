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
    std::vector<std::string> nodeLines = {EVENT_NODE_HEADER,
                                          "\tunvisit Heaven\n",
                                          "\tunvisit Valhalla\n"};
    parser.setLines(nodeLines);

    json unvisit;
    unvisit.emplace_back("Heaven");
    unvisit.emplace_back("Valhalla");
    json event = parser.run();
    ASSERT_EQ(event["unvisit"], unvisit);
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
    std::vector<std::string> nodeLines = {EVENT_NODE_HEADER,
                                          "\t\"visit planet\" Harambe\n",
                                          "\t\"visit planet\" Uranus\n"};
    parser.setLines(nodeLines);

    json visit;
    visit.emplace_back("Harambe");
    visit.emplace_back("Uranus");
    json event = parser.run();
    ASSERT_EQ(event["visit planet"], visit);
}

TEST_F(FileEventItemParserTest, TestEventUnvisitPlanetParsing) {
    /** JSON representation:
     *  {
     *     "visunvisitit planet": [
     *         "Harambe",
     *         "Uranus"
     *     ]
     *  }
     */
    std::vector<std::string> nodeLines = {EVENT_NODE_HEADER,
                                          "\t\"unvisit planet\" Harambe\n",
                                          "\t\"unvisit planet\" Uranus\n"};
    parser.setLines(nodeLines);

    json unvisit;
    unvisit.emplace_back("Harambe");
    unvisit.emplace_back("Uranus");
    json event = parser.run();
    ASSERT_EQ(event["unvisit planet"], unvisit);
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

    std::vector<std::string> nodeLines = {EVENT_NODE_HEADER,
                                          "\tlink Sol Heaven\n",
                                          "\tlink Sol Heaven\n"};
    parser.setLines(nodeLines);

    json expected, link;
    link["system"] = "Sol";
    link["other"] = "Heaven";
    expected.emplace_back(link);
    expected.emplace_back(link);
    json event = parser.run();
    ASSERT_EQ(event["link"], expected);
}

TEST_F(FileEventItemParserTest, TestEventUnlinkSystemParsing) {
    /** JSON representation:
     *  {
     *     "unlink": [
     *         {
     *             "system": "Sol",
     *             "other": "Heaven"
     *         }
     *     ]
     *  }
     */

    std::vector<std::string> nodeLines = {EVENT_NODE_HEADER,
                                          "\tunlink Sol Heaven\n",
                                          "\tunlink Sol Heaven\n"};
    parser.setLines(nodeLines);

    json expected, unlink;
    unlink["system"] = "Sol";
    unlink["other"] = "Heaven";
    expected.emplace_back(unlink);
    expected.emplace_back(unlink);
    json event = parser.run();
    ASSERT_EQ(event["unlink"], expected);
}

} // namespace parsertests
