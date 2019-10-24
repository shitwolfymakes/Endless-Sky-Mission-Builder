import unittest
import src.model as model


class ParseMissionTestCase(unittest.TestCase):
    """Tests for `Mission.parse`"""

    def test_parse_mission(self):
        true_output = self.add_all_data_lines()

        self.model.parse()
        self.assertEqual(true_output, self.model.lines)
    #end test_parse_mission

    @staticmethod
    def add_all_data_lines():
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


    def setUp(self):
        self.model = model.Mission("Test Mission 0")
        self.model.components.mission_display_name = "test"
        self.model.components.description = "A test mission"
        self.model.components.blocked = "Oh piss off!"
        self.model.components.deadline.set([2, 1])
        self.model.components.cargo.set(["food", 5, 2, 0.1])
        self.model.components.passengers.set([5, 5, 0.2])
        self.model.components.illegal.set([50, "Soviet citizens need no food comrade"])
        self.model.components.is_stealth = True
        self.model.components.is_invisible = True
        self.model.components.priority_level = "priority"
        self.model.components.where_shown = "job"
        self.model.components.repeat.set(5)
        self.model.components.clearance.set("You're on the list")
        self.model.components.is_infiltrating = True
        self.model.components.waypoint = "Sol"
        self.model.components.stopover.set("Delve")
        self.model.components.source.set("Sol")
        self.model.components.destination.set("Delve")

        self.model.add_trigger()
        trigger = self.model.components.trigger_list[0]
        trigger.is_active = True
        trigger.trigger_type = "accept"
        trigger.outfit = ["test outfit", 1]
        trigger.require = ["Jump Drive", 1]

        self.model.add_trigger()
        trigger = self.model.components.trigger_list[1]
        trigger.is_active = True
        trigger.trigger_type = "offer"
        trigger.dialog = "It is Wednesday my dudes"
        trigger.outfit = ["Skylance V", 5]
        trigger.require = ["Hyperdrive", 1]
        trigger.is_payment = True
        trigger.payment = [1500, 0.2]
        trigger.event = ["blaze it", 420, 4200]
        trigger.is_fail = True
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
    #end setUp
#end class ParseMissionTestCase


if __name__ == "__main__":
    unittest.main()
