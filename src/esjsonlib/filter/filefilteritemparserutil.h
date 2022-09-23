#ifndef FILEFILTERITEMPARSERUTIL_H
#define FILEFILTERITEMPARSERUTIL_H

#include <string>
#include <vector>

class FileFilterItemParser;

struct FileFilterItemParserUtil {
    FileFilterItemParser* create(std::vector<std::string> lines);
};

#endif // FILEFILTERITEMPARSERUTIL_H
