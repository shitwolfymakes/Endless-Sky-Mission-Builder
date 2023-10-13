// SPDX-License-Identifier: GPL-3.0-only
/*
 * filepersonalityitemparser_tests.cpp
 *
 * Copyright (c) 2023, Andrew Sneed <wolfy@shitwolfymakes.com>
 */
#include "filepersonalityitemparser_tests.h"
#include "common/fileitemparserutils.h"

using namespace testing;

namespace parsertests {

TEST_F(FilePersonalityItemParserTest, TestEmptyPersonalityParsing) {
    // declare an empty personality node
    json personality = parser.run();

    json expected;

    ASSERT_EQ(personality, expected);
}

} // namespace parsertests
