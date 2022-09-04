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

} // namespace parsertests
