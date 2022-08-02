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
public:
    std::string name;
    std::vector<std::string> lines;

    FileItem();

    std::string getName();
    void setName(std::string);

    void appendLine(std::string);
    std::vector<std::string> getLines();
    void setLines(std::vector<std::string>);

    std::string toString();
    void printLines();

    virtual json parse() = 0;
};

#endif // FILEITEM_H
