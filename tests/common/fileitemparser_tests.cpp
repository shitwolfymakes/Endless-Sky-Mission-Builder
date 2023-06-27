// SPDX-License-Identifier: GPL-3.0-only
/*
 * fileitemparser_tests.cpp
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "fileitemparser_tests.h"

#include "nlohmann/json.hpp"
using json = nlohmann::json;

#include "common/fileitemparserutils.h"

using namespace testing;

namespace parsertests {

// Test top level field parsing
TEST_F(FileItemParserTest, TestCollectNodeLines) {
    int index = 1;
    std::vector<std::string> fileLines = {"mission \"TestCollectNodeLines\"",
                                          "\tsubstitutions",
                                          "\t\t\"<title>\" \"Bossmang\"",
                                          "\t\t\"<title>\" \"Inner\"",
                                          "\t\t\t\"reputation: Inyalowda\" > 100",
                                          "\t\t\t\"reputation: Beltalowda\" < 100",
                                          "\t\t\"<name>\" \"Anderson Dawes\"",
                                          "\tinfiltrating"};

    json expected;
    expected = {"\tsubstitutions",
                "\t\t\"<title>\" \"Bossmang\"",
                "\t\t\"<title>\" \"Inner\"",
                "\t\t\t\"reputation: Inyalowda\" > 100",
                "\t\t\t\"reputation: Beltalowda\" < 100",
                "\t\t\"<name>\" \"Anderson Dawes\""};

    json nodeLines;
    index = FileItemParserUtils::collectNodeLines(&fileLines, index, &nodeLines);


    ASSERT_EQ(index, 6);
    ASSERT_EQ(nodeLines, expected);
}

TEST_F(FileItemParserTest, TestGetIndentLevel) {
    int result = FileItemParserUtils::getIndentLevel("Hello");
    ASSERT_EQ(result, 0);

    result = FileItemParserUtils::getIndentLevel("\tHello");
    ASSERT_EQ(result, 1);

    result = FileItemParserUtils::getIndentLevel("\t\tHello");
    ASSERT_EQ(result, 2);
}

TEST_F(FileItemParserTest, TestIs) {
    bool result = FileItemParserUtils::is("Hello", "Hello");
    ASSERT_TRUE(result);

    result = FileItemParserUtils::is("Hello", "World");
    ASSERT_FALSE(result);
}

} // namespace parsertests
