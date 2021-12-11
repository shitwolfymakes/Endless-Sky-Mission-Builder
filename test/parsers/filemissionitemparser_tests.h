#ifndef FILEMISSIONITEMPARSER_TESTS_H
#define FILEMISSIONITEMPARSER_TESTS_H

#include <gtest/gtest.h>
#include <gmock/gmock.h>

#include "parsers/filemissionitemparser.h"

namespace parsertests {

std::vector<std::string> minimum_mission_node_lines = {"mission \"FileMissionItemParserTest\""};

class FileMissionItemParserTest : public ::testing::Test {
protected:
    FileMissionItemParser parser = FileMissionItemParser(minimum_mission_node_lines);
};

class MissionPriorityParameterizedTestFixture : public FileMissionItemParserTest,
                                                public testing::WithParamInterface<const char*> {
protected:
    FileMissionItemParser parser = FileMissionItemParser(minimum_mission_node_lines);
};

INSTANTIATE_TEST_SUITE_P(FileMissionItemParserTest_MissionPriorityTests,
                        MissionPriorityParameterizedTestFixture,
                        ::testing::Values("priority", "minor"));

class MissionWhereShownParameterizedTestFixture : public FileMissionItemParserTest,
                                                  public testing::WithParamInterface<const char*> {
protected:
    FileMissionItemParser parser = FileMissionItemParser(minimum_mission_node_lines);
};

INSTANTIATE_TEST_SUITE_P(FileMissionItemParserTest_MissionWhereShownTests,
                        MissionWhereShownParameterizedTestFixture,
                        ::testing::Values("job", "landing", "assisting", "boarding"));

} // namespace parsertests

#endif // FILEMISSIONITEMPARSER_TESTS_H
