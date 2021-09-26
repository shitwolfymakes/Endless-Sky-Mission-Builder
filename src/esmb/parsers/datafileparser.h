#ifndef DATAFILEPARSER_H
#define DATAFILEPARSER_H

#include <string>
#include <vector>

#include <QDebug>
#include <QString>
#include <QStringList>

class DataFileParser
{
public:
    QString rawData;
    const QStringList qLines;

    DataFileParser(QString);

    //const QStringList toList();
    std::vector<std::string> toStdStringVector();
    void printRawData();
    void run();
};

#endif // DATAFILEPARSER_H
