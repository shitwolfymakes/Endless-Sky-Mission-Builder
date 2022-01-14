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
    json expected;
    json e1, e2, e3;
    e1["key"] = "<title>";
    e1["replacement_text"] = "Bossmang";
    expected.emplace_back(e1);

    e2["key"] = "<title>";
    e2["replacement_text"] = "Inner";
    e2["condition_sets"].emplace_back("reputation: Inyalowda > 100");
    e2["condition_sets"].emplace_back("reputation: Beltalowda < 100");
    expected.emplace_back(e2);

    e3["key"] = "<name>";
    e3["replacement_text"] = "Anderson Dawes";
    expected.emplace_back(e3);

    json substitutions = parser.run();

    ASSERT_EQ(substitutions, expected);
}

} // namespace parsertests
