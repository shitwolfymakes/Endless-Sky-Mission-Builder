#ifndef FILEITEMPARSER_H
#define FILEITEMPARSER_H

#include <string>
#include <vector>

#include <QString>
#include <boost/algorithm/string.hpp>
#include <boost/tokenizer.hpp>

class FileItemParser
{
protected:
    const std::vector<std::string> lines;

    FileItemParser(std::vector<std::string>);

    virtual void run() = 0;
    std::vector<std::string> tokenize(std::string);
    bool isOneOf(std::string, std::vector<std::string>);
};

#endif // FILEITEMPARSER_H
