// SPDX-License-Identifier: GPL-3.0-only
/*
 * itemmission.cpp
 *
 * Copyright (c) 2021, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "itemmission.h"

ItemMission::ItemMission()
{

}

void ItemMission::parse() {
    // TODO: Implement this
    qDebug() << "parsing mission item to JSON";
    // for self.i, self.line in self.enum_lines:
    // for line in ItemMission->lines

    vector<string> tokens;
    for (const string &line: lines) {
        // start by tokenizing each line
        tokens = tokenize(line);

        if (tokens.size() == 0) {
            QString qLine = QString::fromStdString(line);
            qDebug("\tERROR: NO TOKENS FOUND ON LINE: %s", qUtf8Printable(qLine));
        }
        else if (tokens.at(0).compare("mission") == 0) {
            setName(tokens.at(1));
            qDebug("\tMission ID is: %s", qUtf8Printable(QString::fromStdString(tokens.at(1))));
        }
        else if (tokens.at(0).compare("name") == 0) {
            // this will get nabbed and crash if name token appears inside a conversation block
            if (tokens.size() != 2) { continue; }
            qDebug("\tFound mission display name: %s", qUtf8Printable(QString::fromStdString(tokens.at(1))));
        }
        else if (tokens.at(0).compare("description") == 0) {
            qDebug("\tFound description: %s", qUtf8Printable(QString::fromStdString(tokens.at(1))));
        }
        else if (tokens.at(0).compare("blocked") == 0) {
            qDebug("\tFound blocked: %s", qUtf8Printable(QString::fromStdString(tokens.at(1))));
        }
        else if (tokens.at(0).compare("deadline") == 0) {
            qDebug("\tFound deadline: %s", qUtf8Printable(QString::fromStdString(line)));
        }
        else if (tokens.at(0).compare("cargo") == 0) {
            qDebug("\tFound cargo: %s", qUtf8Printable(QString::fromStdString(line)));
        }
        else if (tokens.at(0).compare("passengers") == 0) {
            qDebug("\tFound passengers: %s", qUtf8Printable(QString::fromStdString(line)));
        }
        else if (tokens.at(0).compare("illegal") == 0) {
            qDebug("\tFound illegal: %s", qUtf8Printable(QString::fromStdString(line)));
        }
        else if (tokens.at(0).compare("stealth") == 0) {
            qDebug("\tFound stealth");
        }
        else if (tokens.at(0).compare("invisible") == 0) {
            qDebug("\tFound invisible");
        }
        else if (isOneOf(tokens.at(0), {"priority", "minor"})) {
            qDebug("\tFound priority: %s", qUtf8Printable(QString::fromStdString(tokens.at(0))));
        }
        else if (isOneOf(tokens.at(0), {"job", "landing", "assisting", "boarding"})) {
            qDebug("\tFound where shown: %s", qUtf8Printable(QString::fromStdString(tokens.at(0))));
        }
        else if (tokens.at(0).compare("repeat") == 0) {
            qDebug("\tFound repeat: %s", qUtf8Printable(QString::fromStdString(line)));
        }
        else if (tokens.at(0).compare("clearance") == 0) {
            qDebug("\tFound clearance: %s", qUtf8Printable(QString::fromStdString(tokens.at(1))));
        }
        else if (tokens.at(0).compare("infiltrating") == 0) {
            qDebug("\tFound infiltrating");
        }
        else if (tokens.at(0).compare("waypoint") == 0) {
            qDebug("\tFound waypoint: %s", qUtf8Printable(QString::fromStdString(tokens.at(1))));
        }
        else if (tokens.at(0).compare("stopover") == 0) {
            qDebug("\tFound stopover: %s", qUtf8Printable(QString::fromStdString(tokens.at(1))));
        }
        else if (tokens.at(0).compare("source") == 0) {
            if (tokens.size() == 2) {
                qDebug("\tFound source: %s", qUtf8Printable(QString::fromStdString(tokens.at(1))));
            } else {
                qDebug("COMPLEX SOURCE HANDLING NOT YET IMPLEMENTED");
            }
        }
        else if (tokens.at(0).compare("destination") == 0) {
            qDebug("\tFound destionation: %s", qUtf8Printable(QString::fromStdString(tokens.at(1))));
        }
        // elif "on" in tokens
        // elif "to" in tokens
        // elif "npc" in tokens
        // else error
    }
    qDebug() << "finished parsing mission";
}
