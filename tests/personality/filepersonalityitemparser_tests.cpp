// SPDX-License-Identifier: GPL-3.0-only
/*
 * filepersonalityitemparser_tests.cpp
 *
 * Copyright (c) 2023, Andrew Sneed <wolfy@shitwolfymakes.com>
 */
#include "filepersonalityitemparser_tests.h"
#include "common/fileitemparserutils.h"

using namespace testing;

namespace parsertests {

TEST_F(FilePersonalityItemParserTest, TestEmptyPersonalityParsing) {
    // declare an empty personality node
    json personality = parser.run();

    json expected;

    ASSERT_EQ(personality, expected);
}

TEST_F(FilePersonalityItemParserTest, TestParsePersonalityTypes) {
    std::vector<std::string> nodeLines = {"personality forbearing\n",
                                          "\ttimid\n"};
    parser.setLines(nodeLines);

    json personality = parser.run();

    json expected;
    expected["types"].emplace_back("forbearing");
    expected["types"].emplace_back("timid");

    ASSERT_EQ(personality, expected);
}

TEST_F(FilePersonalityItemParserTest, TestParsePersonalityTypesWithDuplicates) {
    std::vector<std::string> nodeLines = {"personality forbearing forbearing\n",
                                          "\ttimid timid\n"};
    parser.setLines(nodeLines);

    json personality = parser.run();

    json expected;
    expected["types"].emplace_back("forbearing");
    expected["types"].emplace_back("timid");

    ASSERT_EQ(personality, expected);
}

TEST_F(FilePersonalityItemParserTest, TestParseConfusion) {
    std::vector<std::string> nodeLines = {"personality \n",
                                          "\tconfusion 24\n"};
    parser.setLines(nodeLines);

    json personality = parser.run();

    json expected;
    expected["confusion"] = 24;

    ASSERT_EQ(personality, expected);
}

TEST_F(FilePersonalityItemParserTest, TestParseFullPersonalityNode) {
    std::vector<std::string> nodeLines = {"personality forbearing forbearing heroic\n",
                                          "\ttimid timid daring\n",
                                          "\tconfusion 24"};
    parser.setLines(nodeLines);

    json personality = parser.run();

    json expected;
    expected["types"].emplace_back("forbearing");
    expected["types"].emplace_back("heroic");
    expected["types"].emplace_back("timid");
    expected["types"].emplace_back("daring");
    expected["confusion"] = 24;

    ASSERT_EQ(personality, expected);
}

} // namespace parsertests
