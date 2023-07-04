// SPDX-License-Identifier: GPL-3.0-only
/*
 * filegovernmentitemparser_tests.cpp
 *
 * Copyright (c) 2023, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "filegovernmentitemparser_tests.h"

using namespace testing;

namespace parsertests {

// Test top level field parsing
TEST_F(FileGovernmentItemParserTest, TestFullGovernmentParsing) {
    // TODO: Implement this
    // declare a fully populated govt node
    std::vector<std::string> full_government_node = {
        "\tgovernment GalacticFederation\n",
        "\t\t\"display name\" \"Galactic Federation\"\n",
        "\t\tswizzle 6\n",
        "\t\t\"provoked on scan\"\n",
        "\t\t\"send untranslated hails\"\n",
        "\t\tcolor Red\n",
        "\t\t\"player reputation\" 100\n",
        "\t\treputation\n",
        "\t\t\t\"player reputation\" 50\n",
        "\t\t\tmin 0\n",
        "\t\t\tmax 100\n",
        "\t\t\"crew attack\" 5\n",
        "\t\t\"crew defense\" 5\n"
    };
    parser.setLines(full_government_node);
    json govt = parser.run();

    json expected;
    expected["id"] = "GalacticFederation";
    expected["display_name"] = "Galactic Federation";
    expected["swizzle"] = 6;
    expected["provoked_on_scan"] = true;
    expected["send_untranslated_hails"] = true;
    expected["color"] = "Red";
    expected["player_reputation"] = 100;
    expected["reputation"]["player_reputation"] = 50;
    expected["reputation"]["min"] = 0;
    expected["reputation"]["max"] = 100;
    expected["crew_attack"] = 5;
    expected["crew_defense"] = 5;

    ASSERT_EQ(govt, expected);
}

TEST_F(FileGovernmentItemParserTest, TestEmptyGovernmentParsing) {
    // declare an empty govt node
    parser.setLines(empty_government_node);
    json govt = parser.run();

    json expected;
    // set flags that appear only if true to false to ensure they don't persist

    expected["id"] = "GalacticFederation";
    expected["provoked_on_scan"] = false;
    expected["send_untranslated_hails"] = false;

    ASSERT_EQ(govt, expected);
}
/*
TEST_F(FileGovernmentItemParserTest, TestParseId) {
    std::string token = "GalacticFederation";
    parser.parseId(token);
    ASSERT_EQ(parser.getData()["id"], "GalacticFederation");
}

TEST_F(FileGovernmentItemParserTest, TestParseDisplayName) {
    std::string token = "Galactic Federation";
    parser.parseDisplayName(token);
    ASSERT_EQ(parser.getData()["display_name"], "Galactic Federation");
}

TEST_F(FileGovernmentItemParserTest, TestParseSwizzle) {
    std::string token = "6";
    parser.parseSwizzle(token);
    ASSERT_EQ(parser.getData()["swizzle"], 6);
}

TEST_F(FileGovernmentItemParserTest, TestParseColorRGB) {
    std::vector<std::string> tokens = {"color", ".11", ".22", ".33"};
    json color;
    color["R"] = 0.11;
    color["G"] = 0.22;
    color["B"] = 0.33;
    parser.parseColor(tokens);
    ASSERT_EQ(parser.getData()["color"], color);
}

TEST_F(FileGovernmentItemParserTest, TestParseColorName) {
    std::vector<std::string> tokens = {"color", "Red"};
    json color;
    color = "Red";
    parser.parseColor(tokens);
    ASSERT_EQ(parser.getData()["color"], "Red");
}

TEST_F(FileGovernmentItemParserTest, TestParsePlayerRep) {
    std::string token = "100";
    parser.parsePlayerRep(token);
    ASSERT_EQ(parser.getData()["player_reputation"], 100);
}

TEST_F(FileGovernmentItemParserTest, TestParseReputationNode) {
    std::vector<std::string> nodeLines = {"\treputation",
                                          "\t\t\"player reputation\" 50\n",
                                          "\t\tmin 0\n",
                                          "\t\tmax 100\n"};
    json reputation;
    reputation["player_reputation"] = 50;
    reputation["min"] = 0;
    reputation["max"] = 100;
    parser.parseReputation(nodeLines);
    ASSERT_EQ(parser.getData()["reputation"], reputation);
}

TEST_F(FileGovernmentItemParserTest, TestParseCrewAttack) {
    std::string token = "5";
    parser.parseCrewAttack(token);
    ASSERT_EQ(parser.getData()["crew_attack"], 5);
}

TEST_F(FileGovernmentItemParserTest, TestParseCrewDefense) {
    std::string token = "5";
    parser.parseCrewDefense(token);
    ASSERT_EQ(parser.getData()["crew_defense"], 5);
}
*/
TEST_F(FileGovernmentItemParserTest, TestParseAttitudeToward) {
    std::vector<std::string> nodeLines = {"\t\"attitude toward\"",
                                          "\t\t\"Klingon Empire\" 85\n",
                                          "\t\t\"Cardassian Union\" -100\n"};
    json attitude_toward, attitude;

    attitude["government"] = "Klingon Empire";
    attitude["rep-modifier"] = 85;
    attitude_toward.emplace_back(attitude);

    attitude["government"] = "Cardassian Union";
    attitude["rep-modifier"] = -100;
    attitude_toward.emplace_back(attitude);

    parser.parseAttitudeToward(nodeLines);
    ASSERT_EQ(parser.getData()["attitude_toward"], attitude_toward);
}

