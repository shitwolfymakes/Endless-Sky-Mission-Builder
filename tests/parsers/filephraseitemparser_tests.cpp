// SPDX-License-Identifier: GPL-3.0-only
/*
 * filephraseitemparser_tests.cpp
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */
#include "filephraseitemparser_tests.h"

using namespace testing;

namespace parsertests {

// Test top level field parsing
TEST_F(FilePhraseItemParserTest, TestPhraseParsing) {
    /** JSON representation:
     *  {
     *      "words": [
     *          "Silverback",
     *          "Never forget. ${placeholder}",
     *      ],
     *      "words_weighted": [
     *          { "text": "Harambe died for you", "weight": 10 },
     *          { "text": "Always remember. ${placeholder}", "weight": 20 }
     *      ],
     *      "phrases": [
     *          "Don't fall in!"
     *      ],
     *      "phrases_weighted": [
     *          { "phrase": "Watch out for armed zookeepers", "weight": 30 }
     *      ],
     *      "replace": [
     *          { "text": "Harambe", "replacement": "King" }
     *      ]
     *  }
     */
    json expected;

    // Setup words
    expected["words"].emplace_back("Silverback");
    expected["words"].emplace_back("Never forget. ${placeholder}");

    // Setup words with weights
    json weighted_word, weighted_word_2;
    weighted_word["text"] = "Harambe died for you";
    weighted_word["weight"] = 10;
    weighted_word_2["text"] = "Always remember. ${placeholder}";
    weighted_word_2["weight"] = 20;

    expected["words_weighted"].emplace_back(weighted_word);
    expected["words_weighted"].emplace_back(weighted_word_2);

    // Setup phrases
    expected["phrases"].emplace_back("Don't fall in!");

    // Setup phrases with weights
    json weighted_phrase;
    weighted_phrase["phrase"] = "Watch out for armed zookeepers";
    weighted_phrase["weight"] = 30;

    expected["phrases_weighted"].emplace_back(weighted_phrase);

    // Setup replaces
    json replace;
    replace["text"] = "Harambe";
    replace["replacement"] = "King";

    expected["replace"].emplace_back(replace);

    std::cout << "Expected data: " << expected.dump(4) << std::endl;

    ASSERT_EQ(0,1);
}

TEST_F(FilePhraseItemParserTest, StoreHomogenousWordNode) {
    /** JSON representation:
     *  {
     *     "words": [
     *         "Silverback",
     *         "Never forget. ${placeholder}",
     *      ]
     *  }
     */

    json expected;
    json words;
    words.emplace_back("Silverback");
    words.emplace_back("Never forget. ${placeholder}");
    expected["words"] = words;

    int index = 0;
    std::vector<std::string> lines = empty_word_node;
    lines.emplace_back("\t\t\"Silverback\"");
    lines.emplace_back("\t\t\"Never forget. ${placeholder}\"");
    parser = FilePhraseItemParser(lines);

    index = parser.parseWords(&lines, 1);
    ASSERT_EQ(index, 3);
    ASSERT_EQ(parser.get_data(), expected);
}

TEST_F(FilePhraseItemParserTest, StoreHeterogenousWordNode) {
    /** JSON representation:
     *  {
     *     "words": [
     *         "Silverback"
     *      ],
     *      "words_weighted": [
     *          { "text": "Harambe died for you", "weight": 10 }
     *      ]
     *  }
     */

    json expected;
    json words;
    words.emplace_back("Silverback");
    expected["words"] = words;
    json weighted_word;
    weighted_word["text"] = "Harambe died for you";
    weighted_word["weight"] = 10;
    expected["words_weighted"].emplace_back(weighted_word);

    int index = 0;
    std::vector<std::string> lines = empty_word_node;
    lines.emplace_back("\t\t\"Silverback\"");
    lines.emplace_back("\t\t`Harambe died for you` 10");
    parser = FilePhraseItemParser(lines);

    index = parser.parseWords(&lines, 1);
    ASSERT_EQ(index, 3);
    ASSERT_EQ(parser.get_data(), expected);
}

TEST_F(FilePhraseItemParserTest, StoreHomogenousSubPhraseNode) {
    /** JSON representation:
     *  {
     *     "phrases": [
     *         "Don't fall in!",
     *         "Don't you fall in!"
     *      ]
     *  }
     */

    json expected;
    json phrases;
    phrases.emplace_back("Don't fall in!");
    phrases.emplace_back("Don't you fall in!");
    expected["phrases"] = phrases;

    int index = 0;
    std::vector<std::string> lines = empty_subPhrase_node;
    lines.emplace_back("\t\t\"Don't fall in!\"");
    lines.emplace_back("\t\t\"Don't you fall in!\"");
    parser = FilePhraseItemParser(lines);

    index = parser.parseSubPhrase(&lines, 1);
    ASSERT_EQ(index, 3);
    ASSERT_EQ(parser.get_data(), expected);
}

TEST_F(FilePhraseItemParserTest, StoreHeterogenousSubPhraseNode) {
    /** JSON representation:
     *  {
     *     "phrases": [
     *         "Don't fall in!"
     *      ],
     *      "phrases_weighted": [
     *          { "text": "Watch out for armed zookeepers", "weight": 30 }
     *      ]
     *  }
     */

    json expected;
    json phrases;
    phrases.emplace_back("Don't fall in!");
    expected["phrases"] = phrases;
    json weighted_word;
    weighted_word["text"] = "Watch out for armed zookeepers";
    weighted_word["weight"] = 30;
    expected["phrases_weighted"].emplace_back(weighted_word);

    int index = 0;
    std::vector<std::string> lines = empty_subPhrase_node;
    lines.emplace_back("\t\t\"Don't fall in!\"");
    lines.emplace_back("\t\t\"Watch out for armed zookeepers\" 30");
    parser = FilePhraseItemParser(lines);

    index = parser.parseSubPhrase(&lines, 1);
    ASSERT_EQ(index, 3);
    ASSERT_EQ(parser.get_data(), expected);
}

TEST_F(FilePhraseItemParserTest, StoreReplaceNode) {
    /** JSON representation:
     *  {
     *      "replace": [
     *          { "text": "Harambe", "replacement": "King" },
     *          { "text": "Harambe", "replacement": "Chad" }
     *      ]
     *  }
     */

    json expected;
    json replace, replace2;
    replace["text"] = "Harambe";
    replace["replacement"] = "King";
    replace2["text"] = "Harambe";
    replace2["replacement"] = "Chad";

    expected["replace"].emplace_back(replace);
    expected["replace"].emplace_back(replace2);

    int index = 0;
    std::vector<std::string> lines = empty_subPhrase_node;
    lines.emplace_back("\t\t\"Harambe\" \"King\"");
    lines.emplace_back("\t\t\"Harambe\" \"Chad\"");
    parser = FilePhraseItemParser(lines);

    index = parser.parseReplace(&lines, 1);
    ASSERT_EQ(index, 3);
    ASSERT_EQ(parser.get_data(), expected);
}


} // namespace parsertests
