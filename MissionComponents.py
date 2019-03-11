''' MissionComponents.py
    This file contains the classes defining some components of a mission
'''

class MissionComponents(object):

    def __init__(self):
        print("component %s initialized" % self.__class__)
    #end init

#end class MissionComponents

class Cargo(object):
    '''
    cargo  = [ [None, None, [None, None]], # cargo (random | <name>) <number> [<number> [<probability>]]
               [None, None, None],         #     illegal <fine> [<message>]
               None ]                      #     stealth
    '''

    def __init__(self):
        print("component %s initialized" % self.__class__)
    #end init

#end class Cargo


class Passengers(object):

    def __init__(self):
        print("component %s initialized" % self.__class__)
    # end init

# end class Passengers


class Clearance(object):

    def __init__(self):
        print("component %s initialized" % self.__class__)
    # end init

# end class Clearance


class Stopover(object):

    def __init__(self):
        print("component %s initialized" % self.__class__)
    # end init

# end class Conversations

class Conversations(object):
    #TODO: Implement this in full in Version 2

    def __init__(self):
        print("component %s initialized" % self.__class__)
    # end init

# end class Conversations