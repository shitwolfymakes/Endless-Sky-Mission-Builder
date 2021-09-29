#include "fileitem.h"

FileItem::FileItem() {};

FileItem::FileItem(ItemType itemType) {
    this->itemType = itemType;
}

FileItem::ItemType FileItem::getType() {
    return itemType;
}

void FileItem::setType(FileItem::ItemType itemType) {
    this->itemType = itemType;
}

string FileItem::getName() {
    return name;
}

void FileItem::setName(string name) {
    this->name = name;
}

void FileItem::appendLines(string line) {
    this->lines.push_back(line);
}

vector<string> FileItem::getLines() {
    return lines;
}

void FileItem::setLines(vector<string> lines) {
    this->lines = lines;
}

string FileItem::toString() {
    // this is O(n), whereas std::accumulate is O(n^2) for strings
    std::string str;
    for (const auto &piece: lines) str += piece;
    return str;
}
