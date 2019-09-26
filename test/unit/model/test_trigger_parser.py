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


    ### outfit
    def test_has_outfit_true(self):
        test_model = self.get_empty_test_model()
        trigger = test_model.components.triggerList[0]
        trigger.outfit = "Skylance V"
        self.assertTrue(test_model._has_outfit())
    # end test_has_outfit_true


    def test_has_outfit_false(self):
        test_model = self.get_empty_test_model()
        self.assertFalse(test_model._has_outfit())
    # end test_has_outfit_false


    def test_parse_outfit(self):
        true_output = '\t\toutfit "Skylance V" 5\n'
        test_model = self.get_empty_test_model()
        trigger = test_model.components.triggerList[0]
        trigger.outfit = ["Skylance V", 5]
        test_model._parse_outfit()
        self.assertEqual(true_output, test_model.lines[0])
    # end test_parse_outfit

    ### require
    def test_has_require_true(self):
        test_model = self.get_empty_test_model()
        trigger = test_model.components.triggerList[0]
        trigger.require = "Hyperdrive"
        self.assertTrue(test_model._has_require())
    # end test_has_require_true


    def test_has_require_false(self):
        test_model = self.get_empty_test_model()
        self.assertFalse(test_model._has_require())
    # end test_has_require_false


    def test_parse_require(self):
        true_output = '\t\trequire Hyperdrive 1\n'
        test_model = self.get_empty_test_model()
        trigger = test_model.components.triggerList[0]
        trigger.require = ["Hyperdrive", 1]
        test_model._parse_require()
        self.assertEqual(true_output, test_model.lines[0])
    # end test_parse_require


    ### payment
    def test_has_payment_true(self):
        test_model = self.get_empty_test_model()
        trigger = test_model.components.triggerList[0]
        trigger.isPayment = True
        self.assertTrue(test_model._has_payment())
    # end test_has_payment_true


    def test_has_payment_false(self):
        test_model = self.get_empty_test_model()
        self.assertFalse(test_model._has_payment())
    # end test_has_payment_false


    def test_parse_payment(self):
        true_output = '\t\tpayment 1500 0.2\n'
        test_model = self.get_empty_test_model()
        trigger = test_model.components.triggerList[0]
        trigger.isPayment = True
        trigger.payment = [1500, 0.2]
        test_model._parse_payment()
        self.assertEqual(true_output, test_model.lines[0])
    # end test_parse_payment


    ### conditions
    def test_has_conditions_true(self):
        test_model = self.get_empty_test_model()
        trigger = test_model.components.triggerList[0]
        self.add_condition_to_trigger(trigger)
        self.assertTrue(test_model._has_conditions())
    # end test_has_require_true


    def test_has_conditions_false(self):
        test_model = self.get_empty_test_model()
        self.assertFalse(test_model._has_conditions())
    # end test_has_require_false


    def test_parse_conditions_conditionType_0(self):
        true_output = '\t\t"yo mama" += 20\n'
        test_model = self.get_empty_test_model()
        trigger = test_model.components.triggerList[0]
        self.add_condition_to_trigger(trigger)
        trigger.conditions[0].set(0, ["yo mama", "+=", 20])
        test_model._parse_conditions()
        self.assertEqual(true_output, test_model.lines[0])
    # end test_parse_conditions_conditionType_0


    def test_parse_conditions_conditionType_1(self):
        true_output = '\t\t"no u" ++\n'
        test_model = self.get_empty_test_model()
        trigger = test_model.components.triggerList[0]
        self.add_condition_to_trigger(trigger)
        trigger.conditions[0].set(1, ["no u", "++"])
        test_model._parse_conditions()
        self.assertEqual(true_output, test_model.lines[0])
    # end test_parse_conditions_conditionType_1


    def test_parse_conditions_conditionType_2(self):
        true_output = '\t\tclear "the drugs"\n'
        test_model = self.get_empty_test_model()
        trigger = test_model.components.triggerList[0]
        self.add_condition_to_trigger(trigger)
        trigger.conditions[0].set(2, ["clear", "the drugs"])
        test_model._parse_conditions()
        self.assertEqual(true_output, test_model.lines[0])
    # end test_parse_conditions_conditionType_2


    ### event
    def test_has_event_true(self):
        test_model = self.get_empty_test_model()
        trigger = test_model.components.triggerList[0]
        trigger.event = ["blaze it", 420, 4200]
        self.assertTrue(test_model._has_event())
    # end test_has_event_true


    def test_has_event_false(self):
        test_model = self.get_empty_test_model()
        self.assertFalse(test_model._has_event())
    # end test_has_event_false


    def test_parse_event(self):
        true_output = '\t\tevent "blaze it" 420 4200\n'
        test_model = self.get_empty_test_model()
        trigger = test_model.components.triggerList[0]
        trigger.event = ["blaze it", 420, 4200]
        test_model._parse_event()
        self.assertEqual(true_output, test_model.lines[0])
    # end test_parse_event


    @staticmethod
    def get_empty_test_model():
        mission = model.Mission("Testing")
        mission.add_trigger()
        test_model = model.TriggerParser(mission)
        test_model.trigger = test_model.components.triggerList[0]
        return test_model
    # end get_empty_test_model


    @staticmethod
    def add_condition_to_trigger(trigger):
        trigger.add_tc()
    #end add_condition_to_trigger
#end class TriggerParserTestCase


if __name__ == "__main__":
    unittest.main()
