import unittest
import json
from unittest.mock import patch

import jsonpickle

from gecore.ps_discord_slash.commands.command_manager.command_manager_command import CommandManagerInteractionCommand
from gecore.ps_discord_slash.commands.command_manager.manage_commands import create_command_submission
from gecore.ps_discord_slash.implementations.bases.search_base_command import SearchBaseSlashCommand
from gecore.ps_discord_slash.implementations.bob_commands.roll_call_command import RollCallInteractionCommand
from gecore.ps_discord_slash.implementations.pretty_time.test_date_command import TestDateInteractionCommand
from gecore.ps_discord_slash.implementations.reservation.start_reservation_command import StartReservationSlashCommand


class CommandCreatorTest(unittest.TestCase):
    @patch('gecore.ps_discord_slash.implementations.bases.search_base_command.BasesParser')
    def test_searchbaseid_command(self, mock_bases):
        """"Checks if commands generate the expected values in json"""
        # Arrange
        guild_id = 2
        # Act
        search_base_id = SearchBaseSlashCommand.build(guild_id)
        search_base_id_submission = create_command_submission(search_base_id)
        submittable_command_result = json.loads(jsonpickle.encode(search_base_id_submission, unpicklable=False))
        created_command_result = json.loads(jsonpickle.encode(search_base_id, unpicklable=False))
        # Assert
        # submittable command
        self.assertEqual('searchbaseid', submittable_command_result['name'])
        self.assertEqual('True', submittable_command_result['options'][0]['required'])
        # previously submitted command
        self.assertEqual(guild_id, created_command_result['guild_id'])

    def test_things(self):
        # result = CommandManagerInteractionCommand.build()
        # printable = json.loads(jsonpickle.encode(result, unpicklable=False))
        # print(json.dumps(printable))
        #
        # result_two = TestDateInteractionCommand.build(621502053373706241)
        # printable2 = json.loads(jsonpickle.encode(result_two, unpicklable=False))
        # print(json.dumps(printable2))
        #
        # result_three = StartReservationSlashCommand.build(621502053373706241)
        # printable3 = json.loads(jsonpickle.encode(result_three, unpicklable=False))
        # print(json.dumps(printable3))

        result_four = RollCallInteractionCommand.build(621502053373706241)
        printable4 = json.loads(jsonpickle.encode(result_four, unpicklable=False))
        print(json.dumps(printable4))

