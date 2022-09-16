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

#include <iostream>

#include "nlohmann/json.hpp"

using json = nlohmann::json;

class FileItem
{
protected:
    std::string name;
    std::vector<std::string> lines;

public:
    // CREATORS
    FileItem();

    // MANIPULATORS
    void setName(std::string);
    void setLines(std::vector<std::string>);
    void appendLine(std::string);
    virtual json parse() = 0;

    //ACCESSORS
    std::string getName() const;
    std::vector<std::string> getLines() const;
    std::string toString() const;
    void printLines() const;
};

#endif // FILEITEM_H