TEST_F(FileGovernmentItemParserTest, TestParsePenaltyFor) {
    std::vector<std::string> nodeLines = {"\t\"penalty for\"",
                                          "\t\tassist -0.1\n",
                                          "\t\tdestroy 1\n"};
    json penalty_for, penalty;

    penalty["action"] = "assist";
    penalty["rep-modifier"] = -0.1;
    penalty_for.emplace_back(penalty);

    penalty["action"] = "destroy";
    penalty["rep-modifier"] = 1.0;
    penalty_for.emplace_back(penalty);

    parser.parsePenaltyFor(nodeLines);
    ASSERT_EQ(parser.getData()["penalty_for"], penalty_for);
}

TEST_F(FileGovernmentItemParserTest, TestParseForeignPenaltiesFor) {
    std::vector<std::string> nodeLines = {"\t\"foreign penalties for\"",
                                          "\t\t\"Klingon Empire\"\n",
                                          "\t\t\"Cardassian Union\"\n"};
    json foreign_penalties;
    foreign_penalties.emplace_back("Klingon Empire");
    foreign_penalties.emplace_back("Cardassian Union");

    parser.parseForeignPenaltiesFor(nodeLines);
    ASSERT_EQ(parser.getData()["foreign_penalties_for"], foreign_penalties);
}

TEST_F(FileGovernmentItemParserTest, TestParseCustomPenaltiesFor) {
    std::vector<std::string> nodeLines = {"\tcustom penalties for",
                                          "\t\t\"Klingon Empire\"\n",
                                          "\t\t\tassist -0.1\n",
                                          "\t\t\"Cardassian Union\"\n",
                                          "\t\t\tdestroy 1\n"};
    json custom_penalties;
    json penalty, penalty_for_a, penalty_for_b;
    json govt_penalties_a, govt_penalties_b;

    penalty["action"] = "assist";
    penalty["rep-modifier"] = -0.1;
    penalty_for_a.emplace_back(penalty);
    govt_penalties_a["government"] = "Klingon Empire";
    govt_penalties_a["penalties"] = penalty_for_a;

    penalty["action"] = "destroy";
    penalty["rep-modifier"] = 1.0;
    penalty_for_b.emplace_back(penalty);
    govt_penalties_b["government"] = "Cardassian Union";
    govt_penalties_b["penalties"] = penalty_for_b;

    custom_penalties.emplace_back(govt_penalties_a);
    custom_penalties.emplace_back(govt_penalties_b);
    parser.parseCustomPenaltiesFor(nodeLines);
    ASSERT_EQ(parser.getData()["custom_penalties_for"], custom_penalties);
}

TEST_F(FileGovernmentItemParserTest, TestParseBribe) {
    std::string token = "0.1";
    json bribe;
    bribe = 0.1;

    parser.parseBribe(token);
    ASSERT_EQ(parser.getData()["bribe"], bribe);
}

TEST_F(FileGovernmentItemParserTest, TestParsePercentage) {
    std::string token = "0.1";
    json fine;
    fine = 0.1;

    parser.parseFine(token);
    ASSERT_EQ(parser.getData()["fine"], fine);
}

TEST_F(FileGovernmentItemParserTest, TestParseDeathSentence) {
    std::string token = "caught red-handed";
    json death_sentence;
    death_sentence = "caught red-handed";

    parser.parseDeathSentence(token);
    ASSERT_EQ(parser.getData()["death_sentence"], death_sentence);
}

TEST_F(FileGovernmentItemParserTest, TestParseFriendlyHail) {
    std::string token = "hello world";
    json friendly_hail;
    friendly_hail = "hello world";

    parser.parseFriendlyHail(token);
    ASSERT_EQ(parser.getData()["friendly_hail"], friendly_hail);
}

TEST_F(FileGovernmentItemParserTest, TestParseFriendlyDisabledHail) {
    std::string token = "SOS";
    json friendly_disabled_hail;
    friendly_disabled_hail = "SOS";

    parser.parseFriendlyDisabledHail(token);
    ASSERT_EQ(parser.getData()["friendly_disabled_hail"], friendly_disabled_hail);
}

TEST_F(FileGovernmentItemParserTest, TestParseHostileHail) {
    std::string token = "screw you";
    json hostile_hail;
    hostile_hail = "screw you";

    parser.parseHostileHail(token);
    ASSERT_EQ(parser.getData()["hostile_hail"], hostile_hail);
}

TEST_F(FileGovernmentItemParserTest, TestParseHostileDisabledHail) {
    std::string token = "just let me die";
    json hostile_disabled_hail;
    hostile_disabled_hail = "just let me die";

    parser.parseHostileDisabledHail(token);
    ASSERT_EQ(parser.getData()["hostile_disabled_hail"], hostile_disabled_hail);
}

TEST_F(FileGovernmentItemParserTest, TestLanguage) {
    std::string token = "metaphorical allegory";
    json language;
    language = "metaphorical allegory";

    parser.parseLanguage(token);
    ASSERT_EQ(parser.getData()["language"], language);
}

TEST_F(FileGovernmentItemParserTest, TestRaid) {
    std::vector<std::string> tokens = {"raid", "pirate raid", "5", "10"};
    json raid;
    raid["fleet"] = "pirate raid";
    raid["min-attraction"] = 5;
    raid["max-attraction"] = 10;

    parser.parseRaid(tokens);
    ASSERT_EQ(parser.getData()["raid"], raid);
}

} // namespace parsertests
