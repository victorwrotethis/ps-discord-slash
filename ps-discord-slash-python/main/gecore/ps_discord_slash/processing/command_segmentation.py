from gecore.ps_discord_slash.commands.command_interface import ISlashCommand
from gecore.ps_discord_slash.commands.models.available_commands import AvailableCommands
from gecore.ps_discord_slash.commands.models.guild_commands import GuildSlashCommand, GuildSlashCommands
from gecore.ps_discord_slash.implementations.bases.search_base_command import SearchBaseSlashCommand
from gecore.ps_discord_slash.commands.command_manager.manage_command_command import ManageCommandSlashCommand
from gecore.ps_discord_slash.implementations.load_guild_commands import load_guild_commands

available_commands = None #load_available_commands()


def retrieve_guild_command(command_body: {}) -> {GuildSlashCommand, ISlashCommand}:
    incoming_guild_id = int(command_body['guild_id'])
    incoming_command = command_body['data']['name']

    slash_command = available_commands.retrieve_command(incoming_command)
    # Todo distinguish grabbing guild or global command
    #  If it is a global command, check if there are perms. If not then only admin is allowed. -> we got StartingPerms
    #  If it's a guild command, retrieve the perms and deny if they aren't set .
    #  Basically we start off with the global which is just to enable for the guild.
    #  I guess we have the potential issue of those being show in DMs however.

    # we should get a member, if we don't we toss the command?
    # if user toss command?

    # Todo distinguish finding out if the guild has perms vs grabbing guild command

    return {}


def find_guild_commands(incoming_guild_id: int) -> GuildSlashCommands:
    """"Tries to find out if the guild can be found in the list of configured commands"""
    guilds_command_list = load_guild_commands()
    for guild_commands in guilds_command_list:
        if guild_commands.guild_id == incoming_guild_id:
            return guild_commands
    # todo throw an error here that the command has not been configured yet


def load_available_commands() -> AvailableCommands:
    return AvailableCommands([SearchBaseSlashCommand(), ManageCommandSlashCommand()])