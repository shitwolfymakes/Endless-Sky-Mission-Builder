import unittest
from src.model.MissionFileParser import MissionFileParser


class MissionFileParserTestCase(unittest.TestCase):
    #TODO: Add test for run()
    """Tests for `MissionFileParser.py`."""


    def setUp(self):
        self.test_lines = ['mission "Test"\n', '\tname "Testing"\n', "\n", "\n", "\n", 'event "Testing end"']
        self.parser = MissionFileParser(self.test_lines)
    #end set_up_parser


    def test_store_item_for_parsing(self):
        passing_lines = ['mission "Test"\n', '\tname "Testing"\n', "\n", "\n", "\n"]
        self.parser.store_item_for_parsing(0, self.test_lines[0], "mission")
        self.assertEqual(self.parser.file_items[0], ("mission", passing_lines))
    #end test_store_item_for_parsing


    def test_end_of_item_condition_true(self):
        self.assertTrue(self.parser.end_of_item_condition(self.test_lines[0]), True)
    #end test_end_of_item_condition_true


    def test_end_of_item_condition_false(self):
        self.assertFalse(self.parser.end_of_item_condition(self.test_lines[1]), False)
    #end test_end_of_item_condition_false


    def test_is_eof_true(self):
        last_line_num = len(self.test_lines) - 1
        self.assertTrue(self.parser.is_eof(last_line_num, self.test_lines), True)
    #end test_is_eof_true


    def test_is_eof_false(self):
        self.assertFalse(self.parser.is_eof(0, self.test_lines), False)
    #end test_is_eof_false
#end class MissionFileParserTestCase
