// SPDX-License-Identifier: GPL-3.0-only
/*
 * filegovernmentitemparser.h
 *
 * Copyright (c) 2023, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef FILEGOVERNMENTITEMPARSER_H
#define FILEGOVERNMENTITEMPARSER_H

#include <common/fileitemparserimpl.h>

#include "nlohmann/json.hpp"
using json = nlohmann::json;

class FileGovernmentItemParser : public FileItemParserImpl {
    json govt;

public:
    // CREATORS
    FileGovernmentItemParser(std::vector<std::string>);

    // MANIPULATORS
    json run();

    void parseId(std::string);
    void parseDisplayName(std::string);
    void parseSwizzle(std::string);
    void parseColor(std::vector<std::string>);
    void parsePlayerRep(std::string);
    void parseReputation(std::vector<std::string>);
    void parseCrewAttack(std::string);
    void parseCrewDefense(std::string);
    void parseAttitudeToward(std::vector<std::string>);
    json parseActionsAndModifiers(std::vector<std::string>);
    void parsePenaltyFor(std::vector<std::string>);
    void parseForeignPenaltiesFor(std::vector<std::string>);
    void parseCustomPenaltiesFor(std::vector<std::string>);
    void parseBribe(std::string);

    // ACCESSORS
    json getData() const;
};

#endif // FILEGOVERNMENTITEMPARSER_H
