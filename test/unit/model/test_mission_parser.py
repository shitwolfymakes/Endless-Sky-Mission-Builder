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
    #end test_parse_blocked


    @staticmethod
    def get_empty_test_model():
        return model.MissionParser(model.Mission("Testing"))
    #end get_empty_test_model

#end class MissionParserTestCase


if __name__ == "__main__":
    unittest.main()
