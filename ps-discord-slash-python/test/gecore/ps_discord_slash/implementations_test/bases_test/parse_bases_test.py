import unittest
import os

from gecore.ps_discord_slash.implementations.bases.parse_bases import BasesParser


class ParseBasesTest(unittest.TestCase):
    def test_load_bases(self):
        # Arrange
        os.environ['MAP_REGION_LOCATION'] = '../../../../resources/map_region.json'
        parser = BasesParser()
        # Act
        base_list = parser.create_base_list()
        # Assert
        # Normal bases
        self.assertEqual(base_list['Hvar Tech Plant'], 7500)
        # Extra loaded bases
        self.assertEqual(base_list['Koltyr Amp Station Outpost'], 400022)


if __name__ == '__main__':
    unittest.main()
