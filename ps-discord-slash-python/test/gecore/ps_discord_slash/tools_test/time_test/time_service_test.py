import unittest

from gecore.ps_discord_slash.tools.time.time_service import get_month_from_timestamp


class TimeServiceTest(unittest.TestCase):

    def test_get_month_from_timestamp(self):
        october = 10
        october_first_timestamp = 1633046400
        result = get_month_from_timestamp(october_first_timestamp)
        self.assertEqual(october, result.value[1])
