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

QString FileItem::getName() {
    return name;
}

void FileItem::setName(QString name) {
    this->name = name;
}

void FileItem::appendLines(QString line) {
    this->lines.append(line);
}

QStringList FileItem::getLines() {
    return lines;
}

void FileItem::setLines(QStringList lines) {
    this->lines = lines;
}

QString FileItem::toString() {
    return lines.join("\n");
}
