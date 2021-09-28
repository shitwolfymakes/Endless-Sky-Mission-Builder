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
    // convert lines to vector
    std::vector<std::string> lines = toStdStringVector();

    // define regex matches
    std::regex matchEvent       (eventPattern);
    std::regex matchGovernment  (governmentPattern);
    std::regex matchMission     (missionPattern);
    std::regex matchPhrase      (phrasePattern);
    std::regex matchShip        (shipPattern);

    qDebug() << "Parsing data file...";
    int i = 0;
    for(std::string &line: lines) {
        // account for whitespace between file items
        if (line == "") {
            qDebug() << "skipping blank line";
            i++;
            continue;
        }

        // search for lines starting file items
        if (std::regex_match(line, matchEvent)) {
            QString qLine = QString::fromStdString(line);
            qDebug("\tEVENT FOUND: %s", qUtf8Printable(qLine));
        } else if (std::regex_match(line, matchGovernment)) {
            QString qLine = QString::fromStdString(line);
            qDebug("\tGOVERNMENT FOUND: %s", qUtf8Printable(qLine));
        } else if (std::regex_match(line, matchMission)) {
            QString qLine = QString::fromStdString(line);
            qDebug("\tMISSION FOUND: %s", qUtf8Printable(qLine));
        } else if (std::regex_match(line, matchPhrase)) {
            QString qLine = QString::fromStdString(line);
            qDebug("\tPHRASE FOUND: %s", qUtf8Printable(qLine));
        } else if (std::regex_match(line, matchShip)) {
            QString qLine = QString::fromStdString(line);
            qDebug("\tSHIP FOUND: %s", qUtf8Printable(qLine));
        } else {
            continue;
        }

        i++;
    }
}
