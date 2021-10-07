from datetime import datetime
import unittest

from gecore.ps_discord_slash.commands.support.date_picker_buttons.date_picker_buttons import create_date_buttons_from
from gecore.ps_discord_slash.tools.time.time_converter import create_utc_timestamp
from gecore.ps_discord_slash.tools.time.time_service import get_current_time, grab_previous_day
from gecore.ps_discord_slash.tools.time.time_variants import TimeZoneVariant


class DatePickerButtonsTest(unittest.TestCase):

    def test_create_date_buttons_from(self):
        # -1 day because there's the chance the UTC day is 1 day before current UTC day
        current_time = get_current_time()
        previous_day = grab_previous_day(current_time)
        print(previous_day)
        result = create_date_buttons_from('datepicker', previous_day, True)
        pass




if __name__ == '__main__':
    unittest.main()
