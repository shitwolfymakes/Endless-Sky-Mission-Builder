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

json FileMissionItemParser::run() {
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
            // TODO: convert this to handle filters the same way parseTrigger works
            // e.g. i = parseNodeWithFilter(&lines, i);
            parseClearance(tokens);
        }
        else if (tokens.at(0).compare("infiltrating") == 0) {
            parseInfiltrating();
        }
        else if (tokens.at(0).compare("waypoint") == 0) {
            if (tokens.size() == 2) {
                parseWaypoint(tokens.at(1));
            } else {
                // TODO: convert this to handle filters the same way parseTrigger works
                // e.g. i = parseNodeWithFilter(&lines, i);
                qDebug("COMPLEX WAYPOINT HANDLING NOT YET IMPLEMENTED");
                continue;
            }
        }
        else if (tokens.at(0).compare("stopover") == 0) {
            if (tokens.size() == 2) {
                parseStopover(tokens.at(1));
            } else {
                // TODO: convert this to handle filters the same way parseTrigger works
                // e.g. i = parseNodeWithFilter(&lines, i);
                qDebug("COMPLEX STOPOVER HANDLING NOT YET IMPLEMENTED");
                continue;
            }
        }
        else if (tokens.at(0).compare("source") == 0) {
            if (tokens.size() == 2) {
                parseSource(tokens.at(1));
            } else {
                // TODO: convert this to handle filters the same way parseTrigger works
                // e.g. i = parseNodeWithFilter(&lines, i);
                qDebug("COMPLEX SOURCE HANDLING NOT YET IMPLEMENTED");
                continue;
            }
        }
        else if (tokens.at(0).compare("destination") == 0) {
            if (tokens.size() == 2) {
                parseDestination(tokens.at(1));
            } else {
                // TODO: convert this to handle filters the same way parseTrigger works
                // e.g. i = parseNodeWithFilter(&lines, i);
                qDebug("COMPLEX DESTINATION HANDLING NOT YET IMPLEMENTED");
                continue;
            }
        }
        // elif "on" in tokens (Trigger)
        else if (tokens.at(0).compare("on") == 0) {
            i = parseTrigger(&lines, i);
        }
        // elif "to" in tokens (Conditions)
        else if (tokens.at(0).compare("to") == 0) {
            i = parseCondition(&lines, i);
        }
        // elif "npc" in tokens
        else if (tokens.at(0).compare("npc") == 0) {
            i = parseNpc(&lines, i);
        }
        // else error
        else {
            qDebug("\tERROR - No tokens found in line: %s", qUtf8Printable(QString::fromStdString(lines.at(i))));
        }
    }
    // qDebug may occassionally truncate strings output, but the data is still there
    // (https://bugreports.qt.io/browse/QTCREATORBUG-24649)
    //qDebug("Mission data: %s", qUtf8Printable(QString::fromStdString(mission.dump(4))));
    return mission;
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
        mission["deadline"]["days"] = std::stoi(tokens.at(1));
        if (tokens.size() == 3) {
            mission["deadline"]["multiplier"] = std::stoi(tokens.at(2));
        }
    }
}

void FileMissionItemParser::parseCargo(std::vector<std::string> tokens) {
    qDebug("\tFound cargo: %s", qUtf8Printable(QString::fromStdString(boost::join(tokens, " "))));
    mission["cargo"]["cargo"] = tokens.at(1);
    mission["cargo"]["tonnage"] = std::stoi(tokens.at(2));
    if (tokens.size() > 3) {
        mission["cargo"]["tonnage_range"] = std::stoi(tokens.at(3));
        if (tokens.size() == 5) {
            mission["cargo"]["probability"] = std::stod(tokens.at(4));
        }
    }
}

void FileMissionItemParser::parsePassengers(std::vector<std::string> tokens) {
    qDebug("\tFound passengers: %s", qUtf8Printable(QString::fromStdString(boost::join(tokens, " "))));
    mission["passengers"]["passengers"] = std::stoi(tokens.at(1));
    if (tokens.size() > 2) {
        mission["passengers"]["passengers_range"] = std::stoi(tokens.at(2));
        if (tokens.size() == 4) {
            mission["passengers"]["probability"] = std::stod(tokens.at(3));
        }
    }
}

void FileMissionItemParser::parseIllegal(std::vector<std::string> tokens) {
    qDebug("\tFound illegal: %s", qUtf8Printable(QString::fromStdString(boost::join(tokens, " "))));
    mission["illegal"]["fine"] = std::stoi(tokens.at(1));
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
        mission["repeat"]["amount"] = std::stoi(tokens.at(1));
    }
}

