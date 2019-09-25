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


    @staticmethod
    def get_empty_test_model():
        return model.MissionParser(model.Mission("Testing"))
    #end get_empty_test_model

#end class MissionParserTestCase
