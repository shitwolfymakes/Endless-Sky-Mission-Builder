// SPDX-License-Identifier: GPL-3.0-only
/*
 * filesubstitutionsitemparser_tests.h
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef FILESUBSTITUTIONSITEMPARSER_TESTS_H
#define FILESUBSTITUTIONSITEMPARSER_TESTS_H

#include <gtest/gtest.h>
#include <gmock/gmock.h>

#include "parsers/filesubstitutionsitemparser.h"

namespace parsertests {

std::vector<std::string> sample_substitution_node = {"\tsubstitutions",
                                                     "\t\t\"<title>\" \"Bossmang\"",
                                                     "\t\t\"<title>\" \"Inner\"",
                                                     "\t\t\t\"reputation: Inyalowda\" > 100",
                                                     "\t\t\t\"reputation: Beltalowda\" < 100",
                                                     "\t\t\"<name>\" \"Anderson Dawes\""};

// Fixture for testing a substitution node
class FileSubstititionsItemParserTest : public ::testing::Test {
protected:
    FileSubstitutionsItemParser parser = FileSubstitutionsItemParser(sample_substitution_node);
};

} // namespace parsertests

#endif // FILESUBSTITUTIONSITEMPARSER_TESTS_H
