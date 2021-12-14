#ifndef FILEMISSIONITEMPARSER_TESTS_H
#define FILEMISSIONITEMPARSER_TESTS_H

#include <gtest/gtest.h>
#include <gmock/gmock.h>

#include "parsers/filemissionitemparser.h"

namespace parsertests {

std::vector<std::string> minimum_mission_node_lines = {"mission \"FileMissionItemParserTest\""};

// Fixture for testing a mission's top level fields
class FileMissionItemParserTest : public ::testing::Test {
protected:
    FileMissionItemParser parser = FileMissionItemParser(minimum_mission_node_lines);
};


// Fixture for testing the types of mission priorities
class MissionPriorityParameterizedTestFixture : public FileMissionItemParserTest,
                                                public testing::WithParamInterface<const char*> {
protected:
    FileMissionItemParser parser = FileMissionItemParser(minimum_mission_node_lines);
};

INSTANTIATE_TEST_SUITE_P(FileMissionItemParserTest_MissionPriorityTests,
                        MissionPriorityParameterizedTestFixture,
                        ::testing::Values("priority", "minor"));


// Fixture for testing the types of mission showing locations
class MissionWhereShownParameterizedTestFixture : public FileMissionItemParserTest,
                                                  public testing::WithParamInterface<const char*> {
protected:
    FileMissionItemParser parser = FileMissionItemParser(minimum_mission_node_lines);
};

INSTANTIATE_TEST_SUITE_P(FileMissionItemParserTest_MissionWhereShownTests,
                        MissionWhereShownParameterizedTestFixture,
                        ::testing::Values("job", "landing", "assisting", "boarding"));


// Fixture for testing a mission trigger
class FileMissionItemTriggerParserTest : public FileMissionItemParserTest {
protected:
    json trigger;
};

} // namespace parsertests

#endif // FILEMISSIONITEMPARSER_TESTS_H
