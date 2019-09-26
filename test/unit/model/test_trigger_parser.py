import unittest
import src.model as model


class TriggerParserTestCase(unittest.TestCase):
    """Tests for methods in `TriggerParser.py`"""

    def test_add_line(self):
        true_output = ["Harambe died for you\n"]
        test_model = self.get_empty_test_model()
        test_model._add_line("Harambe died for you")
        self.assertEqual(true_output, test_model.lines)
    #end test_add_line


    def test_add_quotes_quotes_added(self):
        true_output = "\"Michael Reeves is the Elon Musk of bad ideas\""
        test_output = model.TriggerParser._add_quotes("Michael Reeves is the Elon Musk of bad ideas")
        self.assertEqual(true_output, test_output)
    #end test_add_quotes_quotes_added


    ### triggerType
    def test_has_trigger_type_true(self):
        test_model = self.get_empty_test_model()
        trigger = test_model.components.triggerList[0]
        trigger.triggerType = "accept"
        self.assertTrue(test_model._has_trigger_type())
    #end test_has_trigger_type_true


    def test_has_trigger_type_false(self):
        test_model = self.get_empty_test_model()
        self.assertFalse(test_model._has_trigger_type())
    #end test_has_trigger_type_false


    def test_parse_trigger_type(self):
        true_output = '\ton accept\n'
        test_model = self.get_empty_test_model()
        trigger = test_model.components.triggerList[0]
        trigger.triggerType = "accept"
        test_model._parse_trigger_type()
        self.assertEqual(true_output, test_model.lines[0])
    #end test_parse_trigger_type


    ### dialog
    def test_has_dialog_true(self):
        test_model = self.get_empty_test_model()
        trigger = test_model.components.triggerList[0]
        trigger.dialog = "It is Wednesday my dudes"
        self.assertTrue(test_model._has_dialog())
    # end test_has_dialog_true

    def test_has_dialog_false(self):
        test_model = self.get_empty_test_model()
        self.assertFalse(test_model._has_dialog())
    # end test_has_dialog_false

    def test_parse_dialog(self):
        true_output = '\t\tdialog `It is Wednesday my dudes`\n'
        test_model = self.get_empty_test_model()
        trigger = test_model.components.triggerList[0]
        trigger.dialog = "It is Wednesday my dudes"
        test_model._parse_dialog()
        self.assertEqual(true_output, test_model.lines[0])
    # end test_parse_dialog


    def test_add_quotes_quotes_not_added(self):
        true_output = "Harambe"
        test_output = model.TriggerParser._add_quotes("Harambe")
        self.assertEqual(true_output, test_output)
    #end test_add_quotes_quotes_not_added


    @staticmethod
    def get_empty_test_model():
        mission = model.Mission("Testing")
        mission.add_trigger()
        test_model = model.TriggerParser(mission)
        test_model.trigger = test_model.components.triggerList[0]
        return test_model
    # end get_empty_test_model
#end class TriggerParserTestCase


if __name__ == "__main__":
    unittest.main()
