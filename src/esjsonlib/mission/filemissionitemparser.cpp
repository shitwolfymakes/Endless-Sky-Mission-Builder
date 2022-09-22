// SPDX-License-Identifier: GPL-3.0-only
/*
 * filemissionitemparser.cpp
 *
 * Copyright (c) 2021, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "filemissionitemparser.h"

FileMissionItemParser::FileMissionItemParser(std::vector<std::string> lines)
{
    this->lines = lines;
}

json FileMissionItemParser::run() {
    // for self.i, self.line in self.enum_lines:
    // for line in ItemMission->lines
    std::vector<std::string> tokens;
    for (int i = 0; i < static_cast<int>(lines.size()); i++) {
        // start by tokenizing each line
        tokens = tokenize(lines.at(i));
        //std::cout << "LINE: " << tokens.at(0) << std::endl;

        if (tokens.size() == 0) {
            std::cout << "\tERROR: NO TOKENS FOUND ON LINE: " << lines.at(i) << std::endl;
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
                std::cout << "COMPLEX WAYPOINT HANDLING NOT YET IMPLEMENTED" << std::endl;
                continue;
            }
        }
        else if (tokens.at(0).compare("stopover") == 0) {
            if (tokens.size() == 2) {
                parseStopover(tokens.at(1));
            } else {
                // TODO: convert this to handle filters the same way parseTrigger works
                // e.g. i = parseNodeWithFilter(&lines, i);
                std::cout << "COMPLEX STOPOVER HANDLING NOT YET IMPLEMENTED" << std::endl;
                continue;
            }
        }
        else if (tokens.at(0).compare("substitutions") == 0) {
            i = parseSubstitutions(&lines, i);
        }
        else if (tokens.at(0).compare("source") == 0) {
            if (tokens.size() == 2) {
                parseSource(tokens.at(1));
            } else {
                // TODO: convert this to handle filters the same way parseTrigger works
                // e.g. i = parseNodeWithFilter(&lines, i);
                std::cout << "COMPLEX SOURCE HANDLING NOT YET IMPLEMENTED" << std::endl;
                continue;
            }
        }
        else if (tokens.at(0).compare("destination") == 0) {
            if (tokens.size() == 2) {
                parseDestination(tokens.at(1));
            } else {
                // TODO: convert this to handle filters the same way parseTrigger works
                // e.g. i = parseNodeWithFilter(&lines, i);
                std::cout << "COMPLEX DESTINATION HANDLING NOT YET IMPLEMENTED" << std::endl;
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
            std::cout << "\tERROR - No tokens found in line: " << lines.at(i) << std::endl;
        }
    }
    //std::cout << "Mission data: " << mission.dump(4) << std::endl;
    return mission;
}

void FileMissionItemParser::parseId(std::vector<std::string> tokens) {
    std::cout << "\tMission ID is: " << tokens.at(1) << std::endl;
    mission["id"] = tokens.at(1);
}

void FileMissionItemParser::parseName(std::vector<std::string> tokens) {
    std::cout << "\tMission mission display name is: " << tokens.at(1) << std::endl;
    mission["name"] = tokens.at(1);
}

void FileMissionItemParser::parseDescription(std::vector<std::string> tokens) {
    std::cout << "\tFound description: " << tokens.at(1) << std::endl;
    mission["description"] = tokens.at(1);
}

void FileMissionItemParser::parseBlocked(std::vector<std::string> tokens) {
    std::cout << "\tFound blocked: " << tokens.at(1) << std::endl;
    mission["blocked"] = tokens.at(1);
}

void FileMissionItemParser::parseDeadline(std::vector<std::string> tokens) {
    std::cout << "\tFound deadline: " << boost::join(tokens, " ") << std::endl;
    mission["deadline"]["is_active"] = true;
    if (tokens.size() > 1) {
        mission["deadline"]["days"] = std::stoi(tokens.at(1));
        if (tokens.size() == 3) {
            mission["deadline"]["multiplier"] = std::stoi(tokens.at(2));
        }
    }
}

void FileMissionItemParser::parseCargo(std::vector<std::string> tokens) {
    std::cout << "\tFound cargo: " << boost::join(tokens, " ") << std::endl;
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
    std::cout << "\tFound passengers: " << boost::join(tokens, " ") << std::endl;
    mission["passengers"]["passengers"] = std::stoi(tokens.at(1));
    if (tokens.size() > 2) {
        mission["passengers"]["passengers_range"] = std::stoi(tokens.at(2));
        if (tokens.size() == 4) {
            mission["passengers"]["probability"] = std::stod(tokens.at(3));
        }
    }
}

void FileMissionItemParser::parseIllegal(std::vector<std::string> tokens) {
    std::cout << "\tFound illegal: " << boost::join(tokens, " ") << std::endl;
    mission["illegal"]["fine"] = std::stoi(tokens.at(1));
    if (tokens.size() == 3) {
        mission["illegal"]["message"] = tokens.at(2);
    }
}

void FileMissionItemParser::parseStealth() {
    std::cout << "\tFound stealth field" << std::endl;
    mission["stealth"] = true;
}

void FileMissionItemParser::parseInvisible() {
    std::cout << "\tFound invisible field" << std::endl;
    mission["invisible"] = true;
}

void FileMissionItemParser::parsePriorityLevel(std::string token) {
    std::cout << "\tFound priority level: " << token << std::endl;
    mission["priority_level"] = token;
}

void FileMissionItemParser::parseWhereShown(std::string token) {
    std::cout << "\tFound where shown: " << token << std::endl;
    mission["where_shown"] = token;
}

void FileMissionItemParser::parseRepeat(std::vector<std::string> tokens) {
    std::cout << "\tFound repeat: " << boost::join(tokens, " ") << std::endl;
    mission["repeat"]["is_active"] = true;
    if (tokens.size() == 2) {
        mission["repeat"]["amount"] = std::stoi(tokens.at(1));
    }
}

void FileMissionItemParser::parseClearance(std::vector<std::string> tokens) {
    std::cout << "\tFound clearance: " << boost::join(tokens, " ") << std::endl;
    mission["clearance"]["is_active"] = true;
    if (tokens.size() == 2) {
        mission["clearance"]["message"] = tokens.at(1);
    }
}

void FileMissionItemParser::parseInfiltrating() {
    std::cout << "\tFound infiltrating field" << std::endl;
    mission["infiltrating"] = true;
}

void FileMissionItemParser::parseWaypoint(std::string token) {
    std::cout << "\tFound waypoint: " << token << std::endl;
    json waypoint;
    waypoint["system"] = token;
    mission["waypoints"].emplace_back(waypoint);
}

void FileMissionItemParser::parseStopover(std::string token) {
    std::cout << "\tFound stopover: " << token << std::endl;
    json stopover;
    stopover["planet"] = token;
    mission["stopovers"].emplace_back(stopover);
}

int FileMissionItemParser::parseSubstitutions(std::vector<std::string> *missionLines, int startingIndex) {
    std::vector<std::string> lines = *missionLines;
    int index = startingIndex;
    json substitutions;
    json nodeLines;

    std::cout << "\tFound substitution: " << index << std::endl;

    // pass the missionLines, index, and address to a json object that will store the parsed JSON data
    index = collectNodeLines(missionLines, index, &nodeLines);

    // instantiate and run the substitution parser
    FileSubstitutionsItemParser parser = FileSubstitutionsItemParser(nodeLines);
    substitutions = parser.run();

    // store the json data
    mission["substitutions"] = substitutions;

    return index;
}

void FileMissionItemParser::parseSource(std::string token) {
    std::cout << "\tFound source: " << token << std::endl;
    mission["source"] = token;
}

void FileMissionItemParser::parseDestination(std::string token) {
    std::cout << "\tFound destination: " << token << std::endl;
    mission["destination"] = token;
}

int FileMissionItemParser::parseTrigger(std::vector<std::string> *missionLines, int startingIndex) {
    std::vector<std::string> lines = *missionLines;
    int index = startingIndex;
    json trigger; // create a json obect to store trigger data, pass ref to this when necessary

    std::string triggerType = tokenize(lines.at(index)).at(1);
    std::cout << "\tFound trigger: " << triggerType << std::endl;

    // check to prevent multiple triggers of the same type (except for on enter)
    for (auto& t: mission["triggers"]) {
        if (triggerType.compare("enter") == 0) {
            break;
        } else if (triggerType.compare(t["type"]) == 0) {
            std::cout << "\tERROR: second trigger using: " << triggerType << ", skipping..." << std::endl;
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
            std::cout << "\tFound log: " << lines.at(index) << std::endl;
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
            parsePayment(tokens, &trigger);
        } else if (tokens.at(0).compare("fine") == 0) {
            parseFine(tokens.at(1), &trigger);
        }
        // TODO: Add support for Value Expressions
        // https://github.com/endless-sky/endless-sky/wiki/Player-Conditions#value-expressions
        else if (isOneOf(tokens.at(1), {"=", "+=", "-="})) {
            parseTriggerConditionType1(tokens, &trigger);
        } else if (isOneOf(tokens.at(1), {"++", "--"})) {
            parseTriggerConditionType2(tokens, &trigger);
        } else if (isOneOf(tokens.at(0), {"set", "clear"})) {
            parseTriggerConditionType3(tokens, &trigger);
        } else if (tokens.at(0).compare("event") == 0) {
            parseEvent(tokens, &trigger);
        } else if (tokens.at(0).compare("fail") == 0) {
            parseFail(tokens, &trigger);
        } else {
            std::cout << "\tTrigger component not found: " << lines.at(index) << std::endl;
        }

        // handle getting the depth of the next line
        try {
            nxt = getIndentLevel(lines.at(index + 1));
        }  catch (const std::out_of_range& ex) {
            break;
        }
    }
    mission["triggers"].emplace_back(trigger);
    //std::cout << "\tTrigger data: " << trigger.dump(4) << std::endl;
    return index;
}

void FileMissionItemParser::parseLog(std::vector<std::string> tokens, json *trigger) {
    std::cout << "\tFound log: " << boost::join(tokens, " ") << std::endl;
    json log;
    log["category"] = tokens.at(1);
    log["header"] = tokens.at(2);
    log["text"] = tokens.at(3);
    (*trigger)["logs"].emplace_back(log);
}

void FileMissionItemParser::parseLog(std::string token, json *trigger) {
    std::cout << "\tFound log: " << token << std::endl;
    json log;
    log["text"] = token;
    (*trigger)["logs"].emplace_back(log);
}

int FileMissionItemParser::parseConversation(std::vector<std::string> *missionLines, int startingIndex, json *trigger) {
    std::vector<std::string> lines = *missionLines;
    int index = startingIndex;
    json convo;

    std::cout << "\tParsing conversation: " << lines.at(index) << std::endl;
    int cur = getIndentLevel(lines.at(index));
    int nxt = getIndentLevel(lines.at(index + 1));
    while (true) {
        if (nxt <= cur) {
            break;
        }
        index++;

        std::vector<std::string> tokens = tokenize(lines.at(index));
        std::cout << "\tLine in conversation: " << lines.at(index) << std::endl;
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
    //std::cout << "\tConversation data: " << (*trigger)["conversation"].dump(4) << std::endl;
    return index;
}

int FileMissionItemParser::parseDialog(std::vector<std::string> *missionLines, int startingIndex, json *trigger) {
    std::vector<std::string> lines = *missionLines;
    int index = startingIndex;
    json dialog;

    // Check if dialog is phrase
    std::vector<std::string> tokens = tokenize(lines.at(index));
    if (tokens.size() == 3) {
        std::cout << "\tFound dialog phrase: " << lines.at(index) << std::endl;
        (*trigger)["dialog_phrase"].emplace_back(tokens.at(2));
        return startingIndex;
    } else {
        std::cout << "\tFound dialog: " << lines.at(index) << std::endl;
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
            std::cout << "\tParsing complex dialog node..." << std::endl;

            std::vector<std::string> tokens = tokenize(lines.at(index));
            std::cout << "\tLine in dialog node: " << lines.at(index) << std::endl;
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
    //std::cout << "\tDialog data: " << (*trigger)["dialog"].dump(4) << std::endl;
    return index;
}

void FileMissionItemParser::parseOutfit(std::vector<std::string> tokens, json *trigger) {
    std::cout << "\tFound outfit: " << boost::join(tokens, " ") << std::endl;
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
    std::cout << "\tFound require: " << boost::join(tokens, " ") << std::endl;
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
    std::cout << "\tFound give ship: " << boost::join(tokens, " ") << std::endl;
    json give_ship;
    give_ship["model"] = tokens.at(2);
    if (tokens.size() == 4) {
        give_ship["name"] = tokens.at(3);
    }
    (*trigger)["give_ships"].emplace_back(give_ship);
}

void FileMissionItemParser::parsePayment(std::vector<std::string> tokens, json *trigger) {
    std::cout << "\tFound payment: " << boost::join(tokens, " ") << std::endl;
    json payment;
    payment["is_active"] = true;
    if (tokens.size() > 1) {
        payment["base"] = std::stoi(tokens.at(1));
        if (tokens.size() == 3) {
            payment["multiplier"] = std::stoi(tokens.at(2));
        }
    }
    (*trigger)["payment"] = payment;
}

void FileMissionItemParser::parseFine(std::string token, json *trigger) {
    std::cout << "\tFound fine: " << token << std::endl;
    (*trigger)["fine"] = std::stoi(token);
}

void FileMissionItemParser::parseTriggerConditionType1(std::vector<std::string> tokens, json *trigger) {
    std::cout << "\tFound trigger condition: " << boost::join(tokens, "") << std::endl;
    json conditionSet;
    conditionSet["condition"] = tokens.at(0);
    conditionSet["operand"] = tokens.at(1);
    // easier to leave as a string during ingest instead of checking if it's a double or int
    conditionSet["value"] = tokens.at(2);

    (*trigger)["condition_sets"].emplace_back(conditionSet);
}

void FileMissionItemParser::parseTriggerConditionType2(std::vector<std::string> tokens, json *trigger) {
    std::cout << "\tFound trigger condition: " << boost::join(tokens, "") << std::endl;
    json conditionSet;
    conditionSet["condition"] = tokens.at(0);
    conditionSet["operand"] = tokens.at(1);

    (*trigger)["condition_sets"].emplace_back(conditionSet);
}

void FileMissionItemParser::parseTriggerConditionType3(std::vector<std::string> tokens, json *trigger) {
    std::cout << "\tFound trigger condition: " << boost::join(tokens, "") << std::endl;
    json conditionSet;
    conditionSet["tag"] = tokens.at(0);
    conditionSet["condition"] = tokens.at(1);

    (*trigger)["condition_sets"].emplace_back(conditionSet);
}

void FileMissionItemParser::parseEvent(std::vector<std::string> tokens, json *trigger) {
    std::cout << "\tFound event: " << boost::join(tokens, " ") << std::endl;
    json event;
    event["name"] = tokens.at(1);
    if (tokens.size() > 2) {
        event["delay"] = std::stoi(tokens.at(2));
        if (tokens.size() == 4) {
            event["max_delay"] = std::stoi(tokens.at(3));
        }
    }
    (*trigger)["events"].emplace_back(event);
}

void FileMissionItemParser::parseFail(std::vector<std::string> tokens, json *trigger) {
    std::cout << "\tFound fail: " << boost::join(tokens, " ") << std::endl;
    if (tokens.size() == 2) {
        (*trigger)["fails"].emplace_back(tokens.at(1));
    } else {
        (*trigger)["fails"].emplace_back(get_mission_id());
    }
}

int FileMissionItemParser::parseCondition(std::vector<std::string> *missionLines, int startingIndex) {
    std::vector<std::string> lines = *missionLines;
    int index = startingIndex;
    json condition;

    std::string conditionType = tokenize(lines.at(index)).at(1);
    std::cout << "\tParsing condition: " << lines.at(index) << std::endl;

    // check to prevent multiple conditions of the same type
    for (auto& t: mission["conditions"]) {
        if (conditionType.compare(t["type"]) == 0) {
            std::cout << "\tERROR: second condition using: " << conditionType << ", skipping..." << std::endl;
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
        std::cout << "\tLine in condition: " << lines.at(index) << std::endl;
        condition["data"].emplace_back(lines.at(index));

        // handle getting the depth of the next line
        try {
            nxt = getIndentLevel(lines.at(index + 1));
        }  catch (const std::out_of_range& ex) {
            break;
        }
    }
    mission["conditions"].emplace_back(condition);
    //std::cout << "\tCondition data: " << condition.dump(4) << std::endl;
    return index;
}

int FileMissionItemParser::parseNpc(std::vector<std::string> *missionLines, int startingIndex) {
    std::vector<std::string> lines = *missionLines;
    int index = startingIndex;
    json npc;

    std::cout << "\tParsing NPC: " << lines.at(index) << std::endl;
    // TODO: store the npc tags without storing duplicates

    int cur = getIndentLevel(lines.at(index));
    int nxt = getIndentLevel(lines.at(index + 1));
    while (true) {
        if (nxt <= cur) {
            break;
        }
        index++;

        std::vector<std::string> tokens = tokenize(lines.at(index));
        std::cout << "\tLine in npc: " << lines.at(index) << std::endl;
        npc["data"].emplace_back(lines.at(index));

        // handle getting the depth of the next line
        try {
            nxt = getIndentLevel(lines.at(index + 1));
        }  catch (const std::out_of_range& ex) {
            break;
        }
    }
    mission["npcs"].emplace_back(npc);
    //std::cout << "\tNPC data: " << npc.dump(4) << std::endl;
    return index;
}

void FileMissionItemParser::set_mission_id(std::string id) {
    mission["id"] = id;
}

json FileMissionItemParser::get_data() const {
    return mission;
}

std::string FileMissionItemParser::get_mission_id() const {
    return mission["id"];
}
