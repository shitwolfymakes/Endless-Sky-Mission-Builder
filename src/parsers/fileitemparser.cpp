#include "fileitemparser.h"

FileItemParser::FileItemParser(std::vector<std::string> lines)
    : lines(lines)
{

}

std::vector<std::string> FileItemParser::tokenize(std::string line) {
    // strip whitespace/tabs from line
    boost::trim(line);
    boost::trim_if(line, boost::is_any_of("\t"));

    std::vector<std::string> tokens;
    std::string token;

    // define the separators
    std::string separator1("");//dont let quoted arguments escape themselves
    std::string separator2(" ");//split on spaces
    std::string separator3("`\"");//let it have quoted arguments

    boost::escaped_list_separator<char> els(separator1,separator2,separator3);
    boost::tokenizer<boost::escaped_list_separator<char>> tok(line, els);
    for(boost::tokenizer<boost::escaped_list_separator<char>>::iterator beg=tok.begin(); beg!=tok.end();++beg)
    {
        token = *beg;
        boost::trim(token);
        tokens.push_back(token);
    }
    return tokens;
}

int FileItemParser::getIndentLevel(std::string line) {
    int level = 0;
    for (char c: line) {
        if (c == '\t') {
            level++;
        } else {
            break;
        }
    }
    return level;
}

bool FileItemParser::isOneOf(std::string token, std::vector<std::string> options) {
    for (std::string &option: options) {
        if (token.compare(option) == 0) {
            return true;
        }
    }
    return false;
}