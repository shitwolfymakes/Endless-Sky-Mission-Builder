// SPDX-License-Identifier: GPL-3.0-only
/*
 * main.cpp
 *
 * Copyright (c) 2021, Andrew Sneed <wolfy@shitwolfymakes.com>
 */
#ifndef TST_TESTCASENAME_H
#define TST_TESTCASENAME_H

#include <gtest/gtest.h>
#include <gmock/gmock-matchers.h>

using namespace testing;

TEST(TestSuiteName, TestCaseName)
{
    EXPECT_EQ(1, 1);
    ASSERT_THAT(0, Eq(0));
}

#endif // TST_TESTCASENAME_H
