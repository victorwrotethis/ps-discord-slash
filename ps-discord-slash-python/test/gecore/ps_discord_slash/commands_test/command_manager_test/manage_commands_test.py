import unittest

from gecore.ps_discord_slash.commands.command_manager.manage_commands import ManageCommands, \
    find_abbreviated_manage_command_variant


class ManageCommandsTest(unittest.TestCase):
    def test_things(self):
        things = ManageCommands.COMMAND_MANAGER
        thing = find_abbreviated_manage_command_variant(things)
        print(thing)
