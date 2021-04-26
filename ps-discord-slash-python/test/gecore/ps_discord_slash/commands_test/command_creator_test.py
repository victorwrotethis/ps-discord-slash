import unittest
import json
from unittest.mock import patch, MagicMock

import jsonpickle

from gecore.ps_discord_slash.implementations.created_commands import create_command_submission
from gecore.ps_discord_slash.implementations.bases.search_base_command import SearchBaseSlashCommand


class CommandCreatorTest(unittest.TestCase):
    @patch('gecore.ps_discord_slash.implementations.bases.search_base_command.BasesParser')
    def test_searchbaseid_command(self, mock_bases):
        """"Checks if commands generate the expected values in json"""
        # Arrange
        command_id = 1
        guild_id = 2
        version = 3
        # Act
        search_base_id = SearchBaseSlashCommand.build(command_id, guild_id, version)
        search_base_id_submission = create_command_submission(search_base_id)
        submittable_command_result = json.loads(jsonpickle.encode(search_base_id_submission, unpicklable=False))
        created_command_result = json.loads(jsonpickle.encode(search_base_id, unpicklable=False))
        # Assert
        # submittable command
        self.assertEqual('searchbaseid', submittable_command_result['name'])
        self.assertEqual(True, submittable_command_result['options'][0]['required'])
        # previously submitted command
        self.assertEqual(str(command_id), created_command_result['id'])
        self.assertEqual(guild_id, created_command_result['guild_id'])
        self.assertEqual(version, created_command_result['version'])



