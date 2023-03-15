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
    ASSERT_EQ(0, 1);
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
    std::string token = "Heaven";
    json visit;
    visit.emplace_back("Heaven");

    // test single instance
    parser.parseVisitSystem(token);
    ASSERT_EQ(parser.getData()["visit"], visit);

}

} // namespace parsertests
