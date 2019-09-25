import unittest
import src.model as model


class MissionParserTestCase(unittest.TestCase):
    """Tests for methods in `MissionParser.py`"""

    def test_add_line(self):
        true_output = ["Harambe died for you\n"]

        test_model = self.get_empty_test_model()
        test_model._add_line("Harambe died for you")

        self.assertEqual(true_output, test_model.lines)
    #end test_add_line


    ### mission display name
    def test_has_mission_display_name_true(self):
        test_model = self.get_empty_test_model()
        test_model.components.missionDisplayName = 'Welcome To The Jungle'
        self.assertTrue(test_model._has_mission_display_name())
    #end test_has_mission_display_name_true


    def test_has_mission_display_name_false(self):
        test_model = self.get_empty_test_model()
        self.assertFalse(test_model._has_mission_display_name())
    #end test_has_mission_display_name_false


    def test_parse_mission_display_name(self):
        true_output = '\tname `Welcome To The Jungle`\n'
        test_model = self.get_empty_test_model()
        test_model.components.missionDisplayName = 'Welcome To The Jungle'
        test_model._parse_mission_display_name()
        self.assertEqual(true_output, test_model.lines[0])
    #end test_parse_mission_display_name


    ### description
    def test_has_description_true(self):
        test_model = self.get_empty_test_model()
        test_model.components.description = 'A test mission'
        self.assertTrue(test_model._has_description())
    # end test_has_description_true


    def test_has_description_false(self):
        test_model = self.get_empty_test_model()
        self.assertFalse(test_model._has_description())
    # end test_has_description_false


    def test_parse_description(self):
        true_output = '\tdescription `A test mission`\n'
        test_model = self.get_empty_test_model()
        test_model.components.description = 'A test mission'
        test_model._parse_description()
        self.assertEqual(true_output, test_model.lines[0])
    #end test_parse_description


    ### blocked
    def test_has_blocked_true(self):
        test_model = self.get_empty_test_model()
        test_model.components.blocked = "Oh piss off!"
        self.assertTrue(test_model._has_blocked())
    # end test_has_blocked_true


    def test_has_blocked_false(self):
        test_model = self.get_empty_test_model()
        self.assertFalse(test_model._has_blocked())
    # end test_has_blocked_false


    def test_parse_blocked(self):
        true_output = '\tblocked "Oh piss off!"\n'
        test_model = self.get_empty_test_model()
        test_model.components.blocked = "Oh piss off!"
        test_model._parse_blocked()
        self.assertEqual(true_output, test_model.lines[0])
    #end test_parse_blocked


    ### deadline
    def test_has_deadline_true(self):
        test_model = self.get_empty_test_model()
        test_model.components.deadline.set([2, 1])
        self.assertTrue(test_model._has_deadline())
    # end test_has_deadline_true


    def test_has_deadline_false(self):
        test_model = self.get_empty_test_model()
        self.assertFalse(test_model._has_deadline())
    # end test_has_deadline_false


    def test_parse_deadline(self):
        true_output = '\tdeadline 2 1\n'
        test_model = self.get_empty_test_model()
        test_model.components.deadline.set([2, 1])
        test_model._parse_deadline()
        self.assertEqual(true_output, test_model.lines[0])
    #end test_parse_deadline


    ### cargo
    def test_has_cargo_true(self):
        test_model = self.get_empty_test_model()
        test_model.components.cargo.set(["food", 5, 2, 0.1])
        self.assertTrue(test_model._has_cargo())
    # end test_has_cargo_true


    def test_has_cargo_false(self):
        test_model = self.get_empty_test_model()
        self.assertFalse(test_model._parse_cargo())
    # end test_has_cargo_false


    def test_parse_cargo(self):
        true_output = '\tcargo "food" 5 2 0.1\n'
        test_model = self.get_empty_test_model()
        test_model.components.cargo.set(["food", 5, 2, 0.1])
        test_model._parse_cargo()
        self.assertEqual(true_output, test_model.lines[0])
    #end test_parse_cargo


    ### passengers
    def test_has_passengers_true(self):
        test_model = self.get_empty_test_model()
        test_model.components.passengers.set([5, 5, 0.2])
        self.assertTrue(test_model._has_passengers())
    # end test_has_passengers_true


    def test_has_passengers_false(self):
        test_model = self.get_empty_test_model()
        self.assertFalse(test_model._has_passengers())
    # end test_has_passengers_false


    def test_parse_passengers(self):
        true_output = '\tpassengers 5 5 0.2\n'
        test_model = self.get_empty_test_model()
        test_model.components.passengers.set([5, 5, 0.2])
        test_model._parse_passengers()
        self.assertEqual(true_output, test_model.lines[0])
    #end test_parse_passengers


    ### illegal
    def test_has_illegal_true(self):
        test_model = self.get_empty_test_model()
        test_model.components.illegal.set([50, "Soviet citizens need no food comrade"])
        self.assertTrue(test_model._has_illegal())
    # end test_has_illegal_true


    def test_has_illegal_false(self):
        test_model = self.get_empty_test_model()
        self.assertFalse(test_model._has_illegal())
    # end test_has_illegal_false


    def test_parse_illegal(self):
        true_output = '\tillegal 50 `Soviet citizens need no food comrade`\n'
        test_model = self.get_empty_test_model()
        test_model.components.illegal.set([50, "Soviet citizens need no food comrade"])
        test_model._parse_illegal()
        self.assertEqual(true_output, test_model.lines[0])
    #end test_parse_illegal


    ### stealth
    def test_has_stealth_true(self):
        test_model = self.get_empty_test_model()
        test_model.components.isStealth = True
        self.assertTrue(test_model._has_stealth())
    # end test_has_stealth_true


    def test_has_stealth_false(self):
        test_model = self.get_empty_test_model()
        self.assertFalse(test_model._has_stealth())
    # end test_has_stealth_false


    def test_parse_stealth(self):
        true_output = '\tstealth\n'
        test_model = self.get_empty_test_model()
        test_model.components.isStealth = True
        test_model._parse_stealth()
        self.assertEqual(true_output, test_model.lines[0])
    #end test_parse_stealth


    ### invisible
    def test_has_invisible_true(self):
        test_model = self.get_empty_test_model()
        test_model.components.isInvisible = True
        self.assertTrue(test_model._has_invisible())
    # end test_has_invisible_true


    def test_has_invisible_false(self):
        test_model = self.get_empty_test_model()
        self.assertFalse(test_model._has_invisible())
    # end test_has_invisible_false


    def test_parse_invisible(self):
        true_output = '\tinvisible\n'
        test_model = self.get_empty_test_model()
        test_model.components.isInvisible = True
        test_model._parse_invisible()
        self.assertEqual(true_output, test_model.lines[0])
    #end test_parse_invisible


    ### priority level
    def test_has_priority_level_true(self):
        test_model = self.get_empty_test_model()
        test_model.components.priorityLevel = 'priority'
        self.assertTrue(test_model._has_priority_level())
    # end test_has_priority_level_true


    def test_has_priority_level_false(self):
        test_model = self.get_empty_test_model()
        self.assertFalse(test_model._has_priority_level())
    # end test_has_priority_level_false


    def test_parse_priority_level(self):
        true_output = '\tpriority\n'
        test_model = self.get_empty_test_model()
        test_model.components.priorityLevel = 'priority'
        test_model._parse_priority_level()
        self.assertEqual(true_output, test_model.lines[0])
    #end test_parse_priority_level


    ### where shown
    def test_has_where_shown_true(self):
        test_model = self.get_empty_test_model()
        test_model.components.whereShown = 'job'
        self.assertTrue(test_model._has_where_shown())
    # end test_has_where_shown_true

    def test_has_where_shown_false(self):
        test_model = self.get_empty_test_model()
        self.assertFalse(test_model._has_where_shown())
    # end test_has_where_shown_false

    def test_parse_where_shown(self):
        true_output = '\tjob\n'
        test_model = self.get_empty_test_model()
        test_model.components.whereShown = 'job'
        test_model._parse_where_shown()
        self.assertEqual(true_output, test_model.lines[0])
    # end test_parse_where_shown


    ### repeat
    def test_has_repeat_true(self):
        test_model = self.get_empty_test_model()
        test_model.components.repeat.set(5)
        self.assertTrue(test_model._has_repeat())
    # end test_has_repeat_true


    def test_has_repeat_false(self):
        test_model = self.get_empty_test_model()
        self.assertFalse(test_model._has_repeat())
    # end test_has_repeat_true


    def test_parse_repeat(self):
        true_output = '\trepeat 5\n'
        test_model = self.get_empty_test_model()
        test_model.components.repeat.set(5)
        test_model._parse_repeat()
        self.assertEqual(true_output, test_model.lines[0])
    # end test_parse_repeat


    ### clearance
    def test_has_clearance_true(self):
        test_model = self.get_empty_test_model()
        test_model.components.clearance.set("You're on the list")
        self.assertTrue(test_model._has_clearance())
    # end test_has_clearance_true


    def test_has_clearance_false(self):
        test_model = self.get_empty_test_model()
        self.assertFalse(test_model._has_clearance())
    # end test_has_clearance_false


    def test_parse_clearance(self):
        true_output = "\tclearance `You're on the list`\n"
        test_model = self.get_empty_test_model()
        test_model.components.clearance.set("You're on the list")
        test_model._parse_clearance()
        self.assertEqual(true_output, test_model.lines[0])
    # end test_parse_clearance


    ### infiltrating
    def test_has_infiltrating_true(self):
        test_model = self.get_empty_test_model()
        test_model.components.isInfiltrating = True
        self.assertTrue(test_model._has_infiltrating())
    # end test_has_infiltrating_true

    def test_has_infiltrating_false(self):
        test_model = self.get_empty_test_model()
        self.assertFalse(test_model._has_infiltrating())
    # end test_has_invisible_false

    def test_parse_infiltrating(self):
        true_output = '\tinfiltrating\n'
        test_model = self.get_empty_test_model()
        test_model.components.isInfiltrating = True
        test_model._parse_infiltrating()
        self.assertEqual(true_output, test_model.lines[0])
    # end test_parse_infiltrating


    @staticmethod
    def get_empty_test_model():
        return model.MissionParser(model.Mission("Testing"))
    #end get_empty_test_model

#end class MissionParserTestCase


if __name__ == "__main__":
    unittest.main()
