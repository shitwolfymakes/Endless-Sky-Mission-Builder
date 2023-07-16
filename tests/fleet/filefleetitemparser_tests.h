// SPDX-License-Identifier: GPL-3.0-only
/*
 * filefleetitemparser_tests.h
 *
 * Copyright (c) 2023, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef FILEFLEETITEMPARSER_TESTS_H
#define FILEFLEETITEMPARSER_TESTS_H

#include <gtest/gtest.h>
#include <gmock/gmock.h>

#include "fleet/filefleetitemparser.h"

namespace parsertests {

std::string FLEET_NODE_HEADER = "fleet \"Black Swan\"\n";

// Fixture for testing a node
class FileFleetItemParserTest : public ::testing::Test {
protected:
    FileFleetItemParser parser = FileFleetItemParser({FLEET_NODE_HEADER});
};

} // namespace parsertests

#endif // FILEFLEETITEMPARSER_TESTS_H
