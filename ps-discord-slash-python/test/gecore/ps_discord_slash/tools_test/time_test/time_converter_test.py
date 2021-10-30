import unittest

from gecore.ps_discord_slash.tools.time.time_converter import create_utc_timestamp, convert_time_of_day_to_24h
from gecore.ps_discord_slash.tools.time.time_variants import MonthVariant, TimeZoneVariant, TimeVariant


class TimeConverterTest(unittest.TestCase):

    def test_create_timestamp_UTC(self):
        result = create_utc_timestamp(
            hour=10,
            minute=30,
            month_variant=MonthVariant.MAR,
            day=5,
            timezone_variant=TimeZoneVariant.UTC
        )
        self.assertEqual(1614940200, result)
        pass

    def test_create_timestamp_EASTERN(self):
        result = create_utc_timestamp(
            hour=10,
            minute=30,
            month_variant=MonthVariant.MAR,
            day=5,
            timezone_variant=TimeZoneVariant.EASTERN
        )
        self.assertEqual(1614958200, result)

    def test_convert_time_of_day_to_24h(self):
        mid_afternoon = convert_time_of_day_to_24h(12, TimeVariant.PM)
        two_afternoon = convert_time_of_day_to_24h(2, TimeVariant.PM)
        midnight = convert_time_of_day_to_24h(12, TimeVariant.AM)
        two_after_midnight = convert_time_of_day_to_24h(2, TimeVariant.AM)
        self.assertEqual(12, mid_afternoon)
        self.assertEqual(14, two_afternoon)
        self.assertEqual(0, midnight)
        self.assertEqual(2, two_after_midnight)

    def test_create_timestamp_EASTERN_PM(self):
        result = create_utc_timestamp(
            hour=10,
            minute=30,
            month_variant=MonthVariant.MAR,
            day=5,
            timezone_variant=TimeZoneVariant.EASTERN,
            time_variant=TimeVariant.PM
        )
        self.assertEqual(1615001400, result)


if __name__ == '__main__':
    unittest.main()
