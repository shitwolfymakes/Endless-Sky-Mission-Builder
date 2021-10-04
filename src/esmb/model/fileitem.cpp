// SPDX-License-Identifier: GPL-3.0-only
/*
 * fileitem.cpp
 *
 * Copyright (c) 2021, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "fileitem.h"

FileItem::FileItem() {};

string FileItem::getName() {
    return name;
}

void FileItem::setName(string name) {
    this->name = name;
}

void FileItem::appendLine(string line) {
    this->lines.push_back(line);
}

vector<string> FileItem::getLines() {
    return lines;
}

void FileItem::setLines(vector<string> lines) {
    this->lines = lines;
}

string FileItem::toString() {
    // this is O(n), whereas std::accumulate is O(n^2) for strings
    string str;
    for (const auto &piece: lines) str += piece;
    return str;
}

void FileItem::printLines() {
    qDebug() << "Item Data:";
    for (const string &line: lines) {
        QString qLine = QString::fromStdString(line);
        qDebug("\t%s", qUtf8Printable(qLine));
    }
}

vector<string> FileItem::tokenize(string line) {
    // strip whitespace/tabs from line
    boost::trim(line);
    boost::trim_if(line, boost::is_any_of("\t"));

    vector<string> tokens;

    // define the separators
    string separator1("");//dont let quoted arguments escape themselves
    string separator2(" ");//split on spaces
    string separator3("`\"");//let it have quoted arguments

    boost::escaped_list_separator<char> els(separator1,separator2,separator3);
    boost::tokenizer<boost::escaped_list_separator<char>> tok(line, els);
    for(boost::tokenizer<boost::escaped_list_separator<char>>::iterator beg=tok.begin(); beg!=tok.end();++beg)
    {
        tokens.push_back(*beg);
    }
    return tokens;
}

bool FileItem::isOneOf(string token, vector<string> options) {
    for (string &option: options) {
        if (token.compare(option) == 0) {
            return true;
        }
    }
    return false;
}
