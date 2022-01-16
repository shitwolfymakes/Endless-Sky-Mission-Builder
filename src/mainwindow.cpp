// SPDX-License-Identifier: GPL-3.0-only
/*
 * mainwindow.cpp
 *
 * Copyright (c) 2021, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "mainwindow.h"
#include "./ui_mainwindow.h"

#include "esmbapplication.h"
#include "parsers/datafileparser.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    this->setCentralWidget(ui->centralwidget);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_actionOpen_triggered()
{
    QString filename = QFileDialog::getOpenFileName(this, "Open the file");
    if (filename.isNull()) {
        return;
    }
    QFile file(filename);
    currentFile = filename;
    if (!file.open(QIODevice::ReadOnly | QFile::Text)){
        QMessageBox::warning(this, "Warning", "Cannot open file: " + file.errorString());
    }
    QTextStream in(&file);
    QString text = in.readAll();
    DataFileParser parser = DataFileParser(text);
    parser.run();

    // store the parsed data in the singleton
    ESMBApplication& esmb = ESMBApplication::getInstance();
    esmb.setJsonItems(parser.getJsonItems());

    // TODO: set the spinbox to display the data for a selected mission
    ui->textDisplay->setText(text);
    QString jsonText = QString::fromStdString(esmb.getJsonItems().dump(4));
    ui->jsonDisplay->setText(jsonText);
    file.close();
}


void MainWindow::on_actionQuit_triggered()
{
    QApplication::quit();
}
