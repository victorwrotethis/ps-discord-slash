import unittest

from gecore.ps_discord_slash.commands.support.datetime_picking.date.date_picker_buttons import create_date_buttons_from, \
    add_navigation_buttons
from gecore.ps_discord_slash.tools.time.time_service import get_current_time


class DatePickerButtonsTest(unittest.TestCase):

    def test_create_date_buttons_from(self):
        # -1 day because there's the chance the UTC day is 1 day before current UTC day
        current_time = get_current_time()
        print(current_time)
        result = create_date_buttons_from('datepicker', current_time, True)
        pass


    def test_add_navigation_buttons(self):
        reference_time = 1633046400
        result = add_navigation_buttons('test', reference_time, True)
        self.assertTrue(result.components[0].disabled)
        result_two = add_navigation_buttons('test', reference_time, False)
        self.assertFalse(result_two.components[0].disabled)


    def test_create_date_buttons_from_two(self):
        result = create_date_buttons_from('datepicker', 1634421600, True)
        print('ho')





if __name__ == '__main__':
    unittest.main()
