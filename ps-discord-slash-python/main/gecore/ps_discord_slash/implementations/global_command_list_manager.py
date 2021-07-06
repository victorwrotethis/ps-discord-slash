from gecore.ps_discord_slash.commands.models.local_commands import SlashCommands
from gecore.ps_discord_slash.implementations.load_global_commands import load_global_commands


class GlobalCommandManager:
    """Contains a list of all the guilds and their slash commands"""
    global_command_list = SlashCommands

    def load_global_list(self):
        self.global_command_list = load_global_commands()
