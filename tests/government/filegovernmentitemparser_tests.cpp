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
        "\t\t\"send untranslated hails\"\n"
    };
    parser.setLines(full_government_node);
    json govt = parser.run();

    json expected;
    expected["id"] = "GalacticFederation";
    expected["display_name"] = "Galactic Federation";
    expected["swizzle"] = 6;
    expected["provoked_on_scan"] = true;
    expected["send_untranslated_hails"] = true;



    ASSERT_EQ(govt, expected);
}

TEST_F(FileGovernmentItemParserTest, TestEmptyGovernmentParsing) {
    // declare an empty govt node
    json govt = parser.run();

    json expected;
    // set flags that appear only if true to false to ensure they don't persist

    expected["id"] = "GalacticFederation";
    expected["provoked_on_scan"] = false;
    expected["send_untranslated_hails"] = false;

    ASSERT_EQ(govt, expected);
}

TEST_F(FileGovernmentItemParserTest, TestParseDisplayName) {
    std::vector<std::string> nodeLines = {GOVT_NODE_HEADER,
                                          "\t\"display name\" \"Galactic Federation\"\n"};
    parser.setLines(nodeLines);

    json govt = parser.run();
    ASSERT_EQ(govt["display_name"], "Galactic Federation");
}

TEST_F(FileGovernmentItemParserTest, TestParseSwizzle) {
    std::vector<std::string> nodeLines = {GOVT_NODE_HEADER,
                                          "\tswizzle 6\n"};
    parser.setLines(nodeLines);

    json govt = parser.run();
    ASSERT_EQ(govt["swizzle"], 6);
}

TEST_F(FileGovernmentItemParserTest, TestParseColorRGB) {
    std::vector<std::string> nodeLines = {GOVT_NODE_HEADER,
                                          "\tcolor .11 .22 .33\n"};
    parser.setLines(nodeLines);
    json color;
    color["R"] = 0.11;
    color["G"] = 0.22;
    color["B"] = 0.33;

    json govt = parser.run();
    ASSERT_EQ(govt["color"], color);
}

TEST_F(FileGovernmentItemParserTest, TestParseColorName) {
    std::vector<std::string> nodeLines = {GOVT_NODE_HEADER,
                                          "\tcolor Red\n"};
    parser.setLines(nodeLines);
    json color;
    color = "Red";

    json govt = parser.run();
    ASSERT_EQ(govt["color"], "Red");
}

TEST_F(FileGovernmentItemParserTest, TestParsePlayerRep) {
    std::vector<std::string> nodeLines = {GOVT_NODE_HEADER,
                                          "\t\"player reputation\" 100\n"};
    parser.setLines(nodeLines);

    json govt = parser.run();
    ASSERT_EQ(govt["player_reputation"], 100);
}

TEST_F(FileGovernmentItemParserTest, TestParseReputationNode) {
    std::vector<std::string> nodeLines = {GOVT_NODE_HEADER,
                                          "\treputation",
                                          "\t\t\"player reputation\" 50\n",
                                          "\t\tmin 0\n",
                                          "\t\tmax 100\n"};
    parser.setLines(nodeLines);
    json reputation;
    reputation["player_reputation"] = 50;
    reputation["min"] = 0;
    reputation["max"] = 100;

    json govt = parser.run();
    ASSERT_EQ(parser.getData()["reputation"], reputation);
}

TEST_F(FileGovernmentItemParserTest, TestParseCrewAttack) {
    std::vector<std::string> nodeLines = {GOVT_NODE_HEADER,
                                          "\t\"crew attack\" 5\n"};
    parser.setLines(nodeLines);

    json govt = parser.run();
    ASSERT_EQ(govt["crew_attack"], 5.0);
}

TEST_F(FileGovernmentItemParserTest, TestParseCrewDefense) {
    std::vector<std::string> nodeLines = {GOVT_NODE_HEADER,
                                          "\t\"crew defense\" 5\n"};
    parser.setLines(nodeLines);

    json govt = parser.run();
    ASSERT_EQ(govt["crew_defense"], 5.0);
}

TEST_F(FileGovernmentItemParserTest, TestParseAttitudeToward) {
    std::vector<std::string> nodeLines = {GOVT_NODE_HEADER,
                                          "\t\"attitude toward\"\n",
                                          "\t\t\"Klingon Empire\" 85\n",
                                          "\t\t\"Cardassian Union\" -100\n"};
    parser.setLines(nodeLines);

    json attitude_toward, attitude;

    attitude["government"] = "Klingon Empire";
    attitude["rep-modifier"] = 85;
    attitude_toward.emplace_back(attitude);

    attitude["government"] = "Cardassian Union";
    attitude["rep-modifier"] = -100;
    attitude_toward.emplace_back(attitude);

    json govt = parser.run();
    ASSERT_EQ(govt["attitude_toward"], attitude_toward);
}

TEST_F(FileGovernmentItemParserTest, TestParsePenaltyFor) {
    std::vector<std::string> nodeLines = {GOVT_NODE_HEADER,
                                          "\t\"penalty for\"\n",
                                          "\t\tassist -0.1\n",
                                          "\t\tdestroy 1\n"};
    parser.setLines(nodeLines);

    json penalty_for, penalty;

    penalty["action"] = "assist";
    penalty["rep-modifier"] = -0.1;
    penalty_for.emplace_back(penalty);

    penalty["action"] = "destroy";
    penalty["rep-modifier"] = 1.0;
    penalty_for.emplace_back(penalty);

    json govt = parser.run();
    ASSERT_EQ(govt["penalty_for"], penalty_for);
}

