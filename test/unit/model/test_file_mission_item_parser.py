import unittest

from src.model import MissionComponents
from src.model.file_data_parsers.FileMissionItemParser import FileMissionItemParser


class FileMissionItemParserTestCase(unittest.TestCase):
    #TODO: Add test for run()
    """Tests for `FileMissionItemParser.py`."""

    def setUp(self):
        self.test_lines = ['mission "Testing testing"\n', '\tcargo "scanning equipment" 8"\n', "\n", "\n", "\n"]
        self.parser = FileMissionItemParser(self.test_lines)
    #end setUp


    def test_strip_ending_whitespace_from_lines(self):
        passing_lines = ['mission "Testing testing"\n', '\tcargo "scanning equipment" 8"\n']
        self.parser.strip_ending_whitespace_from_lines()
        self.assertEqual(self.parser.lines, passing_lines)
    #end test_strip_ending_whitespace_from_lines


    def test_tokenize(self):
        tokens = FileMissionItemParser.tokenize('mission "Testing testing"\n')
        passing_tokens = ["mission", "Testing testing"]
        self.assertEqual(passing_tokens, tokens)
    #end test_tokenize


    def test_get_indent_level(self):
        passing_data = 0
        self.assertEqual(FileMissionItemParser.get_indent_level(self.test_lines[0]), passing_data)
    #end test_get_indent_level


    def test_store_component_data(self):
        passing_data = ["scanning equipment", "8", None, None]
        component = MissionComponents()
        test_data = FileMissionItemParser.tokenize(self.test_lines[1])
        FileMissionItemParser.store_component_data(component.cargo.cargo, test_data[1:])
        self.assertEqual(component.cargo.cargo, passing_data)
    #end test_store_component_data
#end class FileMissionItemParser
