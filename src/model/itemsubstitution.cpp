#include "itemsubstitution.h"

ItemSubstitution::ItemSubstitution()
{

}

json ItemSubstitution::parse() {
    // TODO: Implement this
    qDebug() << "parsing mission item to JSON";
    FileSubstitutionItemParser parser = FileSubstitutionItemParser(lines);
    json mission = parser.run();
    qDebug() << "finished parsing mission";
    return mission;
}
