#ifndef FILEMISSIONITEMPARSER_H
#define FILEMISSIONITEMPARSER_H

#include "parsers/fileitemparser.h"
#include "nlohmann/json.hpp"

class FileMissionItemParser : public FileItemParser
{

public:
    FileMissionItemParser(std::vector<std::string>);

    void run();


};

#endif // FILEMISSIONITEMPARSER_H
