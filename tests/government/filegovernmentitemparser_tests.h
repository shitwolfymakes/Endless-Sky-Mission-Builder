// SPDX-License-Identifier: GPL-3.0-only
/*
 * filegovernmentitemparser_tests.h
 *
 * Copyright (c) 2023, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef FILEGOVERNMENTITEMPARSER_TESTS_H
#define FILEGOVERNMENTITEMPARSER_TESTS_H

#include <gtest/gtest.h>
#include <gmock/gmock.h>

#include "government/filegovernmentitemparser.h"

namespace parsertests {

std::vector<std::string> empty_event_node = {
    "event \"The Savior's Return\""
};

// Fixture for testing a node
class FileGovernmentItemParserTest : public ::testing::Test {
protected:
    FileGovernmentItemParser parser = FileGovernmentItemParser(empty_event_node);
};

} // namespace parsertests

#endif // FILEGOVERNMENTITEMPARSER_TESTS_H
