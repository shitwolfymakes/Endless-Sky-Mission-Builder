#include "datafileparser.h"

DataFileParser::DataFileParser(QString rawData)
    : qLines(rawData.split("\n"))
{
    this->rawData = rawData;
    printRawData();
}

std::vector<std::string> DataFileParser::toStdStringVector() {
    std::vector<std::string> lines;
    for(const QString &line: qLines) {
        lines.push_back(line.toStdString());
    }
    return lines;
}

/*
const QStringList DataFileParser::toList() {
    const QStringList lines = rawData.split("\n");
    return lines;
}
*/

void DataFileParser::printRawData() {
    qDebug() << "BEGIN RAW DATA";
    for(const QString &line: qLines){
        //need to use qUtf8Printable to preserve the formatting
        qDebug("%s", qUtf8Printable(line));
    }
    qDebug() << "END RAW DATA";
}

void DataFileParser::run() {
    std::vector<std::string> lines = toStdStringVector();
    qDebug() << "Parsing data file...";
    int i = 0;
    for(std::string &line: lines) {
        if (line == "") {
            qDebug() << "skipping blank line";
            i++;
            continue;
        }
        i++;
    }
}
