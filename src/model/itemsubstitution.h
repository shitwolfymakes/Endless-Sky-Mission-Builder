#ifndef ITEMSUBSTITUTION_H
#define ITEMSUBSTITUTION_H

#include "fileitem.h"
#include "parsers/filesubstitutionitemparser.h"

class ItemSubstitution : public FileItem
{
public:
    ItemSubstitution();

    json parse();
};

#endif // ITEMSUBSTITUTION_H
