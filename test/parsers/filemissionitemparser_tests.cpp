// SPDX-License-Identifier: GPL-3.0-only
/*
 * filemissionitemparser_tests.cpp
 *
 * Copyright (c) 2021, Andrew Sneed <wolfy@shitwolfymakes.com>
 */
#include "filemissionitemparser_tests.h"

using namespace testing;

namespace parsertests {

// Test top level field parsing
TEST_F(FileMissionItemParserTest, StoreEngineMissionId) {
    std::vector<std::string> tokens = {"mission", "FileMissionItemParserTest"};
    parser.parseId(tokens);
    ASSERT_EQ(parser.get_mission()["id"], "FileMissionItemParserTest");
}

TEST_F(FileMissionItemParserTest, StoreMissionName) {
    std::vector<std::string> tokens = {"name", "Mission 1"};
    parser.parseName(tokens);
    ASSERT_EQ(parser.get_mission()["name"], "Mission 1");
}

TEST_F(FileMissionItemParserTest, StoreMissionDescription) {
    std::vector<std::string> tokens = {"description", "A test mission"};
    parser.parseDescription(tokens);
    ASSERT_EQ(parser.get_mission()["description"], "A test mission");
}

TEST_F(FileMissionItemParserTest, StoreMissionBlocked) {
    std::vector<std::string> tokens = {"blocked", "Oh piss off!"};
    parser.parseBlocked(tokens);
    ASSERT_EQ(parser.get_mission()["blocked"], "Oh piss off!");
}

TEST_F(FileMissionItemParserTest, StoreMissionDeadlineContainingDaysAndMultiplier) {
    std::vector<std::string> tokens = {"deadline", "2", "1"};
    json deadline;
    deadline["is_active"] = true;
    deadline["days"] = 2;
    deadline["multiplier"] = 1;

    parser.parseDeadline(tokens);
    ASSERT_EQ(parser.get_mission()["deadline"].dump(), deadline.dump());
}

TEST_F(FileMissionItemParserTest, StoreMissionDeadlineContainingDays) {
    std::vector<std::string> tokens = {"deadline", "2"};
    json deadline;
    deadline["is_active"] = true;
    deadline["days"] = 2;

    parser.parseDeadline(tokens);
    ASSERT_EQ(parser.get_mission()["deadline"].dump(), deadline.dump());
}

TEST_F(FileMissionItemParserTest, StoreMissionDeadlineOnly) {
    std::vector<std::string> tokens = {"deadline"};
    json deadline;
    deadline["is_active"] = true;

    parser.parseDeadline(tokens);
    ASSERT_EQ(parser.get_mission()["deadline"].dump(), deadline.dump());
}

TEST_F(FileMissionItemParserTest, StoreMissionCargoContainingCargoAndTonnageAndRangeAndProbability) {
    std::vector<std::string> tokens = {"cargo", "food", "5", "2", "0.1"};
    json cargo;
    cargo["cargo"] = "food";
    cargo["tonnage"] = 5;
    cargo["tonnage_range"] = 2;
    cargo["probability"] = 0.1;

    parser.parseCargo(tokens);
    ASSERT_EQ(parser.get_mission()["cargo"].dump(), cargo.dump());
}

TEST_F(FileMissionItemParserTest, StoreMissionCargoContainingCargoAndTonnageAndRange) {
    std::vector<std::string> tokens = {"cargo", "food", "5", "2"};
    json cargo;
    cargo["cargo"] = "food";
    cargo["tonnage"] = 5;
    cargo["tonnage_range"] = 2;

    parser.parseCargo(tokens);
    ASSERT_EQ(parser.get_mission()["cargo"].dump(), cargo.dump());
}

TEST_F(FileMissionItemParserTest, StoreMissionCargoContainingCargoAndTonnage) {
    std::vector<std::string> tokens = {"cargo", "food", "5"};
    json cargo;
    cargo["cargo"] = "food";
    cargo["tonnage"] = 5;

    parser.parseCargo(tokens);
    ASSERT_EQ(parser.get_mission()["cargo"].dump(), cargo.dump());
}

TEST_F(FileMissionItemParserTest, StoreMissionPassengersContainingPassengersAndRangeAndProbability) {
    std::vector<std::string> tokens = {"passengers", "10", "5", "0.2"};
    json passengers;
    passengers["passengers"] = 10;
    passengers["passengers_range"] = 5;
    passengers["probability"] = 0.2;

    parser.parsePassengers(tokens);
    ASSERT_EQ(parser.get_mission()["passengers"].dump(), passengers.dump());
}

TEST_F(FileMissionItemParserTest, StoreMissionPassengersContainingPassengersAndRange) {
    std::vector<std::string> tokens = {"passengers", "10", "5"};
    json passengers;
    passengers["passengers"] = 10;
    passengers["passengers_range"] = 5;

    parser.parsePassengers(tokens);
    ASSERT_EQ(parser.get_mission()["passengers"].dump(), passengers.dump());
}

TEST_F(FileMissionItemParserTest, StoreMissionPassengersContainingPassengers) {
    std::vector<std::string> tokens = {"passengers", "10"};
    json passengers;
    passengers["passengers"] = 10;

    parser.parsePassengers(tokens);
    ASSERT_EQ(parser.get_mission()["passengers"].dump(), passengers.dump());
}

TEST_F(FileMissionItemParserTest, StoreMissionIllegalContainingFineAndMessage) {
    std::vector<std::string> tokens = {"illegal", "50", "Soviet citizens need no food comrade"};
    json illegal;
    illegal["fine"] = 50;
    illegal["message"] = "Soviet citizens need no food comrade";

    parser.parseIllegal(tokens);
    ASSERT_EQ(parser.get_mission()["illegal"].dump(), illegal.dump());
}

TEST_F(FileMissionItemParserTest, StoreMissionIllegalContainingFine) {
    std::vector<std::string> tokens = {"illegal", "50"};
    json illegal;
    illegal["fine"] = 50;

    parser.parseIllegal(tokens);
    ASSERT_EQ(parser.get_mission()["illegal"].dump(), illegal.dump());
}

TEST_F(FileMissionItemParserTest, StoreMissionStealthFlag) {
    parser.parseStealth();
    ASSERT_EQ(parser.get_mission()["stealth"], true);
}

TEST_F(FileMissionItemParserTest, StoreMissionInvisibleFlag) {
    parser.parseInvisible();
    ASSERT_EQ(parser.get_mission()["invisible"], true);
}

TEST_P(MissionPriorityParameterizedTestFixture, StoreMissionPriorityLevel) {
    parser.parsePriorityLevel(GetParam());
    ASSERT_EQ(parser.get_mission()["priority_level"], GetParam());
}

TEST_P(MissionWhereShownParameterizedTestFixture, StoreMissionWhereShown) {
    parser.parseWhereShown(GetParam());
    ASSERT_EQ(parser.get_mission()["where_shown"], GetParam());
}

TEST_F(FileMissionItemParserTest, StoreMissionRepeatContainingAmount) {
    std::vector<std::string> tokens = {"repeat", "5"};
    json repeat;
    repeat["is_active"] = true;
    repeat["amount"] = 5;

    parser.parseRepeat(tokens);
    ASSERT_EQ(parser.get_mission()["repeat"].dump(), repeat.dump());
}

TEST_F(FileMissionItemParserTest, StoreMissionRepeatOnly) {
    std::vector<std::string> tokens = {"repeat"};
    json repeat;
    repeat["is_active"] = true;

    parser.parseRepeat(tokens);
    ASSERT_EQ(parser.get_mission()["repeat"].dump(), repeat.dump());
}

TEST_F(FileMissionItemParserTest, StoreMissionClearanceContainingMessage) {
    std::vector<std::string> tokens = {"clearance", "You're on the list"};
    json clearance;
    clearance["is_active"] = true;
    clearance["message"] = "You're on the list";

    parser.parseClearance(tokens);
    ASSERT_EQ(parser.get_mission()["clearance"].dump(), clearance.dump());
}

TEST_F(FileMissionItemParserTest, StoreMissionClearanceOnly) {
    std::vector<std::string> tokens = {"clearance"};
    json clearance;
    clearance["is_active"] = true;

    parser.parseClearance(tokens);
    ASSERT_EQ(parser.get_mission()["clearance"].dump(), clearance.dump());
}

TEST_F(FileMissionItemParserTest, StoreMissionInfiltratingFlag) {
    parser.parseInfiltrating();
    ASSERT_EQ(parser.get_mission()["infiltrating"], true);
}

TEST_F(FileMissionItemParserTest, StoreMissionWaypointWithSystem) {
    std::string token = "Sol";
    json expected;
    json waypoint;
    waypoint["system"] = "Sol";
    expected.emplace_back(waypoint);

    parser.parseWaypoint(token);
    ASSERT_EQ(parser.get_mission()["waypoints"].dump(), expected.dump());
}

TEST_F(FileMissionItemParserTest, StoreMissionStopoverWithSystem) {
    std::string token = "Earth";
    json expected;
    json stopover;
    stopover["planet"] = "Earth";
    expected.emplace_back(stopover);

    parser.parseStopover(token);
    ASSERT_EQ(parser.get_mission()["stopovers"].dump(), expected.dump());
}

TEST_F(FileMissionItemParserTest, StoreMissionSourceWithPlanet) {
    parser.parseSource("Earth");
    ASSERT_EQ(parser.get_mission()["source"], "Earth");
}

TEST_F(FileMissionItemParserTest, StoreMissionDestinationWithPlanet) {
    parser.parseDestination("Delve");
    ASSERT_EQ(parser.get_mission()["destination"], "Delve");
}


// Test trigger parsing
//TEST_F(FileMissionItemParserTest, StoreMissionTrigger) {}

TEST_F(FileMissionItemTriggerParserTest, StoreTriggerLogWithCategoryAndHeaderAndText) {
    std::vector<std::string> tokens = {"log", "People", "Yo mama", "is a ho"};
    json expected;
    json log;
    log["category"] = "People";
    log["header"] = "Yo mama";
    log["text"] = "is a ho";
    expected.emplace_back(log);

    parser.parseLog(tokens, &trigger);
    ASSERT_EQ(trigger["logs"].dump(), expected.dump());
}

TEST_F(FileMissionItemTriggerParserTest, StoreTriggerLogWithText) {
    std::string token = "my mama ain't a ho";
    json expected;
    json log;
    log["text"] = "my mama ain't a ho";
    expected.emplace_back(log);

    parser.parseLog(token, &trigger);
    ASSERT_EQ(trigger["logs"].dump(), expected.dump());
}

TEST_F(FileMissionItemTriggerParserTest, StoreTriggerDialogPhrase) {
    json expected;
    expected.emplace_back("Harambe 1");

    int index = 0;
    std::vector<std::string> lines = minimum_mission_node_lines;
    lines.emplace_back("\t\tdialog phrase \"Harambe 1\"");

    index = parser.parseDialog(&lines, 1, &trigger);
    ASSERT_EQ(index, 1);
    ASSERT_EQ(trigger["dialog_phrase"].dump(), expected.dump());
}



//TEST_F(FileMissionItemTriggerParserTest, StoreTriggerConvoWithoutParsing) {}



} // namespace parsertests
