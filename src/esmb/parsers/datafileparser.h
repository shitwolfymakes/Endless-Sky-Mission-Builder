#ifndef DATAFILEPARSER_H
#define DATAFILEPARSER_H

#include <regex>
#include <string>
#include <vector>

#include <QDebug>
#include <QString>
#include <QStringList>

class DataFileParser
{
public:
    // define regex patterns for File Items
    std::string eventPattern        = "^event.*$";
    std::string governmentPattern   = "^government.*$";
    std::string missionPattern      = "^mission.*$";
    std::string phrasePattern       = "^phrase.*$";
    std::string shipPattern         = "^ship.*$";

    QString rawData;
    const QStringList qLines;

    DataFileParser(QString);

    //const QStringList toList();
    std::vector<std::string> toStdStringVector();
    void printRawData();
    void run();
};

#endif // DATAFILEPARSER_H
