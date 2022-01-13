#ifndef FILESUBSTITUTIONITEMPARSER_H
#define FILESUBSTITUTIONITEMPARSER_H

#include "fileitemparser.h"

class FileSubstitutionItemParser : public FileItemParser
{
private:
    json substitution;

public:
    FileSubstitutionItemParser(std::vector<std::string>);

    json run();
};

#endif // FILESUBSTITUTIONITEMPARSER_H
