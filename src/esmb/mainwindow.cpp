// SPDX-License-Identifier: GPL-3.0-only
/*
 * mainwindow.cpp
 *
 * Copyright (c) 2021, Andrew Sneed <wolfy@shitwolfymakes.com>
 */

#include "mainwindow.h"
#include "./ui_mainwindow.h"

#include "esmbapplication.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    this->setCentralWidget(ui->centralwidget);

    connect(ui->comboBox, SIGNAL(currentIndexChanged(int)), this, SLOT(comboBoxChanged()));
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

    ESMBApplication& esmb = ESMBApplication::getInstance();
    esmb.parseFileData(text.toStdString());

    updateComboBoxData();

    QString jsonText = QString::fromStdString(esmb.getCurrentItem()->dump(4));
    ui->jsonDisplay->setText(jsonText);
    ui->textDisplay->setText(text);

    file.close();
}

void MainWindow::on_actionQuit_triggered()
{
    QApplication::quit();
}

void MainWindow::comboBoxChanged() {
    ESMBApplication& esmb = ESMBApplication::getInstance();
    int index = ui->comboBox->currentIndex();
    qDebug("%s: %d", "COMBOBOX INDEX SELECTED", index);

    std::string id = ui->comboBox->itemText(index).toStdString();
    esmb.setCurrentItem(esmb.getJsonItemById(id)); // TODO: add handling for when a nullptr is returned

    // store the json text as a QString and update the json display widget
    QString jsonText = QString::fromStdString(esmb.getCurrentItem()->dump(4));
    ui->jsonDisplay->setText(jsonText);
}

void MainWindow::updateComboBoxData() {
    ESMBApplication& esmb = ESMBApplication::getInstance();
    esmb.updateItemNames();

    // update the combobox with the new itemNames
    ui->comboBox->clear();
    ui->comboBox->insertItems(0, esmb.getNames());
}
