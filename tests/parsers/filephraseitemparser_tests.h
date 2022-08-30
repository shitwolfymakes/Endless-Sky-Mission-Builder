// SPDX-License-Identifier: GPL-3.0-only
/*
 * filephraseitemparser_tests.h
 *
 * Copyright (c) 2022, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef FILEPHRASEITEMPARSERTEST_H
#define FILEPHRASEITEMPARSERTEST_H

#include <gtest/gtest.h>
#include <gmock/gmock.h>

#include "parsers/filephraseitemparser.h"

namespace parsertests {

std::vector<std::string> sample_phrase_node;

// Fixture for testing a substitution node
class FilePhraseItemParserTest : public ::testing::Test {
protected:
    FilePhraseItemParser parser = FilePhraseItemParser(sample_phrase_node);
};

} // namespace parsertests

#endif // FILEPHRASEITEMPARSERTEST_H
