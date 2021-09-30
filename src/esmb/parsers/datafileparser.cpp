// SPDX-License-Identifier: GPL-3.0-only
/*
 * datafileparser.cpp
 *
 * Copyright (c) 2021, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "datafileparser.h"

DataFileParser::DataFileParser(QString rawData)
    : qLines(rawData.split("\n")),
      lines(toStdStringVector())
{
    this->rawData = rawData;
    //printRawData();
}

std::vector<std::string> DataFileParser::toStdStringVector() {
    std::vector<std::string> lines;
    for(const QString &line: qLines) {
        lines.push_back(line.toStdString());
    }
    return lines;
}

void DataFileParser::printRawData() {
    qDebug() << "BEGIN RAW DATA";
    for(const QString &line: qLines){
        //need to use qUtf8Printable to preserve the formatting
        qDebug("%s", qUtf8Printable(line));
    }
    qDebug() << "END RAW DATA";
}

void DataFileParser::run() {
    qDebug() << "Parsing data file...";
    int i = 0;
    for (const std::string &line: lines) {
        // account for whitespace between file items
        if (line == "") {
            i++;
            continue;
        }

        // search for lines starting file items
        if (std::regex_match(line, matchEvent))
        {
            QString qLine = QString::fromStdString(line);
            qDebug("\tEVENT FOUND: %s", qUtf8Printable(qLine));
            storeItemForParsing(i, line, Event);
        }
        else if (std::regex_match(line, matchGovernment)) {
            QString qLine = QString::fromStdString(line);
            qDebug("\tGOVERNMENT FOUND: %s", qUtf8Printable(qLine));
            storeItemForParsing(i, line, Government);
        }
        else if (std::regex_match(line, matchMission)) {
            QString qLine = QString::fromStdString(line);
            qDebug("\tMISSION FOUND: %s", qUtf8Printable(qLine));
            storeItemForParsing(i, line, Mission);
        }
        else if (std::regex_match(line, matchPhrase)) {
            QString qLine = QString::fromStdString(line);
            qDebug("\tPHRASE FOUND: %s", qUtf8Printable(qLine));
            storeItemForParsing(i, line, Phrase);
        }
        else if (std::regex_match(line, matchShip)) {
            QString qLine = QString::fromStdString(line);
            qDebug("\tSHIP FOUND: %s", qUtf8Printable(qLine));
            storeItemForParsing(i, line, Ship);
        }

        i++;
    }

    for (const auto &item: fileItems) {
        item->printItem();
    }
}

void DataFileParser::storeItemForParsing(int i, std::string line, ItemType itemType) {
    FileItem *fileItem;
    switch (itemType) {
        case Event :
            fileItem = new ItemEvent();
            break;
        case Government :
            ;
        case Mission :
            ;
        case Phrase :
            ;
        case Ship :
            ;
        default:
            fileItem = new ItemEvent();
    }
    fileItem->appendLine(line);

    // safer to cast i to size_t as the loop calling this only increments,
    // whereas the mission file could in theory have more than MAX_INT
    // number of lines
    i += 1;
    for (size_t j = i; j < lines.size(); j++) {
        const std::string line = lines.at(j);
        if (isFileItemStartLine(line)) {
            // check if current line is the start of a new FileItem
            // add the fileItem to the list of FileItems
            fileItems.push_back(std::unique_ptr<FileItem>(fileItem));
            return;
        } else if (line == "") {
            // if the current line is blank
            // add the fileItem to the list of FileItems
            fileItems.push_back(std::unique_ptr<FileItem>(fileItem));
            return;
        } else {
            fileItem->appendLine(line);
        }
    }
}

bool DataFileParser::isFileItemStartLine(std::string line) {
    // search for lines starting file items
    if (std::regex_match(line, matchEvent)) {
        return true;
    } else if (std::regex_match(line, matchGovernment)) {
        return true;
    } else if (std::regex_match(line, matchMission)) {
        return true;
    } else if (std::regex_match(line, matchPhrase)) {
        return true;
    } else if (std::regex_match(line, matchShip)) {
        return true;
    }
    return false;
}
