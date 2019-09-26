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
        return test_model
    # end get_empty_test_model
#end class TriggerParserTestCase


if __name__ == "__main__":
    unittest.main()
