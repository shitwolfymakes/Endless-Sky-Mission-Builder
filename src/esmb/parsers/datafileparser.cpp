#include "datafileparser.h"

DataFileParser::DataFileParser(QString rawData)
{
    this->rawData = rawData;
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
        //need to use qUtf8Printable to preserve the formatting
        qDebug("%s", qUtf8Printable(line));
    }
    qDebug() << "END RAW DATA";
}
