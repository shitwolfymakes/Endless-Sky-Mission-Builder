import unittest
from src.model.Mission import Mission


class ParseMissionTestCase(unittest.TestCase):
    """Tests for `Mission.parse_mission`"""

    def test_parse_mission(self):
        true_output = self.add_all_data_lines()
        model = Mission("Test Mission 0")
        # set data in the model
        model.components.missionDisplayName = "test"
        model.components.description = "A test mission"
        model.components.blocked = "Oh piss off!"
        model.components.deadline.set([2, 1])
        model.components.cargo.set(["food", 5, 2, 0.1])
        model.components.passengers.set([5, 5, 0.2])
        model.components.illegal.set([50, "Soviet citizens need no food comrade"])
        model.components.isStealth = True
        model.components.isInvisible = True
        model.components.priorityLevel = "priority"
        model.components.whereShown = "job"
        model.components.isRepeat = True
        model.components.repeat = 5
        model.components.clearance.set("You're on the list")
        model.components.isInfiltrating = True
        model.components.waypoint = "Sol"
        model.components.stopover.set("Delve")
        model.components.source.set("Sol")
        model.components.destination.set("Delve")

        model.add_trigger()
        trigger = model.components.triggerList[0]
        trigger.isActive = True
        trigger.triggerType = "accept"
        trigger.outfit = ["test outfit", 1]
        trigger.require = ["Jump Drive", 1]

        model.add_trigger()
        trigger = model.components.triggerList[1]
        trigger.isActive = True
        trigger.triggerType = "offer"
        trigger.dialog = "It is Wednesday my dudes"
        trigger.outfit = ["Skylance V", 5]
        trigger.require = ["Hyperdrive", 1]
        trigger.isPayment = True
        trigger.payment = [1500, 0.2]
        trigger.event = ["blaze it", 420, 4200]
        trigger.isFail = True
        trigger.fail = "the mission"

        trigger.add_tc()
        trigger.conditions[0].set(0, ["yo mama", "+=", 20])
        trigger.add_tc()
        trigger.conditions[1].set(1, ["no u", "++"])
        trigger.add_tc()
        trigger.conditions[2].set(2, ["clear", "the drugs"])

        trigger.add_log()
        trigger.logs[0].set(1, ["my mama ain't a ho"])
        trigger.add_log()
        trigger.logs[1].set(3, ["People", "Yo mama", "is a ho"])

        # run the method
        model.parse_mission()

        #test that it worked as expected
        self.assertEqual(true_output, model.missionLines)

    #end test_parse_mission


    def add_all_data_lines(self):
        return ['mission "Test Mission 0"\n',
                '\tname `test`\n',
                '\tdescription `A test mission`\n',
                '\tblocked "Oh piss off!"\n',
                '\tdeadline 2 1\n',
                '\tcargo "food" 5 2 0.1\n',
                '\tpassengers 5 5 0.2\n',
                '\tillegal 50 `Soviet citizens need no food comrade`\n',
                '\tstealth\n',
                '\tinvisible\n',
                '\tpriority\n',
                '\tjob\n',
                '\trepeat 5\n',
                "\tclearance `You're on the list`\n",
                '\tinfiltrating\n',
                '\twaypoint "Sol"\n',
                '\tstopover "Delve"\n',
                '\tsource "Sol"\n',
                '\tdestination "Delve"\n',
                '\ton accept\n',
                '\t\toutfit "test outfit" 1\n',
                '\t\trequire "Jump Drive" 1\n',
                '\ton offer\n',
                '\t\tdialog `It is Wednesday my dudes`\n',
                '\t\toutfit "Skylance V" 5\n',
                '\t\trequire Hyperdrive 1\n',
                '\t\tpayment 1500 0.2\n',
                '\t\t"yo mama" += 20\n',
                '\t\t"no u" ++\n',
                '\t\tclear "the drugs"\n',
                '\t\tevent "blaze it" 420 4200\n',
                '\t\tfail "the mission"\n',
                "\t\tlog `my mama ain't a ho`\n",
                '\t\tlog "People" "Yo mama" `is a ho`\n']
    #end add_all_data_lines


#end class ParseMissionTestCase

if __name__ == "__main__":
    unittest.main()
