import unittest
import json

from gecore.ps_discord_slash.bases.parse_bases import load_bases


class ParseBasesTest(unittest.TestCase):
    def test_load_bases(self):
        result = load_bases()
        print(result)
