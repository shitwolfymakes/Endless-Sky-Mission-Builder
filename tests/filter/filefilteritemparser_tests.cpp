// SPDX-License-Identifier: GPL-3.0-only
/*
 * filefilteritemparser_tests.cpp
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */
#include "filefilteritemparser_tests.h"

using namespace testing;

namespace parsertests {

TEST_F(FileFilterItemParserTest, TestIsModifier) {
    bool result = FileFilterItemParser::isModifier("not");
    ASSERT_EQ(result, true);

    result = FileFilterItemParser::isModifier("neighbor");
    ASSERT_EQ(result, true);

    result = FileFilterItemParser::isModifier("asdf");
    ASSERT_EQ(result, false);
}

} // namespace parsertests
