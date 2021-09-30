// SPDX-License-Identifier: GPL-3.0-only
/*
 * fileitemregex.h
 *
 * Copyright (c) 2021, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef FILEITEMREGEX_H
#define FILEITEMREGEX_H

#include <regex>

// define regex matches
static const std::regex matchEvent      ("^event.*$");
static const std::regex matchGovernment ("^government.*$");
static const std::regex matchMission    ("^mission.*$");
static const std::regex matchPhrase     ("^phrase.*$");
static const std::regex matchShip       ("^ship.*$");

#endif // FILEITEMREGEX_H
