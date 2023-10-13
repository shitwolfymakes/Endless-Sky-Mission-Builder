// SPDX-License-Identifier: GPL-3.0-only
/*
 * filepersonalityitemparser_tests.h
 *
 * Copyright (c) 2023, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef FILEPERSONALITYITEMPARSER_TESTS_H
#define FILEPERSONALITYITEMPARSER_TESTS_H

#include <gtest/gtest.h>
#include <gmock/gmock.h>

#include "personality/filepersonalityitemparser.h"

namespace parsertests {

std::string PERSONALITY_NODE_HEADER = "personality\n";

// Fixture for testing a node
class FilePersonalityItemParserTest : public ::testing::Test {
protected:
    FilePersonalityItemParser parser = FilePersonalityItemParser({PERSONALITY_NODE_HEADER});
};

} // namespace parsertests

#endif // FILEPERSONALITYITEMPARSER_TESTS_H
