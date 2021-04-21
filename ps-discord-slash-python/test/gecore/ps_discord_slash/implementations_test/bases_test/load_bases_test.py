import unittest
import os
import json

from gecore.ps_discord_slash.implementations.bases.load_bases import determine_source


class LoadBasesTest(unittest.TestCase):

    def test_determine_source(self):
        os.environ['LAMBDA_TASK_ROOT'] = '../../../..'
        result = determine_source()
        print(result)
        try:
            map_file = open(result)
            loaded_map = json.load(map_file)
            assert 'map_region_list' in loaded_map
        except IOError:
            print("File not accessible")
            raise
        finally:
            map_file.close()


if __name__ == '__main__':
    unittest.main()