void FileMissionItemParser::parseClearance(std::vector<std::string> tokens) {
    qDebug("\tFound clearance: %s", qUtf8Printable(QString::fromStdString(boost::join(tokens, " "))));
    mission["clearance"]["is_active"] = true;
    if (tokens.size() == 2) {
        mission["clearance"]["message"] = tokens.at(1);
    }
}

void FileMissionItemParser::parseInfiltrating() {
    qDebug("\tFound infiltrating field");
    mission["infiltrating"] = true;
}

void FileMissionItemParser::parseWaypoint(std::string token) {
    qDebug("\tFound waypoint: %s", qUtf8Printable(QString::fromStdString(token)));
    json waypoint;
    waypoint["system"] = token;
    mission["waypoints"].emplace_back(waypoint);
}

void FileMissionItemParser::parseStopover(std::string token) {
    qDebug("\tFound stopover: %s", qUtf8Printable(QString::fromStdString(token)));
    json stopover;
    stopover["planet"] = token;
    mission["stopovers"].emplace_back(stopover);
}

void FileMissionItemParser::parseSource(std::string token) {
    qDebug("\tFound source: %s", qUtf8Printable(QString::fromStdString(token)));
    mission["source"] = token;
}

void FileMissionItemParser::parseDestination(std::string token) {
    qDebug("\tFound destination: %s", qUtf8Printable(QString::fromStdString(token)));
    mission["destination"] = token;
}

