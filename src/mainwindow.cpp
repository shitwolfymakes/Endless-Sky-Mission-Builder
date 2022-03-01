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

    connect(ui->comboBox, SIGNAL(currentIndexChanged(int)), this, SLOT(comboBoxUpdated()));
    //connect(ui->comboBox, QOverload<int>::of(&QComboBox::currentIndexChanged),
    //    [=](int index){ on_comboBox_update(index); });
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
    if (!file.open(QIODevice::ReadOnly | QFile::Text)) {
        QMessageBox::warning(this, "Warning", "Cannot open file: " + file.errorString());
    }
    QTextStream in(&file);
    QString text = in.readAll();
    DataFileParser parser = DataFileParser(text);
    parser.run();

    // store the parsed data in the singleton
    ESMBApplication& esmb = ESMBApplication::getInstance();
    esmb.setJsonItems(parser.getJsonItems());

    // update combobox
    updateComboBoxData();

    // TODO: set the text to display the data for a selected mission
    ui->textDisplay->setText(text);
    QString jsonText = QString::fromStdString(esmb.getJsonItems().dump(4));
    ui->jsonDisplay->setText(jsonText);
    file.close();
}

void MainWindow::on_actionQuit_triggered()
{
    QApplication::quit();
}

void MainWindow::comboBoxUpdated() {
    int index = ui->comboBox->currentIndex();
    qDebug("%s: %d", "COMBOBOX UPDATED", index);
}

void MainWindow::updateComboBoxData() {
    // update the map of ids and their associated items
    ESMBApplication& esmb = ESMBApplication::getInstance();
    esmb.updateIdMap();

    // update the combobox with the new itemNames
    ui->comboBox->clear();
    ui->comboBox->insertItems(0, esmb.getNames());
}
