import unittest
from src.model.Mission import Mission


class MissionTestCase(unittest.TestCase):
    """Tests for `Mission.py`."""

    ### Testing add_quotes()
    def test_add_quotes(self):
        """Check to see if it adds quotes to a multiword String"""
        test_line = "testing testing"
        passing_line = "\"testing testing\""
        self.assertEqual(passing_line, Mission.add_quotes(test_line))
    #end test_add_quotes

    def test_add_quotes_single_word(self):
        """Check to make sure it doesn't add quotes to a single word String"""
        test_line = "testingtesting"
        passing_line = "testingtesting"
        self.assertEqual(passing_line, Mission.add_quotes(test_line))
    #end test_add_quotes_single_word

    #TODO: Make sure this throws a custom exception
    def test_add_quotes_non_string(self):
        """Check to make sure it doesn't add quotes to junk data"""
        test_line = 0
        passing_line = "testingtesting"
        self.assertEqual(passing_line, Mission.add_quotes(test_line))
    #end test_add_quotes_non_string
#end class MissionTestCase


if __name__ == "__main__":
    unittest.main()
