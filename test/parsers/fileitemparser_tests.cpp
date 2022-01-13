// SPDX-License-Identifier: GPL-3.0-only
/*
 * fileitemparser_tests.cpp
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "fileitemparser_tests.h"

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
    index = FileItemParser::collectNodeLines(&fileLines, index, &nodeLines);


    ASSERT_EQ(index, 6);
    ASSERT_EQ(nodeLines["node_lines"], expected);
}


} // namespace parsertests
