from typing import List

from gecore.ps_discord_slash.commands.models.local_commands import GuildSlashCommands
from gecore.ps_discord_slash.implementations.load_guild_commands import load_guild_commands


class GuildCommandManager:
    """Contains a list of all the guilds and their slash commands"""
    guild_command_list = List[GuildSlashCommands]

    def load_guild_list(self):
        self.guild_command_list = load_guild_commands()

    def introduce_guild(self, guild_slash_commands: GuildSlashCommands):
        """"Adds a bare guild to be able to add commands to"""
        self.guild_command_list.append(guild_slash_commands)
