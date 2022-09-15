// SPDX-License-Identifier: GPL-3.0-only
/*
 * filephraseitemparser_tests.h
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef FILEPHRASEITEMPARSERTEST_H
#define FILEPHRASEITEMPARSERTEST_H

#include <gtest/gtest.h>
#include <gmock/gmock.h>

#include "phrase/filephraseitemparser.h"

namespace parsertests {

std::vector<std::string> sample_phrase_node = { "phrase \"Harambe 1\"",
                                                "\tword",
                                                "\t\t\"Silverback\"",
                                                "\t\t`Harambe died for you` 10",
                                                "\t\t\"Never forget. ${placeholder}\"",
                                                "\t\t\"Always remember. ${placeholder}\" 20",
                                                "\tphrase",
                                                "\t\t\"Don't fall in!\"",
                                                "\t\t\"Watch out for armed zookeepers\" 30",
                                                "\treplace",
                                                "\t\t\"Harambe\" \"King\"" };
std::vector<std::string> sample_phrase_child_node = { "\tphrase \"Harambe 1\"",
                                                      "\t\tword",
                                                      "\t\t\t\"Silverback\"",
                                                      "\t\t\t`Harambe died for you` 10",
                                                      "\t\t\t\"Never forget. ${placeholder}\"",
                                                      "\t\t\t\"Always remember. ${placeholder}\" 20",
                                                      "\t\tphrase",
                                                      "\t\t\t\"Don't fall in!\"",
                                                      "\t\t\t\"Watch out for armed zookeepers\" 30",
                                                      "\t\treplace",
                                                      "\t\t\t\"Harambe\" \"King\"" };
std::vector<std::string> empty_word_node = { "phrase \"Harambe 1\"",
                                             "\tword" };
std::vector<std::string> empty_subPhrase_node = { "phrase \"Harambe 1\"",
                                                  "\tphrase" };
std::vector<std::string> empty_replace_node = { "phrase \"Harambe 1\"",
                                                "\treplace" };

// Fixture for testing a substitution node
class FilePhraseItemParserTest : public ::testing::Test {
protected:
    FilePhraseItemParser parser = FilePhraseItemParser(sample_phrase_node);
};

} // namespace parsertests

#endif // FILEPHRASEITEMPARSERTEST_H
