''' MissionFileParser.py
# Copyright (c) 2019 by Andrew Sneed
#
# Endless Sky Mission Builder is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# Endless Sky Mission Builder is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.

This takes the data read in from a mission file and stores it in each mission object

'''
#TODO: Add data validation, there is currently no checks to make sure it's not all junk data
import re, shlex

class MissionFileParser(object):
    def __init__(self, esmb):
        self.esmb     = esmb
        self.missions = esmb.missionList

        self.graveKeyPattern = re.compile(r'^ *(.*) (`.*`).*')
    #end init

    def run(self):
        print("\nParsing Mission file...")

        for mission in self.missions:
            print("\tParsing mission: \"%s\"" % mission.missionName)
            lines = enumerate(mission.missionLines)
            for i, line in lines:
                line = line.rstrip()
                #print(i, line)
                tokens = self.tokenize(line)
                #print(tokens)

                # determine which attribute we've got
                if "name" in tokens[0]:
                    print("\t\tFound mission display name: \"%s\"" % tokens[1])
                    mission.components.missionDisplayName = tokens[1]
                elif "description" in tokens[0]:
                    print("\t\tFound description: %s" % tokens[1])
                    mission.components.description = tokens[1]
                elif "blocked" in tokens[0]:
                    print("\t\tFound blocked: %s" % tokens[1])
                    mission.components.blocked = tokens[1]
                elif "deadline" in tokens[0]:
                    print("\t\tFound deadline")
                    mission.components.deadline.isDeadline = True
                    self.storeComponentData(mission.components.deadline.deadline, tokens[1:])
                elif "cargo" in tokens[0]:
                    print("\t\tFound cargo: %s" % tokens[1:])
                    mission.components.cargo.isCargo = True
                    #TODO: TURN THIS FOR LOOP INTO A SINGLETON
                    self.storeComponentData(mission.components.cargo.cargoType, tokens[1:])

                    # check if next line contains cargo illegal data
                    if self.getIndentLevel(mission.missionLines[i+1]) > self.getIndentLevel(line):
                        i, line = next(lines)
                        line = line.rstrip()
                        tokens = self.tokenize(line)
                        print("\t\t\tFound cargo illegal modifier: %s" % tokens[1:])
                        self.storeComponentData(mission.components.cargo.cargoIllegal, tokens[1:])

                        # check if next line contains stealth data
                        if self.getIndentLevel(mission.missionLines[i+1]) == self.getIndentLevel(line):
                            i, line = next(lines)
                            print("\t\t\tFound cargo stealth modifier")
                            mission.components.cargo.isCargoStealth = True
                        #end if
                    #end if
                elif "passengers" in tokens[0]:
                    print("\t\tFound passengers: %s" % tokens[1:])
                    mission.components.passengers.isPassengers = True
                    self.storeComponentData(mission.components.passengers.passengers, tokens[1:])
                elif "invisible" in tokens[0]:
                    print("\t\tFound invisible modifier")
                    mission.components.isInvisible = True
                elif tokens[0] in ["priority", "minor"]:
                    print("\t\tFound priority level")
                    mission.components.priorityLevel = tokens[0]
                elif tokens[0] in ["job", "landing", "assisting", "boarding"]:
                    print("\t\tFound where shown")
                    mission.components.whereShown = tokens[0]
                elif "repeat" in tokens[0]:
                    print("\t\tFound repeat")
                    mission.components.isRepeat = True
                    if len(tokens) > 1:
                        print("\t\t\tFound repeat optional data: %s" % tokens[1])
                        mission.components.repeat = tokens[1]
                elif "clearance" in tokens[0]:
                    print("\t\tFound clearance: %s" % tokens[1])
                    mission.components.clearance.isClearance = True
                    mission.components.clearance.clearance   = tokens[1]
                elif "infiltrating" in tokens[0]:
                    print("\t\tFound infiltrating")
                    mission.components.isInfiltrating = True
                elif "waypoint" in tokens[0]:
                    print("\t\tFound waypoint: %s" % tokens[1])
                    mission.components.waypoint = tokens[1]
                elif "stopover" in tokens[0]:
                    print("\t\tFound stopover: %s" % tokens[1])
                    mission.components.stopover.isStopover = True
                    mission.components.stopover.stopover   = tokens[1]
                elif "source" in tokens[0]:
                    print("\t\tFound source: %s" % tokens[1])
                    mission.components.source.isSource = True
                    mission.components.source.source   = tokens[1]
                elif "destination" in tokens[0]:
                    print("\t\tFound destination: %s" % tokens[1])
                    mission.components.destination.isDestination = True
                    mission.components.destination.destination   = tokens[1]
                #end if/else
            #end for
            print("\tDone.")
        #end for
        print("File parsing complete.")
    #end run


    def tokenize(self, line):
        tokens = shlex.split(line)
        if '`' in line:
            #TODO: Fully implement this later, it's a ghetto-rigged POS
            #print(line)
            tokens = re.split(self.graveKeyPattern, line)
            tokens = tokens[1:3]
        #print(tokens)
        return tokens
    #end tokenize


    def getIndentLevel(self, line):
        tabCount = len(line) - len(line.lstrip(' '))
        #print(tabCount)
        return tabCount
    #end getIndentLevel


    def storeComponentData(self, component, tokens):
        for i, token in enumerate(tokens):
            if token is not None:
                component[i] = token
            else:
                break
            # end if/else
        # end for
        #print(component)
    #end storeComponentData
#end class MissionFileParser