TEST_F(FileGovernmentItemParserTest, TestParseForeignPenaltiesFor) {
    std::vector<std::string> nodeLines = {GOVT_NODE_HEADER,
                                          "\t\"foreign penalties for\"",
                                          "\t\t\"Klingon Empire\"\n",
                                          "\t\t\"Cardassian Union\"\n"};
    parser.setLines(nodeLines);

    json foreign_penalties;
    foreign_penalties.emplace_back("Klingon Empire");
    foreign_penalties.emplace_back("Cardassian Union");

    json govt = parser.run();
    ASSERT_EQ(govt["foreign_penalties_for"], foreign_penalties);
}

TEST_F(FileGovernmentItemParserTest, TestParseCustomPenaltiesFor) {
    std::vector<std::string> nodeLines = {GOVT_NODE_HEADER,
                                          "\t\"custom penalties for\"\n",
                                          "\t\t\"Klingon Empire\"\n",
                                          "\t\t\tassist -0.1\n",
                                          "\t\t\"Cardassian Union\"\n",
                                          "\t\t\tdestroy 1\n"};
    parser.setLines(nodeLines);

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

    json govt = parser.run();
    ASSERT_EQ(govt["custom_penalties_for"], custom_penalties);
}

TEST_F(FileGovernmentItemParserTest, TestParseBribe) {
    std::vector<std::string> nodeLines = {GOVT_NODE_HEADER,
                                          "\tbribe 0.1\n"};
    parser.setLines(nodeLines);

    json bribe = 0.1;

    json govt = parser.run();
    ASSERT_EQ(govt["bribe"], bribe);
}

TEST_F(FileGovernmentItemParserTest, TestParsePercentage) {
    std::vector<std::string> nodeLines = {GOVT_NODE_HEADER,
                                          "\tfine 0.1\n"};
    parser.setLines(nodeLines);

    json fine = 0.1;

    json govt = parser.run();
    ASSERT_EQ(govt["fine"], fine);
}

TEST_F(FileGovernmentItemParserTest, TestParseDeathSentence) {
    std::vector<std::string> nodeLines = {GOVT_NODE_HEADER,
                                          "\t\"death sentence\" \"caught red-handed\"\n"};
    parser.setLines(nodeLines);
    json death_sentence = "caught red-handed";

    json govt = parser.run();
    ASSERT_EQ(govt["death_sentence"], death_sentence);
}

TEST_F(FileGovernmentItemParserTest, TestParseFriendlyHail) {
    std::vector<std::string> nodeLines = {GOVT_NODE_HEADER,
                                          "\t\"friendly hail\" \"hello world\"\n"};
    parser.setLines(nodeLines);
    json friendly_hail = "hello world";

    json govt = parser.run();
    ASSERT_EQ(govt["friendly_hail"], friendly_hail);
}

TEST_F(FileGovernmentItemParserTest, TestParseFriendlyDisabledHail) {
    std::vector<std::string> nodeLines = {GOVT_NODE_HEADER,
                                          "\t\"friendly disabled hail\" \"SOS\"\n"};
    parser.setLines(nodeLines);
    json friendly_disabled_hail = "SOS";

    json govt = parser.run();
    ASSERT_EQ(govt["friendly_disabled_hail"], friendly_disabled_hail);
}

TEST_F(FileGovernmentItemParserTest, TestParseHostileHail) {
    std::vector<std::string> nodeLines = {GOVT_NODE_HEADER,
                                          "\t\"hostile hail\" \"screw you\"\n"};
    parser.setLines(nodeLines);
    json hostile_hail = "screw you";

    json govt = parser.run();
    ASSERT_EQ(govt["hostile_hail"], hostile_hail);
}

TEST_F(FileGovernmentItemParserTest, TestParseHostileDisabledHail) {
    std::vector<std::string> nodeLines = {GOVT_NODE_HEADER,
                                          "\t\"hostile disabled hail\" \"just let me die\"\n"};
    parser.setLines(nodeLines);
    json hostile_disabled_hail = "just let me die";

    json govt = parser.run();
    ASSERT_EQ(govt["hostile_disabled_hail"], hostile_disabled_hail);
}

TEST_F(FileGovernmentItemParserTest, TestLanguage) {
    std::vector<std::string> nodeLines = {GOVT_NODE_HEADER,
                                          "\tlanguage \"metaphorical allegory\"\n"};
    parser.setLines(nodeLines);
    json language = "metaphorical allegory";

    json govt = parser.run();
    ASSERT_EQ(govt["language"], language);
}

TEST_F(FileGovernmentItemParserTest, TestRaid) {
    std::vector<std::string> nodeLines = {GOVT_NODE_HEADER,
                                          "\traid \"pirate raid\" 5 10\n"};
    parser.setLines(nodeLines);
    json raid;
    raid["fleet"] = "pirate raid";
    raid["min-attraction"] = 5;
    raid["max-attraction"] = 10;

    json govt = parser.run();
    ASSERT_EQ(govt["raid"], raid);
}

} // namespace parsertests