int FileMissionItemParser::parseTrigger(std::vector<std::string> *missionLines, int startingIndex) {
    std::vector<std::string> lines = *missionLines;
    int index = startingIndex;
    json trigger; // create a json obect to store trigger data, pass ref to this when necessary

    std::string triggerType = tokenize(lines.at(index)).at(1);
    qDebug("\tFound trigger: %s", qUtf8Printable(QString::fromStdString(triggerType)));

    // check to prevent multiple triggers of the same type (except for on enter)
    for (auto& t: mission["triggers"]) {
        if (triggerType.compare("enter") == 0) {
            break;
        } else if (triggerType.compare(t["type"]) == 0) {
            qDebug("\tERROR: second trigger using: %s, skipping...",
                   qUtf8Printable(QString::fromStdString(triggerType)));
            int cur = getIndentLevel(lines.at(index));
            int nxt = getIndentLevel(lines.at(index + 1));
            while (true) {
                if (nxt <= cur) {
                    break;
                }
                index++;
                // handle getting the depth of the next line
                try {
                    nxt = getIndentLevel(lines.at(index + 1));
                }  catch (const std::out_of_range& ex) {
                    break;
                }
            }
            return index;
        }
    }

    trigger["type"] = triggerType;
    int cur = getIndentLevel(lines.at(index));
    int nxt = getIndentLevel(lines.at(index + 1));
    while (true) {
        if (nxt <= cur) {
            break;
        }

        index++;
        std::vector<std::string> tokens = tokenize(lines.at(index));
        // parse the content of this line in the trigger
        if (tokens.at(0).compare("log") == 0) {
            qDebug("\tFound log: %s", qUtf8Printable(QString::fromStdString(lines.at(index))));
            if (tokens.size() == 4) {
                parseLog(tokens, &trigger);
            } else {
                parseLog(tokens.at(1), &trigger);
            }
        } else if (tokens.at(0).compare("dialog") == 0) {
            index = parseDialog(missionLines, index, &trigger);
        } else if (tokens.at(0).compare("conversation") == 0) {
            index = parseConversation(missionLines, index, &trigger);
        } else if (tokens.at(0).compare("outfit") == 0) {
            parseOutfit(tokens, &trigger);
        } else if (tokens.at(0).compare("require") == 0) {
            parseRequire(tokens, &trigger);
        } else if (tokens.at(0).compare("give") == 0 && tokens.at(1).compare("ship") == 0) {
            parseGiveShip(tokens, &trigger);
        } else if (tokens.at(0).compare("payment") == 0) {
            qDebug("\tFound payment: %s", qUtf8Printable(QString::fromStdString(lines.at(index))));
            trigger["payment"]["is_active"] = true;
            if (tokens.size() > 1) {
                trigger["payment"]["base"] = tokens.at(1);
                if (tokens.size() == 3) {
                    trigger["payment"]["multiplier"] = tokens.at(2);
                }
            }
        } else if (tokens.at(0).compare("fine") == 0) {
            qDebug("\tFound fine: %s", qUtf8Printable(QString::fromStdString(lines.at(index))));
            trigger["fine"] = tokens.at(1);
        } else if (isOneOf(tokens.at(1), {"=", "+=", "-="})) {
            qDebug("\tFound trigger condition: %s", qUtf8Printable(QString::fromStdString(lines.at(index))));
        } else if (isOneOf(tokens.at(1), {"++", "--"})) {
            qDebug("\tFound trigger condition: %s", qUtf8Printable(QString::fromStdString(lines.at(index))));
        } else if (isOneOf(tokens.at(0), {"set", "clear"})) {
            qDebug("\tFound trigger condition: %s", qUtf8Printable(QString::fromStdString(lines.at(index))));
        } else if (tokens.at(0).compare("event") == 0) {
            qDebug("\tFound event: %s", qUtf8Printable(QString::fromStdString(lines.at(index))));
            trigger["event"]["name"] = tokens.at(1);
            if (tokens.size() > 2) {
                trigger["event"]["delay"] = tokens.at(2);
                if (tokens.size() == 4) {
                    trigger["event"]["max"] = tokens.at(3);
                }
            }
        } else if (tokens.at(0).compare("fail") == 0) {
            qDebug("\tFound fail: %s", qUtf8Printable(QString::fromStdString(lines.at(index))));
            trigger["fail"]["is_active"] = true;
            if (tokens.size() == 2) {
                trigger["fail"]["name"] = tokens.at(1);
            }
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

void FileMissionItemParser::parseLog(std::vector<std::string> tokens, json *trigger) {
    qDebug("\tFound log: %s", qUtf8Printable(QString::fromStdString(boost::join(tokens, " "))));
    json log;
    log["category"] = tokens.at(1);
    log["header"] = tokens.at(2);
    log["text"] = tokens.at(3);
    (*trigger)["logs"].emplace_back(log);
}

void FileMissionItemParser::parseLog(std::string token, json *trigger) {
    qDebug("\tFound log: %s", qUtf8Printable(QString::fromStdString(token)));
    json log;
    log["text"] = token;
    (*trigger)["logs"].emplace_back(log);
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
    qDebug("\tConversation data: %s", qUtf8Printable(QString::fromStdString((*trigger)["conversation"].dump())));
    return index;
}

int FileMissionItemParser::parseDialog(std::vector<std::string> *missionLines, int startingIndex, json *trigger) {
    std::vector<std::string> lines = *missionLines;
    int index = startingIndex;
    json dialog;

    // Check if dialog is phrase
    std::vector<std::string> tokens = tokenize(lines.at(index));
    if (tokens.size() == 3) {
        qDebug("\tFound dialog phrase: %s", qUtf8Printable(QString::fromStdString(lines.at(index))));
        (*trigger)["dialog_phrase"].emplace_back(tokens.at(2));
        return startingIndex;
    } else {
        qDebug("\tFound dialog: %s", qUtf8Printable(QString::fromStdString(lines.at(index))));
        dialog.emplace_back(tokens.at(1));

        // check if next line exists
        try {
            getIndentLevel(lines.at(index + 1));
        }  catch (const std::out_of_range& ex) {
            (*trigger)["dialog"].emplace_back(dialog);
            return index;
        }

        int cur = getIndentLevel(lines.at(index));
        int nxt = getIndentLevel(lines.at(index + 1));
        while (true) {
            if (nxt <= cur) {
                break;
            }
            index++;
            qDebug("\tParsing complex dialog node...");

            std::vector<std::string> tokens = tokenize(lines.at(index));
            qDebug("\tLine in dialog node: %s", qUtf8Printable(QString::fromStdString(lines.at(index))));
            // TODO: handle inline phrase declarations
            //  dialog
            //      phrase
            //          ...
            if (tokens.at(0).compare("phrase") == 0) {
                break;
            }
            dialog.emplace_back(tokens.at(0));

            // handle getting the depth of the next line
            try {
                nxt = getIndentLevel(lines.at(index + 1));
            }  catch (const std::out_of_range& ex) {
                break;
            }
        }
        (*trigger)["dialog"].emplace_back(dialog);
    }
    qDebug("\tDialog data: %s", qUtf8Printable(QString::fromStdString((*trigger)["dialog"].dump(4))));
    return index;
}

void FileMissionItemParser::parseOutfit(std::vector<std::string> tokens, json *trigger) {
    qDebug("\tFound outfit: %s", qUtf8Printable(QString::fromStdString(boost::join(tokens, " "))));
    json outfit;
    outfit["name"] = tokens.at(1);
    if (tokens.size() == 3) {
        int quantity = std::stoi(tokens.at(2));
        if (quantity != 0) {
            outfit["quantity"] = quantity;
        } else {
            // Silently fix deprecated usage
            parseRequire({"require", tokens.at(1)}, trigger);
        }
    }
    (*trigger)["outfits"].emplace_back(outfit);
}

void FileMissionItemParser::parseRequire(std::vector<std::string> tokens, json *trigger) {
    // TODO: record negative quantity as invalid
    qDebug("\tFound require: %s", qUtf8Printable(QString::fromStdString(boost::join(tokens, " "))));
    json require;
    require["name"] = tokens.at(1);
    if (tokens.size() == 3) {
        int quantity = std::stoi(tokens.at(2));
        if (quantity != 1) {
            require["quantity"] = quantity;
        }
    }
    (*trigger)["requires"].emplace_back(require);
}

void FileMissionItemParser::parseGiveShip(std::vector<std::string> tokens, json *trigger) {
    qDebug("\tFound give ship: %s", qUtf8Printable(QString::fromStdString(boost::join(tokens, " "))));
    json give_ship;
    give_ship["model"] = tokens.at(2);
    if (tokens.size() == 4) {
        give_ship["name"] = tokens.at(3);
    }
    (*trigger)["give_ship"].emplace_back(give_ship);
}

int FileMissionItemParser::parseCondition(std::vector<std::string> *missionLines, int startingIndex) {
    std::vector<std::string> lines = *missionLines;
    int index = startingIndex;
    json condition;

    std::string conditionType = tokenize(lines.at(index)).at(1);
    qDebug("\tParsing condition: %s", qUtf8Printable(QString::fromStdString(lines.at(index))));

    // check to prevent multiple conditions of the same type
    for (auto& t: mission["conditions"]) {
        if (conditionType.compare(t["type"]) == 0) {
            qDebug("\tERROR: second condition using: %s, skipping...",
                   qUtf8Printable(QString::fromStdString(conditionType)));
            int cur = getIndentLevel(lines.at(index));
            int nxt = getIndentLevel(lines.at(index + 1));
            while (true) {
                if (nxt <= cur) {
                    break;
                }
                index++;
                // handle getting the depth of the next line
                try {
                    nxt = getIndentLevel(lines.at(index + 1));
                }  catch (const std::out_of_range& ex) {
                    break;
                }
            }
            return index;
        }
    }

    condition["type"] = conditionType;
    int cur = getIndentLevel(lines.at(index));
    int nxt = getIndentLevel(lines.at(index + 1));
    while (true) {
        if (nxt <= cur) {
            break;
        }
        index++;

        std::vector<std::string> tokens = tokenize(lines.at(index));
        qDebug("\tLine in condition: %s", qUtf8Printable(QString::fromStdString(lines.at(index))));
        condition["data"].emplace_back(lines.at(index));

        // handle getting the depth of the next line
        try {
            nxt = getIndentLevel(lines.at(index + 1));
        }  catch (const std::out_of_range& ex) {
            break;
        }
    }
    mission["conditions"].emplace_back(condition);
    qDebug("\tCondition data: %s", qUtf8Printable(QString::fromStdString(condition.dump(4))));
    return index;
}

int FileMissionItemParser::parseNpc(std::vector<std::string> *missionLines, int startingIndex) {
    std::vector<std::string> lines = *missionLines;
    int index = startingIndex;
    json npc;

    qDebug("\tParsing NPC: %s", qUtf8Printable(QString::fromStdString(lines.at(index))));
    // TODO: store the npc tags without storing duplicates

    int cur = getIndentLevel(lines.at(index));
    int nxt = getIndentLevel(lines.at(index + 1));
    while (true) {
        if (nxt <= cur) {
            break;
        }
        index++;

        std::vector<std::string> tokens = tokenize(lines.at(index));
        qDebug("\tLine in npc: %s", qUtf8Printable(QString::fromStdString(lines.at(index))));
        npc["data"].emplace_back(lines.at(index));

        // handle getting the depth of the next line
        try {
            nxt = getIndentLevel(lines.at(index + 1));
        }  catch (const std::out_of_range& ex) {
            break;
        }
    }
    mission["npcs"].emplace_back(npc);
    qDebug("\tNPC data: %s", qUtf8Printable(QString::fromStdString(npc.dump(4))));
    return index;
}

json FileMissionItemParser::get_mission() {
    return mission;
}
