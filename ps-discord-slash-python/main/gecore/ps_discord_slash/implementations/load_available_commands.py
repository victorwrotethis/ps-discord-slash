from gecore.ps_discord_slash.commands.command_manager.manage_command_command import ManageCommandSlashCommand
from gecore.ps_discord_slash.commands.models.available_commands import AvailableCommands
from gecore.ps_discord_slash.implementations.bases.search_base_command import SearchBaseSlashCommand
from gecore.ps_discord_slash.implementations.unplug.unplug_command import UnplugSlashCommand


class LoadedCommands:
    """Defers loading the commands until needed"""
    available_commands: AvailableCommands

    def load_commands(self):
        self.available_commands = AvailableCommands([
            SearchBaseSlashCommand(),
            ManageCommandSlashCommand(),
            UnplugSlashCommand()
        ])

    # def retrieve_command_from_pool(self, incoming_command: str):
    #     if self.available_commands.command_list:
    #         return self.available_commands.retrieve_command(incoming_command)
    #     else:


