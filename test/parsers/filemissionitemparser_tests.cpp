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
    ASSERT_EQ(parser.get_mission()["deadline"], deadline);
}

TEST_F(FileMissionItemParserTest, StoreMissionDeadlineContainingDays) {
    std::vector<std::string> tokens = {"deadline", "2"};
    json deadline;
    deadline["is_active"] = true;
    deadline["days"] = 2;

    parser.parseDeadline(tokens);
    ASSERT_EQ(parser.get_mission()["deadline"], deadline);
}

TEST_F(FileMissionItemParserTest, StoreMissionDeadlineOnly) {
    std::vector<std::string> tokens = {"deadline"};
    json deadline;
    deadline["is_active"] = true;

    parser.parseDeadline(tokens);
    ASSERT_EQ(parser.get_mission()["deadline"], deadline);
}

TEST_F(FileMissionItemParserTest, StoreMissionCargoContainingCargoAndTonnageAndRangeAndProbability) {
    std::vector<std::string> tokens = {"cargo", "food", "5", "2", "0.1"};
    json cargo;
    cargo["cargo"] = "food";
    cargo["tonnage"] = 5;
    cargo["tonnage_range"] = 2;
    cargo["probability"] = 0.1;

    parser.parseCargo(tokens);
    ASSERT_EQ(parser.get_mission()["cargo"], cargo);
}

TEST_F(FileMissionItemParserTest, StoreMissionCargoContainingCargoAndTonnageAndRange) {
    std::vector<std::string> tokens = {"cargo", "food", "5", "2"};
    json cargo;
    cargo["cargo"] = "food";
    cargo["tonnage"] = 5;
    cargo["tonnage_range"] = 2;

    parser.parseCargo(tokens);
    ASSERT_EQ(parser.get_mission()["cargo"], cargo);
}

TEST_F(FileMissionItemParserTest, StoreMissionCargoContainingCargoAndTonnage) {
    std::vector<std::string> tokens = {"cargo", "food", "5"};
    json cargo;
    cargo["cargo"] = "food";
    cargo["tonnage"] = 5;

    parser.parseCargo(tokens);
    ASSERT_EQ(parser.get_mission()["cargo"], cargo);
}

TEST_F(FileMissionItemParserTest, StoreMissionPassengersContainingPassengersAndRangeAndProbability) {
    std::vector<std::string> tokens = {"passengers", "10", "5", "0.2"};
    json passengers;
    passengers["passengers"] = 10;
    passengers["passengers_range"] = 5;
    passengers["probability"] = 0.2;

    parser.parsePassengers(tokens);
    ASSERT_EQ(parser.get_mission()["passengers"], passengers);
}

TEST_F(FileMissionItemParserTest, StoreMissionPassengersContainingPassengersAndRange) {
    std::vector<std::string> tokens = {"passengers", "10", "5"};
    json passengers;
    passengers["passengers"] = 10;
    passengers["passengers_range"] = 5;

    parser.parsePassengers(tokens);
    ASSERT_EQ(parser.get_mission()["passengers"], passengers);
}

TEST_F(FileMissionItemParserTest, StoreMissionPassengersContainingPassengers) {
    std::vector<std::string> tokens = {"passengers", "10"};
    json passengers;
    passengers["passengers"] = 10;

    parser.parsePassengers(tokens);
    ASSERT_EQ(parser.get_mission()["passengers"], passengers);
}

TEST_F(FileMissionItemParserTest, StoreMissionIllegalContainingFineAndMessage) {
    std::vector<std::string> tokens = {"illegal", "50", "Soviet citizens need no food comrade"};
    json illegal;
    illegal["fine"] = 50;
    illegal["message"] = "Soviet citizens need no food comrade";

    parser.parseIllegal(tokens);
    ASSERT_EQ(parser.get_mission()["illegal"], illegal);
}

TEST_F(FileMissionItemParserTest, StoreMissionIllegalContainingFine) {
    std::vector<std::string> tokens = {"illegal", "50"};
    json illegal;
    illegal["fine"] = 50;

    parser.parseIllegal(tokens);
    ASSERT_EQ(parser.get_mission()["illegal"], illegal);
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
    ASSERT_EQ(parser.get_mission()["repeat"], repeat);
}

TEST_F(FileMissionItemParserTest, StoreMissionRepeatOnly) {
    std::vector<std::string> tokens = {"repeat"};
    json repeat;
    repeat["is_active"] = true;

    parser.parseRepeat(tokens);
    ASSERT_EQ(parser.get_mission()["repeat"], repeat);
}

