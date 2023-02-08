// SPDX-License-Identifier: GPL-3.0-only
/*
 * fileeventitemparser_tests.h
 *
 * Copyright (c) 2023, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef FILEEVENTITEMPARSER_TESTS_H
#define FILEEVENTITEMPARSER_TESTS_H

#include <gtest/gtest.h>
#include <gmock/gmock.h>

#include "event/fileeventitemparser.h"

namespace parsertests {

std::vector<std::string> sample_event_node = {};

// Fixture for testing an event node
class FileEventItemParserTest : public ::testing::Test {
protected:
    FileEventItemParser parser = FileEventItemParser(sample_event_node);
};

} // namespace parsertests

#endif // FILEEVENTITEMPARSER_TESTS_H
