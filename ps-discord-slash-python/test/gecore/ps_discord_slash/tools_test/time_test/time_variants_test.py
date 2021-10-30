import unittest

from gecore.ps_discord_slash.tools.time.time_variants import grab_month_variant_by_number


class TimeVariantsTest(unittest.TestCase):

    def test_grab_month_variant_by_number(self):
        april = 4
        result = grab_month_variant_by_number(april)
        self.assertEqual(april, result.value[1])