TEST_F(FileMissionItemParserTest, StoreMissionClearanceContainingMessage) {
    std::vector<std::string> tokens = {"clearance", "You're on the list"};
    json clearance;
    clearance["is_active"] = true;
    clearance["message"] = "You're on the list";

    parser.parseClearance(tokens);
    ASSERT_EQ(parser.get_mission()["clearance"], clearance);
}

TEST_F(FileMissionItemParserTest, StoreMissionClearanceOnly) {
    std::vector<std::string> tokens = {"clearance"};
    json clearance;
    clearance["is_active"] = true;

    parser.parseClearance(tokens);
    ASSERT_EQ(parser.get_mission()["clearance"], clearance);
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
    ASSERT_EQ(parser.get_mission()["waypoints"], expected);
}

TEST_F(FileMissionItemParserTest, StoreMissionStopoverWithSystem) {
    std::string token = "Earth";
    json expected;
    json stopover;
    stopover["planet"] = "Earth";
    expected.emplace_back(stopover);

    parser.parseStopover(token);
    ASSERT_EQ(parser.get_mission()["stopovers"], expected);
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
    ASSERT_EQ(trigger["logs"], expected);
}

TEST_F(FileMissionItemTriggerParserTest, StoreTriggerLogWithText) {
    std::string token = "my mama ain't a ho";
    json expected;
    json log;
    log["text"] = "my mama ain't a ho";
    expected.emplace_back(log);

    parser.parseLog(token, &trigger);
    ASSERT_EQ(trigger["logs"], expected);
}

TEST_F(FileMissionItemTriggerParserTest, StoreTriggerDialogPhrase) {
    json dialoguePhrase;
    dialoguePhrase.emplace_back("Harambe 1");

    int index = 0;
    std::vector<std::string> lines = minimum_trigger_node_lines;
    lines.emplace_back("\t\tdialog phrase \"Harambe 1\"");

    index = parser.parseDialog(&lines, 1, &trigger);
    ASSERT_EQ(index, 1);
    ASSERT_EQ(trigger["dialog_phrase"], dialoguePhrase);
}

TEST_F(FileMissionItemTriggerParserTest, StoreTriggerDialogSingleLine) {
    json expected;
    json dialogLines;
    dialogLines.emplace_back("It is Wednesday my dudes");
    expected.emplace_back(dialogLines);

    int index = 0;
    std::vector<std::string> lines = minimum_trigger_node_lines;
    lines.emplace_back("\t\tdialog `It is Wednesday my dudes`");

    index = parser.parseDialog(&lines, 1, &trigger);
    ASSERT_EQ(index, 1);
    ASSERT_EQ(trigger["dialog"], expected);
}

TEST_F(FileMissionItemTriggerParserTest, StoreTriggerDialogMutlipleLines) {
    json expected;
    json dialogLines;
    dialogLines.emplace_back("It's flat fuck friday");
    dialogLines.emplace_back("You fucking losers");
    expected.emplace_back(dialogLines);

    int index = 0;
    std::vector<std::string> lines = minimum_trigger_node_lines;
    lines.emplace_back("\t\tdialog `It's flat fuck friday`");
    lines.emplace_back("\t\t\t`\tYou fucking losers`");

    index = parser.parseDialog(&lines, 1, &trigger);
    ASSERT_EQ(index, 2);
    ASSERT_EQ(trigger["dialog"], expected);
}

//TEST_F(FileMissionItemTriggerParserTest, StoreTriggerConvoWithoutParsing) {}

TEST_F(FileMissionItemTriggerParserTest, StoreTriggerOutfitContainingNameAndQuantity) {
    std::vector<std::string> tokens = {"outfit", "Skylance V", "5"};
    json expected;
    json outfit;
    outfit["name"] = "Skylance V";
    outfit["quantity"] = 5;
    expected.emplace_back(outfit);

    parser.parseOutfit(tokens, &trigger);
    ASSERT_EQ(trigger["outfits"], expected);
}

TEST_F(FileMissionItemTriggerParserTest, StoreTriggerOutfitContainingName) {
    std::vector<std::string> tokens = {"outfit", "Skylance V"};
    json expected;
    json outfit;
    outfit["name"] = "Skylance V";
    expected.emplace_back(outfit);

    parser.parseOutfit(tokens, &trigger);
    ASSERT_EQ(trigger["outfits"], expected);
}

TEST_F(FileMissionItemTriggerParserTest, StoreTriggerOutfitDeprecated) {
    // outfit <outfit> 0 is deprecated, replaced by require <outfit>
    // test silent fix on file ingest
    std::vector<std::string> tokens = {"outfit", "Skylance V", "0"};
    json expected;
    json require;
    require["name"] = "Skylance V";
    expected.emplace_back(require);

    parser.parseOutfit(tokens, &trigger);
    ASSERT_EQ(trigger["requires"], expected);
}

