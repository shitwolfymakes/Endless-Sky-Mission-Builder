// SPDX-License-Identifier: GPL-3.0-only
/*
 * filefilteritemparser_tests.h
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef FILEFILTERITEMPARSER_TESTS_H
#define FILEFILTERITEMPARSER_TESTS_H

#include <gtest/gtest.h>
#include <gmock/gmock.h>

#include "filter/filefilteritemparser.h"

namespace parsertests {

std::vector<std::string> sample_filter_node = { "" };

// Fixture for testing a filter node
class FileFilterItemParserTest : public ::testing::Test {
protected:
    FileFilterItemParser parser = FileFilterItemParser(sample_filter_node);
};

} // namespace parsertests

#endif // FILEFILTERITEMPARSER_TESTS_H
