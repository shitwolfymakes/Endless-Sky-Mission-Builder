// SPDX-License-Identifier: GPL-3.0-only
/*
 * filemissionitemparser.h
 *
 * Copyright (c) 2021, Andrew Sneed <wolfy@shitwolfymakes.com>
 */
#ifndef FILEMISSIONITEMPARSER_H
#define FILEMISSIONITEMPARSER_H

#include "parsers/fileitemparser.h"

class FileMissionItemParser : public FileItemParser
{
private:
    json mission;

public:
    FileMissionItemParser(std::vector<std::string>);

    void run();

    void parseId(std::vector<std::string>);
    void parseName(std::vector<std::string>);
    void parseDescription(std::vector<std::string>);
    void parseBlocked(std::vector<std::string>);
    void parseDeadline(std::vector<std::string>);
    void parseCargo(std::vector<std::string>);
    void parsePassengers(std::vector<std::string>);
    void parseIllegal(std::vector<std::string>);
    void parseStealth();
    void parseInvisible();
    void parsePriorityLevel(std::string);
    void parseWhereShown(std::string);
    void parseRepeat(std::vector<std::string>);
    void parseClearance(std::vector<std::string>);
    void parseInfiltrating();
    void parseWaypoint(std::vector<std::string>);
};

#endif // FILEMISSIONITEMPARSER_H