TEST_F(FileMissionItemTriggerParserTest, StoreTriggerRequireContainingNameAndQuantity) {
    std::vector<std::string> tokens = {"require", "Hyperdrive", "5"};
    json expected;
    json require;
    require["name"] = "Hyperdrive";
    require["quantity"] = 5;
    expected.emplace_back(require);

    parser.parseRequire(tokens, &trigger);
    ASSERT_EQ(trigger["requires"], expected);
}

TEST_F(FileMissionItemTriggerParserTest, StoreTriggerRequireContainingNameAndQuantityOfOne) {
    std::vector<std::string> tokens = {"require", "Hyperdrive", "1"};
    json expected;
    json require;
    require["name"] = "Hyperdrive";
    expected.emplace_back(require);

    parser.parseRequire(tokens, &trigger);
    ASSERT_EQ(trigger["requires"], expected);
}

TEST_F(FileMissionItemTriggerParserTest, StoreTriggerRequireContainingName) {
    std::vector<std::string> tokens = {"require", "Hyperdrive"};
    json expected;
    json require;
    require["name"] = "Hyperdrive";
    expected.emplace_back(require);

    parser.parseRequire(tokens, &trigger);
    ASSERT_EQ(trigger["requires"], expected);
}

TEST_F(FileMissionItemTriggerParserTest, StoreTriggerGiveShipContainingModelAndName) {
    std::vector<std::string> tokens = {"give", "ship", "Black Diamond", "Stormheart"};
    json expected;
    json giveShip;
    giveShip["model"] = "Black Diamond";
    giveShip["name"] = "Stormheart";
    expected.emplace_back(giveShip);

    parser.parseGiveShip(tokens, &trigger);
    ASSERT_EQ(trigger["give_ships"], expected);
}

TEST_F(FileMissionItemTriggerParserTest, StoreTriggerGiveShipContainingModel) {
    std::vector<std::string> tokens = {"give", "ship", "Black Diamond"};
    json expected;
    json giveShip;
    giveShip["model"] = "Black Diamond";
    expected.emplace_back(giveShip);

    parser.parseGiveShip(tokens, &trigger);
    ASSERT_EQ(trigger["give_ships"], expected);
}

TEST_F(FileMissionItemTriggerParserTest, StoreTriggerPaymentContainingBaseAmountAndMultiplier) {
    std::vector<std::string> tokens = {"payment", "1500", "20"};
    json payment;
    payment["is_active"] = true;
    payment["base"] = 1500;
    payment["multiplier"] = 20;

    parser.parsePayment(tokens, &trigger);
    ASSERT_EQ(trigger["payment"], payment);
}

TEST_F(FileMissionItemTriggerParserTest, StoreTriggerPaymentContainingBaseAmount) {
    std::vector<std::string> tokens = {"payment", "1500"};
    json payment;
    payment["is_active"] = true;
    payment["base"] = 1500;

    parser.parsePayment(tokens, &trigger);
    ASSERT_EQ(trigger["payment"], payment);
}

TEST_F(FileMissionItemTriggerParserTest, StoreTriggerPaymentOnly) {
    std::vector<std::string> tokens = {"payment"};
    json payment;
    payment["is_active"] = true;

    parser.parsePayment(tokens, &trigger);
    ASSERT_EQ(trigger["payment"], payment);
}

TEST_F(FileMissionItemTriggerParserTest, StoreTriggerFine) {
    std::string token = "42069";
    int fine = 42069;

    parser.parseFine(token, &trigger);
    ASSERT_EQ(trigger["fine"], fine);
}

TEST_F(FileMissionItemTriggerParserTest, StoreTriggerConditionSetEquals) {
    std::vector<std::string> tokens = {"my rep", "=", "420"};
    json expected;
    json conditionSet;
    conditionSet["condition"] = "my rep";
    conditionSet["operand"] = "=";
    conditionSet["value"] = "420";
    expected.emplace_back(conditionSet);

    parser.parseTriggerConditionType1(tokens, &trigger);
    ASSERT_EQ(trigger["condition_sets"], expected);
}

TEST_F(FileMissionItemTriggerParserTest, StoreTriggerConditionSetPlusEquals) {
    std::vector<std::string> tokens = {"my rep", "+=", "69"};
    json expected;
    json conditionSet;
    conditionSet["condition"] = "my rep";
    conditionSet["operand"] = "+=";
    conditionSet["value"] = "69";
    expected.emplace_back(conditionSet);

    parser.parseTriggerConditionType1(tokens, &trigger);
    ASSERT_EQ(trigger["condition_sets"], expected);
}

