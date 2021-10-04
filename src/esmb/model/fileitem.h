// SPDX-License-Identifier: GPL-3.0-only
/*
 * fileitem.h
 *
 * Copyright (c) 2021, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#ifndef FILEITEM_H
#define FILEITEM_H

#include <string>
#include <vector>

#include <boost/algorithm/string.hpp>
#include <boost/tokenizer.hpp>
#include <QDebug>
#include <QString>

using namespace std;

class FileItem
{
public:
    string name;
    vector<string> lines;

    FileItem();

    string getName();
    void setName(string);

    void appendLine(string);
    vector<string> getLines();
    void setLines(vector<string>);

    string toString();
    void printLines();

    virtual void parse() = 0;
    vector<string> tokenize(string);
    bool isOneOf(string, vector<string>);
};

#endif // FILEITEM_H
