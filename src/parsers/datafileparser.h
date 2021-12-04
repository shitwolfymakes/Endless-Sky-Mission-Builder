// SPDX-License-Identifier: GPL-3.0-only
/*
 * datafileparser.h
 *
 * Copyright (c) 2021, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef DATAFILEPARSER_H
#define DATAFILEPARSER_H

#include <regex>
#include <string>
#include <vector>

#include <QDebug>
#include <QString>
#include <QStringList>
#include "boost/algorithm/string/join.hpp"

#include "model/fileitem.h"
#include "model/itemevent.h"
#include "model/itemgovernment.h"
#include "model/itemmission.h"
#include "model/itemphrase.h"
#include "model/itemship.h"
#include "model/fileitemconstants.h"

class DataFileParser
{
private:
    // store the file data in different formats
    QString rawData;
    const QStringList qLines;
    const std::vector<std::string> lines;

    std::vector<std::unique_ptr<FileItem>> fileItems;
    json jsonItems;

public:
    DataFileParser(QString);

    //const QStringList toList();
    std::vector<std::string> toStdStringVector();
    void printRawData();
    void run();
    void storeItemForParsing(int, std::string, ItemType);
    bool isFileItemStartLine(std::string);

    json getJsonItems();
};

#endif // DATAFILEPARSER_H
