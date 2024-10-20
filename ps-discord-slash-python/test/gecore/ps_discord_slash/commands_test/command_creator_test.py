import unittest
import json

import jsonpickle

from gecore.ps_discord_slash.commands.command_manager.manage_commands import create_command_submission
from gecore.ps_discord_slash.implementations.bob_commands.roll_call_command import RollCallInteractionCommand


class CommandCreatorTest(unittest.TestCase):

    def test_things(self):
        # result = CommandManagerInteractionCommand.build()
        # printable = json.loads(jsonpickle.encode(result, unpicklable=False))
        # print(json.dumps(printable))
        #
        # result_two = TestDateInteractionCommand.build(621502053373706241)
        # printable2 = json.loads(jsonpickle.encode(result_two, unpicklable=False))
        # print(json.dumps(printable2))

        result_four = RollCallInteractionCommand.build(621502053373706241)
        printable4 = json.loads(jsonpickle.encode(result_four, unpicklable=False))
        print(json.dumps(printable4))

