#include "datafileparser.h"

DataFileParser::DataFileParser(QString text)
{
    rawData = text;
    printRawData();
}


QStringList DataFileParser::toList() {
    QStringList lines = rawData.split("\n");
    return lines;
}

void DataFileParser::printRawData() {
    const QStringList lines = toList();
    qDebug() << "BEGIN RAW DATA";
    for(const QString &line: lines){
        qDebug() << line;
    }
    qDebug() << "END RAW DATA";
}
