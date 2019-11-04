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


    def test_parse_name(self):
        tokens = ["name", "test mission"]
        self.parser._parse_name(tokens)
        self.assertEqual(tokens[1], self.parser.mission.components.mission_display_name)
    #end test_parse_name


    def test_parse_description(self):
        tokens = ["description", "A test mission"]
        self.parser._parse_description(tokens)
        self.assertEqual(tokens[1], self.parser.mission.components.description)
    #end test_parse_description


    def test_parse_blocked(self):
        tokens = ["blocked", "Oh piss off!"]
        self.parser._parse_blocked(tokens)
        self.assertEqual(tokens[1], self.parser.mission.components.blocked)
    #end test_parse_blocked


    def test_parse_deadline(self):
        tokens = ["deadline", "2", "1"]
        self.parser._parse_deadline(tokens)
        self.assertEqual(tokens[1:], self.parser.mission.components.deadline.deadline)
    #end test_parse_deadline


    def test_parse_cargo(self):
        tokens = ["cargo", "food", "5", "2", "0.1"]
        self.parser._parse_cargo(tokens)
        self.assertEqual(tokens[1:], self.parser.mission.components.cargo.cargo)
    #end test_parse_cargo


    def test_parse_passengers(self):
        tokens = ["passengers", "5", "5", "0.2"]
        self.parser._parse_passengers(tokens)
        self.assertEqual(tokens[1:], self.parser.mission.components.passengers.passengers)
    #end test_parse_passengers


    def test_parse_illegal(self):
        tokens = ["illegal", "50", "Soviet citizens need no food comrade"]
        self.parser._parse_illegal(tokens)
        self.assertEqual(tokens[1:], self.parser.mission.components.illegal.illegal)
    #end test_parse_illegal

    def test_parse_stealth(self):
        self.parser._parse_stealth()
        self.assertEqual(True, self.parser.mission.components.is_stealth)
    # end test_parse_stealth


    def test_parse_invisible(self):
        self.parser._parse_invisible()
        self.assertEqual(True, self.parser.mission.components.is_invisible)
    # end test_parse_invisible


    def test_parse_priority_level(self):
        tokens = ["priority"]
        self.parser._parse_priority_level(tokens)
        self.assertEqual(tokens[0], self.parser.mission.components.priority_level)
    # end test_parse_priority_level


    def test_parse_where_shown(self):
        tokens = ["landing"]
        self.parser._parse_where_shown(tokens)
        self.assertEqual(tokens[0], self.parser.mission.components.where_shown)
    # end test_parse_where_shown


    def test_parse_repeat(self):
        tokens = ["repeat", "5"]
        self.parser._parse_repeat(tokens)
        self.assertEqual(tokens[1], self.parser.mission.components.repeat.repeat)
    #end test_parse_repeat


    def test_parse_clearance(self):
        tokens = ["clearance", "You're on the list"]
        self.parser._parse_clearance(tokens)
        self.assertEqual(tokens[1], self.parser.mission.components.clearance.clearance)
    #end test_parse_clearance


    def test_parse_infiltrating(self):
        self.parser._parse_infiltrating()
        self.assertEqual(True, self.parser.mission.components.is_infiltrating)
    # end test_parse_infiltrating


    def test_parse_waypoint(self):
        tokens = ["waypoint", "Sol"]
        self.parser._parse_waypoint(tokens)
        self.assertEqual(tokens[1], self.parser.mission.components.waypoint)
    #end test_parse_waypoint


    def test_parse_stopover(self):
        tokens = ["stopover", "Delve"]
        self.parser._parse_stopover(tokens)
        self.assertEqual(tokens[1], self.parser.mission.components.stopover.stopover)
    #end test_parse_stopover


    def test_parse_source(self):
        tokens = ["source", "Sol"]
        self.parser._parse_source(tokens)
        self.assertEqual(tokens[1], self.parser.mission.components.source.source)
    #end test_parse_source


    def test_parse_destination(self):
        tokens = ["destination", "Delve"]
        self.parser._parse_destination(tokens)
        self.assertEqual(tokens[1], self.parser.mission.components.destination.destination)
    #end test_parse_destination
#end class FileMissionItemParser