TEST_F(FileMissionItemTriggerParserTest, StoreTriggerConditionSetMinusEquals) {
    std::vector<std::string> tokens = {"my rep", "-=", "69"};
    json expected;
    json conditionSet;
    conditionSet["condition"] = "my rep";
    conditionSet["operand"] = "-=";
    conditionSet["value"] = "69";
    expected.emplace_back(conditionSet);

    parser.parseTriggerConditionType1(tokens, &trigger);
    ASSERT_EQ(trigger["condition_sets"], expected);
}

TEST_F(FileMissionItemTriggerParserTest, StoreTriggerConditionSetPlusPlus) {
    std::vector<std::string> tokens = {"my rep", "++"};
    json expected;
    json conditionSet;
    conditionSet["condition"] = "my rep";
    conditionSet["operand"] = "++";
    expected.emplace_back(conditionSet);

    parser.parseTriggerConditionType2(tokens, &trigger);
    ASSERT_EQ(trigger["condition_sets"], expected);
}

TEST_F(FileMissionItemTriggerParserTest, StoreTriggerConditionSetMinusMinus) {
    std::vector<std::string> tokens = {"my rep", "--"};
    json expected;
    json conditionSet;
    conditionSet["condition"] = "my rep";
    conditionSet["operand"] = "--";
    expected.emplace_back(conditionSet);

    parser.parseTriggerConditionType2(tokens, &trigger);
    ASSERT_EQ(trigger["condition_sets"], expected);
}

TEST_F(FileMissionItemTriggerParserTest, StoreTriggerConditionSetTagSet) {
    std::vector<std::string> tokens = {"set", "the tone"};
    json expected;
    json conditionSet;
    conditionSet["tag"] = "set";
    conditionSet["condition"] = "the tone";
    expected.emplace_back(conditionSet);

    parser.parseTriggerConditionType3(tokens, &trigger);
    ASSERT_EQ(trigger["condition_sets"], expected);
}

TEST_F(FileMissionItemTriggerParserTest, StoreTriggerConditionSetTagClear) {
    std::vector<std::string> tokens = {"clear", "the drugs"};
    json expected;
    json conditionSet;
    conditionSet["tag"] = "clear";
    conditionSet["condition"] = "the drugs";
    expected.emplace_back(conditionSet);

    parser.parseTriggerConditionType3(tokens, &trigger);
    ASSERT_EQ(trigger["condition_sets"], expected);
}

TEST_F(FileMissionItemTriggerParserTest, StoreTriggerEventContainingNameAndDelayAndRange) {
    std::vector<std::string> tokens = {"event", "blaze it", "420", "4200"};
    json expected;
    json event;
    event["name"] = "blaze it";
    event["delay"] = 420;
    event["max_delay"] = 4200;
    expected.emplace_back(event);

    parser.parseEvent(tokens, &trigger);
    ASSERT_EQ(trigger["events"], expected);
}

TEST_F(FileMissionItemTriggerParserTest, StoreTriggerEventContainingNameAndDelay) {
    std::vector<std::string> tokens = {"event", "blaze it", "420"};
    json expected;
    json event;
    event["name"] = "blaze it";
    event["delay"] = 420;
    expected.emplace_back(event);

    parser.parseEvent(tokens, &trigger);
    ASSERT_EQ(trigger["events"], expected);
}

TEST_F(FileMissionItemTriggerParserTest, StoreTriggerEventContainingName) {
    std::vector<std::string> tokens = {"event", "blaze it"};
    json expected;
    json event;
    event["name"] = "blaze it";
    expected.emplace_back(event);

    parser.parseEvent(tokens, &trigger);
    ASSERT_EQ(trigger["events"], expected);
}

TEST_F(FileMissionItemTriggerParserTest, StoreTriggerFailContainingMissionId) {
    std::vector<std::string> tokens = {"event", "the mission"};
    json fails;
    fails.emplace_back("the mission");

    parser.parseFail(tokens, &trigger);
    ASSERT_EQ(trigger["fails"], fails);
}

TEST_F(FileMissionItemTriggerParserTest, StoreTriggerFailOnly) {
    std::vector<std::string> tokens = {"event"};
    json fails;
    fails.emplace_back("fail this mission");

    // set the mission id before it is referenced by parseEvent
    parser.set_mission_id("fail this mission");
    parser.parseFail(tokens, &trigger);
    ASSERT_EQ(trigger["fails"], fails);
}

} // namespace parsertests
