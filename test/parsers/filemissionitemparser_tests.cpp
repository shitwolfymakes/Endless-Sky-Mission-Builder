// SPDX-License-Identifier: GPL-3.0-only
/*
 * filemissionitemparser_tests.cpp
 *
 * Copyright (c) 2021, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include <gtest/gtest.h>
#include <gmock/gmock.h>

#include "parsers/filemissionitemparser.h"

using namespace testing;

namespace parsertests {

class FileMissionItemParserTest : public ::testing::Test {
protected:
    std::vector<std::string> minimum_mission_node_lines = {"mission \"FileMissionItemParserTest\""};
    FileMissionItemParser parser = FileMissionItemParser(minimum_mission_node_lines);
};

TEST_F(FileMissionItemParserTest, StoreEngineMissionId)
{
    std::vector<std::string> tokens = {"mission", "FileMissionItemParserTest"};
    parser.parseId(tokens);
    ASSERT_THAT(parser.get_mission()["id"], "FileMissionItemParserTest");
}

TEST_F(FileMissionItemParserTest, StoreMissionName)
{
    std::vector<std::string> tokens = {"name", "Mission 1"};
    parser.parseName(tokens);
    ASSERT_THAT(parser.get_mission()["name"], "Mission 1");
}

TEST_F(FileMissionItemParserTest, StoreMissionDescription)
{
    std::vector<std::string> tokens = {"description", "A test mission"};
    parser.parseDescription(tokens);
    ASSERT_THAT(parser.get_mission()["description"], "A test mission");
}

TEST_F(FileMissionItemParserTest, StoreMissionBlocked)
{
    std::vector<std::string> tokens = {"blocked", "Oh piss off!"};
    parser.parseBlocked(tokens);
    ASSERT_THAT(parser.get_mission()["blocked"], "Oh piss off!");
}

} // namespace parsertests
