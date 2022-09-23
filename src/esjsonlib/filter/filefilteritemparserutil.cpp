#include "filefilteritemparserutil.h"

#include "filefilteritemparser.h"

FileFilterItemParser* FileFilterItemParserUtil::create(std::vector<std::string> lines) {
    FileFilterItemParser *parser = new FileFilterItemParser(lines);
    return parser;
}
