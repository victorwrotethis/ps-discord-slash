import unittest

from gecore.ps_discord_slash.bases.models.base_response import create_base_embeds, create_base_response
from gecore.ps_discord_slash.models.response_models import generic_response


class BaseResponseTest(unittest.TestCase):
    def test_create_base_embeds(self):
        base_list = {'Hvar Tech Plant': 9342, 'Hvar Not Plant': 2342}
        result = create_base_embeds(base_list)
        print(result)

    def test_generic_response(self):
        base_list = {'Hvar Tech Plant': 9342, 'Hvar Not Plant': 2342}
        command_result = create_base_response(base_list, 'Hvar')
        response = generic_response(command_result.type, command_result.data)
        print(response)


if __name__ == '__main__':
    unittest.main()

