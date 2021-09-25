#ifndef DATAFILEPARSER_H
#define DATAFILEPARSER_H

#include <QDebug>
#include <QString>
#include <QStringList>

class DataFileParser
{
public:
    QString rawData;

    DataFileParser(QString);

    QStringList toList();
    void printRawData();
};

#endif // DATAFILEPARSER_H
