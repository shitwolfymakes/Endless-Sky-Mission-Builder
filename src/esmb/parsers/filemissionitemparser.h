#ifndef FILEMISSIONITEMPARSER_H
#define FILEMISSIONITEMPARSER_H

#include "parsers/fileitemparser.h"

class FileMissionItemParser : public FileItemParser
{
private:
    json mission;

public:
    FileMissionItemParser(std::vector<std::string>);

    void run();

    void parseId(std::vector<std::string>);
};

#endif // FILEMISSIONITEMPARSER_H
