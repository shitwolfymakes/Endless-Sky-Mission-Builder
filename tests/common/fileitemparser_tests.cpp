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

TEST_F(FileItemParserTest, TestTokenize) {
    std::vector<std::string> result;
    result = FileItemParserUtils::tokenize("Hello");
    ASSERT_THAT(result, ElementsAre("Hello"));

    result = FileItemParserUtils::tokenize("\tHello World");
    ASSERT_THAT(result, ElementsAre("Hello", "World"));

    result = FileItemParserUtils::tokenize("Test \"Hello World\"");
    ASSERT_THAT(result, ElementsAre("Test", "Hello World"));

    result = FileItemParserUtils::tokenize("Test `Hello World`");
    ASSERT_THAT(result, ElementsAre("Test", "Hello World"));
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

TEST_F(FileItemParserTest, TestCollectNodeLines) {
    int index = 1;
    std::vector<std::string> fileLines = {"mission \"TestCollectNodeLines\"\n",
                                          "\tsubstitutions\n",
                                          "\t\t\"<title>\" \"Bossmang\"\n",
                                          "\t\t\"<title>\" \"Inner\"\n",
                                          "\t\t\t\"reputation: Inyalowda\" > 100\n",
                                          "\t\t\t\"reputation: Beltalowda\" < 100\n",
                                          "\t\t\"<name>\" \"Anderson Dawes\"\n",
                                          "\tinfiltrating\n"};

    json expected;
    expected = {"\tsubstitutions\n",
                "\t\t\"<title>\" \"Bossmang\"\n",
                "\t\t\"<title>\" \"Inner\"\n",
                "\t\t\t\"reputation: Inyalowda\" > 100\n",
                "\t\t\t\"reputation: Beltalowda\" < 100\n",
                "\t\t\"<name>\" \"Anderson Dawes\"\n"};

    json nodeLines;
    index = FileItemParserUtils::collectNodeLines(&fileLines, index, &nodeLines);


    ASSERT_EQ(index, 6);
    ASSERT_EQ(nodeLines, expected);
}

TEST_F(FileItemParserTest, TestCollectNodeLinesStrList) {
    int index = 1;
    std::vector<std::string> fileLines = {"mission \"TestCollectNodeLines\"\n",
                                          "\tsubstitutions\n",
                                          "\t\t\"<title>\" \"Bossmang\"\n",
                                          "\t\t\"<title>\" \"Inner\"\n",
                                          "\t\t\t\"reputation: Inyalowda\" > 100\n",
                                          "\t\t\t\"reputation: Beltalowda\" < 100\n",
                                          "\t\t\"<name>\" \"Anderson Dawes\"\n"};

    std::vector<std::string> expected;
    expected = {"\tsubstitutions\n",
                "\t\t\"<title>\" \"Bossmang\"\n",
                "\t\t\"<title>\" \"Inner\"\n",
                "\t\t\t\"reputation: Inyalowda\" > 100\n",
                "\t\t\t\"reputation: Beltalowda\" < 100\n",
                "\t\t\"<name>\" \"Anderson Dawes\"\n"};

    std::vector<std::string> nodeLines;
    index = FileItemParserUtils::collectNodeLines(&fileLines, index, &nodeLines);


    ASSERT_EQ(index, 6);
    ASSERT_EQ(nodeLines, expected);
}

} // namespace parsertests
