#include "mainwindow.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv); //TODO: create a custom application object to hold the application state
    MainWindow w;
    w.show();
    return a.exec();
}
