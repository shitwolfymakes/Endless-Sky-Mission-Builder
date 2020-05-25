import unittest

from src.model import MissionComponents
from src.model.file_data_parsers.FileMissionItemParser import FileMissionItemParser


class FileMissionItemParserTestCase(unittest.TestCase):
    #TODO: Add test for run()
    """Tests for `FileMissionItemParser.py`."""

    def setUp(self):
        self.test_lines = ['mission "Testing testing"\n', '\tcargo "scanning equipment" 8"\n', "\n", "\n", "\n"]
        self.parser = FileMissionItemParser(self.test_lines)
        self.parser.mission.add_trigger()
        self.trigger = self.parser.mission.components.trigger_list[-1]
    #end setUp


    #TODO: Move this to a test_file_item_parser.py
    def test_strip_ending_whitespace(self):
        passing_lines = ['mission "Testing testing"\n', '\tcargo "scanning equipment" 8"\n']
        self.parser.strip_ending_whitespace(self.test_lines)
        self.assertEqual(self.test_lines, passing_lines)
    #end test_strip_ending_whitespace


    # TODO: Move this to a test_file_item_parser.py
    def test_tokenize(self):
        tokens = FileMissionItemParser.tokenize('mission "Testing testing"\n')
        passing_tokens = ["mission", "Testing testing"]
        self.assertEqual(passing_tokens, tokens)
    #end test_tokenize


    # TODO: Move this to a test_file_item_parser.py
    def test_get_indent_level(self):
        passing_data = 0
        self.assertEqual(FileMissionItemParser.get_indent_level(self.test_lines[0]), passing_data)
    #end test_get_indent_level


    # TODO: Move this to a test_file_item_parser.py
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


    def test_parse_trigger(self):
        pass
    #end test_parse_trigger


    def test_parse_dialog(self):
        tokens = ["dialog", "It is Wednesday my dudes"]
        self.parser._parse_dialog(self.trigger, tokens)
        self.assertEqual(tokens[1], self.trigger.dialog)
    #end test_parse_dialog


    def test_parse_outfit(self):
        tokens = ["outfit", "Skylance V", "5"]
        self.parser._parse_outfit(self.trigger, tokens)
        self.assertEqual(tokens[1:], self.trigger.outfit)
    #end test_parse_outfit


    def test_parse_require(self):
        tokens = ["require", "Hyperdrive", "1"]
        self.parser._parse_require(self.trigger, tokens)
        self.assertEqual(tokens[1:], self.trigger.require)
    #end test_parse_require


    def test_parse_payment(self):
        tokens = ["payment", "1500", "0.2"]
        self.parser._parse_payment(self.trigger, tokens)
        self.assertTrue(self.trigger.is_payment)
        self.assertEqual(tokens[1:], self.trigger.payment)
    # end test_parse_payment


    def test_parse_event(self):
        tokens = ["event", "blaze it", "420", "4200"]
        self.parser._parse_event(self.trigger, tokens)
        self.assertEqual(tokens[1:], self.trigger.event)
    #end test_parse_event


    def test_parse_fail(self):
        tokens = ["fail", "the mission"]
        self.parser._parse_fail(self.trigger, tokens)
        self.assertTrue(self.trigger.is_fail)
        self.assertEqual(tokens[1], self.trigger.fail)
    #end test_parse_fail


    def test_parse_log_type_1(self):
        tokens = ["log", "my mama ain't a ho"]
        self.parser._parse_log_type_1(self.trigger, tokens)
        self.assertTrue(self.trigger.logs[0].is_active)
        self.assertEqual("<message>", self.trigger.logs[0].format_type)
        self.assertEqual([tokens[1], None, None], self.trigger.logs[0].log)
    #end test_parse_log_type_1


    def test_parse_log_type_3(self):
        tokens = ["log", "People", "Yo mama", "is a ho"]
        self.parser._parse_log_type_3(self.trigger, tokens)
        self.assertTrue(self.trigger.logs[0].is_active)
        self.assertEqual("<type> <name> <message>", self.trigger.logs[0].format_type)
        self.assertEqual(tokens[1:], self.trigger.logs[0].log)
    #end test_parse_log_type_3


    def test_parse_condition_type_0(self):
        tokens = ["yo mama", "+=", "20"]
        self.parser._parse_condition_type_0(self.trigger, tokens)
        self.assertTrue(self.trigger.conditions[0].is_active)
        self.assertEqual(0, self.trigger.conditions[0].condition_type)
        self.assertEqual(tokens, self.trigger.conditions[0].condition)
    #end test_parse_condition_type_0


    def test_parse_condition_type_1(self):
        tokens = ["no u", "++"]
        self.parser._parse_condition_type_1(self.trigger, tokens)
        self.assertTrue(self.trigger.conditions[0].is_active)
        self.assertEqual(1, self.trigger.conditions[0].condition_type)
        self.assertEqual([tokens[0], tokens[1], None], self.trigger.conditions[0].condition)
    #end test_parse_condition_type_1


    def test_parse_condition_type_2(self):
        tokens = ["clear", "the drugs"]
        self.parser._parse_condition_type_2(self.trigger, tokens)
        self.assertTrue(self.trigger.conditions[0].is_active)
        self.assertEqual(2, self.trigger.conditions[0].condition_type)
        self.assertEqual([tokens[0], tokens[1], None], self.trigger.conditions[0].condition)
    #end test_parse_condition_type_2


    @staticmethod
    def _get_trigger_lines():
        lines = ["\ton offer\n",
                 "\t\tconversation\n",
                 "\t\t\tscene \"testing testing\"\n",
                 "\t\t\t`A Navy officer asks if you can do a job for him.`\n",
                 "\t\t\tchoice\n",
                 "\t\t\t\t`	\"Sure, I'd love to.\"`\n",
                 "\t\t\t\t\taccept\n",
                 "\t\t\t\t`	\"Sorry, I'm on an urgent cargo mission.\"`\n",
                 "\t\t\t\t\tdecline\n",
                 "\t\t\t\t`(Attack him.)`\n",
                 "\t\t\t\t\tgoto \"bad idea\"\n",
                 "\t\t\tlabel \"bad idea\"\n",
                 "\t\t\t`	You shout \"Death to all tyrants!\" and go for your gun.`\n",
                 "\t\t\t`	Unfortunately, he pulls his own gun first.`\n",
                 "\t\t\t\tdie\n",
                 "\t\t\tname\n",
                 "\t\t\t`	testing testing`\n",
                 "\t\tdialog `It is Wednesday my dudes`\n",
                 "\t\toutfit \"Skylance V\" 5\n",
                 "\t\trequire Hyperdrive 1\n",
                 "\t\tpayment 1500 0.2\n",
                 "\t\t\"yo mama\" += 20\n",
                 "\t\t\"no u\" ++\n",
                 "\t\tclear \"the drugs\"\n",
                 "\t\tevent \"blaze it\" 420 4200\n",
                 "\t\tfail \"the mission\"\n",
                 "\t\tlog `my mama ain't a ho`\n",
                 "\t\tlog \"People\" \"Yo mama\" `is a ho`\n"]
        return lines
    #end _get_trigger_lines
#end class FileMissionItemParser
