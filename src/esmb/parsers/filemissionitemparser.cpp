// SPDX-License-Identifier: GPL-3.0-only
/*
 * filemissionitemparser.cpp
 *
 * Copyright (c) 2021, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "filemissionitemparser.h"

FileMissionItemParser::FileMissionItemParser(std::vector<std::string> lines)
    : FileItemParser(lines)
{

}

void FileMissionItemParser::run() {
    // for self.i, self.line in self.enum_lines:
    // for line in ItemMission->lines
    std::vector<std::string> tokens;
    for (int i = 0; i < static_cast<int>(lines.size()); i++) {
        // start by tokenizing each line
        // TODO: add a count for the number of tab chars
        tokens = tokenize(lines.at(i));
        //qDebug() << "LINE: " << QString::fromStdString(tokens.at(0));

        if (tokens.size() == 0) {
            QString qLine = QString::fromStdString(lines.at(i));
            qDebug("\tERROR: NO TOKENS FOUND ON LINE: %s", qUtf8Printable(qLine));
        }
        else if (tokens.at(0).compare("mission") == 0) {
            parseId(tokens);
        }
        else if (tokens.at(0).compare("name") == 0) {
            parseName(tokens);
        }
        else if (tokens.at(0).compare("description") == 0) {
            parseDescription(tokens);
        }
        else if (tokens.at(0).compare("blocked") == 0) {
            parseBlocked(tokens);
        }
        else if (tokens.at(0).compare("deadline") == 0) {
            parseDeadline(tokens);
        }
        else if (tokens.at(0).compare("cargo") == 0) {
            parseCargo(tokens);
        }
        else if (tokens.at(0).compare("passengers") == 0) {
            parsePassengers(tokens);
        }
        else if (tokens.at(0).compare("illegal") == 0) {
            parseIllegal(tokens);
        }
        else if (tokens.at(0).compare("stealth") == 0) {
            parseStealth();
        }
        else if (tokens.at(0).compare("invisible") == 0) {
            parseInvisible();
        }
        else if (isOneOf(tokens.at(0), {"priority", "minor"})) {
            parsePriorityLevel(tokens.at(0));
        }
        else if (isOneOf(tokens.at(0), {"job", "landing", "assisting", "boarding"})) {
            parseWhereShown(tokens.at(0));
        }
        else if (tokens.at(0).compare("repeat") == 0) {
            parseRepeat(tokens);
        }
        else if (tokens.at(0).compare("clearance") == 0) {
            if (tokens.size() == 2) {
                parseClearance(tokens);
            } else {
                qDebug("COMPLEX CLEARANCE HANDLING NOT YET IMPLEMENTED");
                continue;
            }
        }
        else if (tokens.at(0).compare("infiltrating") == 0) {
            parseInfiltrating();
        }
        else if (tokens.at(0).compare("waypoint") == 0) {
            if (tokens.size() == 2) {
                parseWaypoint(tokens);
            } else {
                qDebug("COMPLEX WAYPOINT HANDLING NOT YET IMPLEMENTED");
                continue;
            }
        }
        else if (tokens.at(0).compare("stopover") == 0) {
            if (tokens.size() == 2) {
                parseStopover(tokens);
            } else {
                qDebug("COMPLEX STOPOVER HANDLING NOT YET IMPLEMENTED");
                continue;
            }
        }
        else if (tokens.at(0).compare("source") == 0) {
            if (tokens.size() == 2) {
                parseSource(tokens);
            } else {
                qDebug("COMPLEX SOURCE HANDLING NOT YET IMPLEMENTED");
                continue;
            }
        }
        else if (tokens.at(0).compare("destination") == 0) {
            if (tokens.size() == 2) {
                parseDestination(tokens);
            } else {
                qDebug("COMPLEX DESTINATION HANDLING NOT YET IMPLEMENTED");
                continue;
            }
        }
        // elif "on" in tokens
        else if (tokens.at(0).compare("on") == 0) {
            i = parseTrigger(&lines, i);
        }
        // elif "to" in tokens
        else if (tokens.at(0).compare("to") == 0) {
            //qDebug("\tFound condition: %s", qUtf8Printable(QString::fromStdString(tokens.at(1))));
        }
        // elif "npc" in tokens
        else if (tokens.at(0).compare("npc") == 0) {
            //qDebug("\tFound NPC: %s", qUtf8Printable(QString::fromStdString(tokens.at(1))));
        }
        // else error
        else {
            qDebug("\tERROR - No tokens found in line: %s", qUtf8Printable(QString::fromStdString(lines.at(i))));
        }
    }
    // qDebug may occassionally truncate strings output, but the data is still there
    // (https://bugreports.qt.io/browse/QTCREATORBUG-24649)
    //qDebug("Mission data: %s", qUtf8Printable(QString::fromStdString(mission.dump(4))));
}

void FileMissionItemParser::parseId(std::vector<std::string> tokens) {
    qDebug("\tMission ID is: %s", qUtf8Printable(QString::fromStdString(tokens.at(1))));
    mission["id"] = tokens.at(1);
}

void FileMissionItemParser::parseName(std::vector<std::string> tokens) {
    qDebug("\tMission mission display name is: %s", qUtf8Printable(QString::fromStdString(tokens.at(1))));
    mission["name"] = tokens.at(1);
}

void FileMissionItemParser::parseDescription(std::vector<std::string> tokens) {
    qDebug("\tFound description: %s", qUtf8Printable(QString::fromStdString(tokens.at(1))));
    mission["description"] = tokens.at(1);
}

void FileMissionItemParser::parseBlocked(std::vector<std::string> tokens) {
    qDebug("\tFound blocked: %s", qUtf8Printable(QString::fromStdString(tokens.at(1))));
    mission["blocked"] = tokens.at(1);
}

void FileMissionItemParser::parseDeadline(std::vector<std::string> tokens) {
    qDebug("\tFound deadline: %s", qUtf8Printable(QString::fromStdString(boost::join(tokens, " "))));
    mission["deadline"]["is_active"] = true;
    if (tokens.size() > 1) {
        mission["deadline"]["days"] = tokens.at(1);
        if (tokens.size() == 3) {
            mission["deadline"]["multiplier"] = tokens.at(2);
        }
    }
}

void FileMissionItemParser::parseCargo(std::vector<std::string> tokens) {
    qDebug("\tFound cargo: %s", qUtf8Printable(QString::fromStdString(boost::join(tokens, " "))));
    mission["cargo"]["cargo"] = tokens.at(1);
    mission["cargo"]["tonnage"] = tokens.at(2);
    if (tokens.size() > 3) {
        mission["cargo"]["tonnage_range"] = tokens.at(3);
        if (tokens.size() == 5) {
            mission["cargo"]["probability"] = tokens.at(4);
        }
    }
}

void FileMissionItemParser::parsePassengers(std::vector<std::string> tokens) {
    qDebug("\tFound passengers: %s", qUtf8Printable(QString::fromStdString(boost::join(tokens, " "))));
    mission["passengers"]["passengers"] = tokens.at(1);
    if (tokens.size() > 2) {
        mission["passengers"]["passengers_range"] = tokens.at(2);
        if (tokens.size() == 4) {
            mission["passengers"]["probability"] = tokens.at(3);
        }
    }
}

void FileMissionItemParser::parseIllegal(std::vector<std::string> tokens) {
    qDebug("\tFound illegal: %s", qUtf8Printable(QString::fromStdString(boost::join(tokens, " "))));
    mission["illegal"]["fine"] = tokens.at(1);
    if (tokens.size() == 3) {
        mission["illegal"]["message"] = tokens.at(2);
    }
}

void FileMissionItemParser::parseStealth() {
    qDebug("\tFound stealth field");
    mission["stealth"] = true;
}

void FileMissionItemParser::parseInvisible() {
    qDebug("\tFound invisible field");
    mission["invisible"] = true;
}

void FileMissionItemParser::parsePriorityLevel(std::string token) {
    qDebug("\tFound priority level: %s", qUtf8Printable(QString::fromStdString(token)));
    mission["priority_level"] = token;
}

void FileMissionItemParser::parseWhereShown(std::string token) {
    qDebug("\tFound where shown: %s", qUtf8Printable(QString::fromStdString(token)));
    mission["where_shown"] = token;
}

void FileMissionItemParser::parseRepeat(std::vector<std::string> tokens) {
    qDebug("\tFound repeat: %s", qUtf8Printable(QString::fromStdString(boost::join(tokens, " "))));
    mission["repeat"]["is_active"] = true;
    if (tokens.size() == 2) {
        mission["repeat"]["amount"] = tokens.at(1);
    }
}

void FileMissionItemParser::parseClearance(std::vector<std::string> tokens) {
    qDebug("\tFound clearance: %s", qUtf8Printable(QString::fromStdString(tokens.at(1))));
    mission["clearance"]["message"] = tokens.at(1);
}

void FileMissionItemParser::parseInfiltrating() {
    qDebug("\tFound infiltrating field");
    mission["infiltrating"] = true;
}

void FileMissionItemParser::parseWaypoint(std::vector<std::string> tokens) {
    qDebug("\tFound waypoint: %s", qUtf8Printable(QString::fromStdString(tokens.at(1))));
    mission["waypoint"] = tokens.at(1);
}

void FileMissionItemParser::parseStopover(std::vector<std::string> tokens) {
    qDebug("\tFound stopover: %s", qUtf8Printable(QString::fromStdString(tokens.at(1))));
    mission["stopover"] = tokens.at(1);
}

void FileMissionItemParser::parseSource(std::vector<std::string> tokens) {
    qDebug("\tFound source: %s", qUtf8Printable(QString::fromStdString(tokens.at(1))));
    mission["source"] = tokens.at(1);
}

void FileMissionItemParser::parseDestination(std::vector<std::string> tokens) {
    qDebug("\tFound destination: %s", qUtf8Printable(QString::fromStdString(tokens.at(1))));
    mission["destination"] = tokens.at(1);
}

int FileMissionItemParser::parseTrigger(std::vector<std::string> *missionLines, int startingIndex) {
    std::vector<std::string> lines = *missionLines;
    int index = startingIndex;
    json trigger; // create a json obect to store trigger data, pass ref to this when necessary

    qDebug("\tFound trigger: %s", qUtf8Printable(QString::fromStdString(lines.at(index))));
    int cur = getIndentLevel(lines.at(index));
    int nxt = getIndentLevel(lines.at(index + 1));
    while (true) {
        if (nxt <= cur) {
            break;
        }

        index++;
        std::vector<std::string> tokens = tokenize(lines.at(index));
        // parse the content of this line in the trigger
        if (tokens.at(0).compare("conversation") == 0) {
            index = parseConversation(missionLines, index, &trigger);
        } else if (tokens.at(0).compare("dialog") == 0) {
            index = parseDialog(missionLines, index, &trigger);
        } else if (tokens.at(0).compare("outfit") == 0) {
            qDebug("\tFound outfit: %s", qUtf8Printable(QString::fromStdString(lines.at(index))));
            trigger["outfit"]["outfit"] = tokens.at(1);
            if (tokens.size() == 3) {
                trigger["outfit"]["quantity"] = tokens.at(2);
            }
        } else if (tokens.at(0).compare("require") == 0) {
            qDebug("\tFound require: %s", qUtf8Printable(QString::fromStdString(lines.at(index))));
            trigger["require"]["outfit"] = tokens.at(1);
            if (tokens.size() == 3) {
                trigger["require"]["quantity"] = tokens.at(2);
            }
        } else if (tokens.at(0).compare("give") == 0 && tokens.at(1).compare("ship") == 0) {
            qDebug("\tFound give ship: %s", qUtf8Printable(QString::fromStdString(lines.at(index))));
            trigger["give_ship"]["model"] = tokens.at(2);
            if (tokens.size() == 4) {
                trigger["give_ship"]["name"] = tokens.at(3);
            }
        } else if (tokens.at(0).compare("payment") == 0) {
            qDebug("\tFound payment: %s", qUtf8Printable(QString::fromStdString(lines.at(index))));
            trigger["payment"]["is_active"] = true;
            if (tokens.size() > 1) {
                trigger["payment"]["base"] = tokens.at(1);
                if (tokens.size() == 3) {
                    trigger["payment"]["multiplier"] = tokens.at(2);
                }
            }
        } else if (tokens.at(0).compare("event") == 0) {
            qDebug("\tFound event: %s", qUtf8Printable(QString::fromStdString(lines.at(index))));
        } else if (tokens.at(0).compare("fail") == 0) {
            qDebug("\tFound fail: %s", qUtf8Printable(QString::fromStdString(lines.at(index))));
        } else if (tokens.at(0).compare("log") == 0 && tokens.size() == 2) {
            qDebug("\tFound log: %s", qUtf8Printable(QString::fromStdString(lines.at(index))));
        } else if (tokens.at(0).compare("log") == 0 && tokens.size() == 4) {
            qDebug("\tFound log: %s", qUtf8Printable(QString::fromStdString(lines.at(index))));
        } else if (isOneOf(tokens.at(1), {"=", "+=", "-="})) {
            qDebug("\tFound trigger condition: %s", qUtf8Printable(QString::fromStdString(lines.at(index))));
        } else if (isOneOf(tokens.at(1), {"++", "--"})) {
            qDebug("\tFound trigger condition: %s", qUtf8Printable(QString::fromStdString(lines.at(index))));
        } else if (isOneOf(tokens.at(0), {"set", "clear"})) {
            qDebug("\tFound trigger condition: %s", qUtf8Printable(QString::fromStdString(lines.at(index))));
        } else {
            qDebug("\tTrigger component not found: %s", qUtf8Printable(QString::fromStdString(lines.at(index))));
        }

        // handle getting the depth of the next line
        try {
            nxt = getIndentLevel(lines.at(index + 1));
        }  catch (const std::out_of_range& ex) {
            break;
        }
    }
    mission["triggers"].emplace_back(trigger);
    qDebug("\tTrigger data: %s", qUtf8Printable(QString::fromStdString(trigger.dump(4))));
    return index;
}

int FileMissionItemParser::parseConversation(std::vector<std::string> *missionLines, int startingIndex, json *trigger) {
    std::vector<std::string> lines = *missionLines;
    int index = startingIndex;
    json convo;

    qDebug("\tParsing conversation: %s", qUtf8Printable(QString::fromStdString(lines.at(index))));
    int cur = getIndentLevel(lines.at(index));
    int nxt = getIndentLevel(lines.at(index + 1));
    while (true) {
        if (nxt <= cur) {
            break;
        }
        index++;

        std::vector<std::string> tokens = tokenize(lines.at(index));
        qDebug("\tLine in conversation: %s", qUtf8Printable(QString::fromStdString(lines.at(index))));
        // TODO: add parsing for conversations
        convo.emplace_back(lines.at(index));

        // handle getting the depth of the next line
        try {
            nxt = getIndentLevel(lines.at(index + 1));
        }  catch (const std::out_of_range& ex) {
            break;
        }
    }
    (*trigger)["conversation"].emplace_back(convo);
    //qDebug("\tConversation data: %s", qUtf8Printable(QString::fromStdString((*trigger)["conversation"].dump())));
    return index;
}

int FileMissionItemParser::parseDialog(std::vector<std::string> *missionLines, int startingIndex, json *trigger) {
    std::vector<std::string> lines = *missionLines;
    int index = startingIndex;
    json dialog;

    // Check if dialog is phrase, single line, or multiline
    std::vector<std::string> tokens = tokenize(lines.at(index));
    if (tokens.size() == 3) {
        qDebug("\tFound dialog phrase: %s", qUtf8Printable(QString::fromStdString(lines.at(index))));
        (*trigger)["dialog_phrase"].emplace_back(tokens.at(2));
       // qDebug("\tDialog phrase data: %s", qUtf8Printable(QString::fromStdString((*trigger)["dialog_phrase"].dump(4))));
        return startingIndex;
    } else if (tokens.size() == 2) {
        qDebug("\tFound dialog: %s", qUtf8Printable(QString::fromStdString(lines.at(index))));
        (*trigger)["dialog"].emplace_back(tokens.at(1));
    } else {
        qDebug("\tParsing complex dialog node: %s", qUtf8Printable(QString::fromStdString(lines.at(index))));
        int cur = getIndentLevel(lines.at(index));
        int nxt = getIndentLevel(lines.at(index + 1));
        while (true) {
            if (nxt <= cur) {
                break;
            }
            index++;

            std::vector<std::string> tokens = tokenize(lines.at(index));
            qDebug("\tLine in dialog: %s", qUtf8Printable(QString::fromStdString(lines.at(index))));
            // TODO: handle inline phrase declarations
            //  dialog
            //      phrase
            //          ...
            dialog.emplace_back(lines.at(index));

            // handle getting the depth of the next line
            try {
                nxt = getIndentLevel(lines.at(index + 1));
            }  catch (const std::out_of_range& ex) {
                break;
            }
        }
        (*trigger)["dialog"].emplace_back(dialog);
    }
    //qDebug("\tDialog data: %s", qUtf8Printable(QString::fromStdString((*trigger)["dialog"].dump(4))));
    return index;
}
