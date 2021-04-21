import unittest

from gecore.ps_discord_slash.implementations.bases.parse_bases import load_bases


class ParseBasesTest(unittest.TestCase):
    def test_load_bases(self):
        result = load_bases()
        print(result)


if __name__ == '__main__':
    unittest.main()
