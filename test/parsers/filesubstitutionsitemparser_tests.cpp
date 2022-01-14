// SPDX-License-Identifier: GPL-3.0-only
/*
 * filesubstitutionsitemparser_tests.cpp
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */
#include "filesubstitutionsitemparser_tests.h"

using namespace testing;

namespace parsertests {

// Test top level field parsing
TEST_F(FileSubstititionsItemParserTest, TestSubstitutionsParsing) {
    parser.run();
    ASSERT_EQ(1, 0);
}

} // namespace parsertests
