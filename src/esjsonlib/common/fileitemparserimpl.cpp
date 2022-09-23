#include "fileitemparserimpl.h"

FileItemParserImpl::FileItemParserImpl() {}

void FileItemParserImpl::setLines(std::vector<std::string> lines) {
    this->lines = lines;
}

std::vector<std::string> FileItemParserImpl::getLines() const {
    return lines;
}
