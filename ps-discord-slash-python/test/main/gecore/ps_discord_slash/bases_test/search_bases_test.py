import unittest

from gecore.ps_discord_slash.bases.search_bases import find_bases


class SearchBasesTest(unittest.TestCase):

    def test_find_base_single(self):
        search_arg = 'hvar'
        bases = {'Hvar Tech Plant': 7500, 'Mao Tech Plant': 4401, 'Allatum Bio Lab': 4001, 'Saurva Bio Lab': 3801}
        result = find_bases(bases, search_arg)
        self.assertEqual({'Hvar Tech Plant': 7500}, result)

    def test_find_base_single_complex(self):
        search_arg = 'Auraxi network'
        bases = {'AuraxiCom Substation': 222190, 'Auraxis Firearms Corp.': 218000, 'AuraxiCom Network Hub': 222060}
        result = find_bases(bases, search_arg)
        self.assertEqual({'AuraxiCom Network Hub': 222060}, result)

    def test_find_base_single_complex_similar(self):
        search_arg = 'Auraxi network corp'
        bases = {
            'AuraxiCom Substation': 222190, 'Auraxis Firearms Corp.': 218000,
            'AuraxiCom Network Hub': 222060, 'Zurvan Network Complex': 118030
        }
        result = find_bases(bases, search_arg)
        self.assertEqual({'AuraxiCom Network Hub': 222060, 'Auraxis Firearms Corp.': 218000}, result)


    def test_find_base_multi(self):
        search_arg = 'hvar, mao'
        bases = {'Hvar Tech Plant': 7500, 'Mao Tech Plant': 4401, 'Allatum Bio Lab': 4001, 'Saurva Bio Lab': 3801}
        result = find_bases(bases, search_arg)
        self.assertEqual({'Hvar Tech Plant': 7500, 'Mao Tech Plant': 4401}, result)

    def test_randomly(self):
        search_arg = 'hammer'
        bases = {'Hvar Tech Plant': 7500, 'Mao Tech Plant': 4401, 'Allatum Bio Lab': 4001, 'Saurva Bio Lab': 3801}
        result = find_bases(bases, search_arg)
        print(result)


if __name__ == '__main__':
    unittest.main()
