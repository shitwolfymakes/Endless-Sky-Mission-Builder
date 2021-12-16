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

    json run();

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
    void parseWaypoint(std::string);
    void parseStopover(std::string);
    void parseSource(std::string);
    void parseDestination(std::string);
    int parseTrigger(std::vector<std::string> *, int);
    void parseLog(std::vector<std::string>, json *);
    void parseLog(std::string, json *);
    int parseConversation(std::vector<std::string> *, int, json *);
    int parseDialog(std::vector<std::string> *, int, json *);
    void parseOutfit(std::vector<std::string>, json *);
    void parseRequire(std::vector<std::string>, json *);
    void parseGiveShip(std::vector<std::string>, json *);
    int parseCondition(std::vector<std::string> *, int);
    int parseNpc(std::vector<std::string> *, int);

    json get_mission();
};

#endif // FILEMISSIONITEMPARSER_H
