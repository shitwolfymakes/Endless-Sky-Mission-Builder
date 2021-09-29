#ifndef FILEITEM_H
#define FILEITEM_H

#include <QString>
#include <QStringList>

class FileItem
{
public:
    enum ItemType { Event, Government, Mission, Phrase, Ship };

private:
    ItemType itemType;
    QString name;
    QStringList lines;

public:

    FileItem();
    FileItem(ItemType);

    ItemType getType();
    void setType(ItemType);

    QString getName();
    void setName(QString);

    void appendLines(QString);
    QStringList getLines();
    void setLines(QStringList);

    QString toString();

    virtual void parse() {};
};

#endif // FILEITEM_H
