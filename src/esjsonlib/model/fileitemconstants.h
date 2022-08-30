// SPDX-License-Identifier: GPL-3.0-only
/*
 * fileitemconstants.h
 *
 * Copyright (c) 2021, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef FILEITEMCONSTANTS_H
#define FILEITEMCONSTANTS_H

#include <regex>

// define the types of File Items
enum ItemType { Event, Government, Mission, Phrase, Ship, Substitutions };

// define regex matches
static const std::regex matchEvent("^event.*$");
static const std::regex matchGovernment("^government.*$");
static const std::regex matchMission("^mission.*$");
static const std::regex matchPhrase("^phrase.*$");
static const std::regex matchShip("^ship.*$");
static const std::regex matchSubstitutions("^substitutions.*$");

#endif // FILEITEMCONSTANTS_H
