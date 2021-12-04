// SPDX-License-Identifier: GPL-3.0-only
/*
 * main.cpp
 *
 * Copyright (c) 2021, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "mainwindow.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv); //TODO: create a custom application object to hold the application state
    MainWindow w;
    w.show();
    return a.exec();
}
