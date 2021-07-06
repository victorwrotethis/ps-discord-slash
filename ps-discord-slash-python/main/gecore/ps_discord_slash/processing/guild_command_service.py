from gecore.ps_discord_slash.commands.command_interface import ISlashCommand
from gecore.ps_discord_slash.commands.models.local_commands import GuildSlashCommands, SlashCommand
from gecore.ps_discord_slash.exception.exceptions import CommandException, CommandExceptionMessage
from gecore.ps_discord_slash.implementations.guild_command_list_manager import GuildCommandManager
from gecore.ps_discord_slash.processing.global_command_service import find_global_command

guild_manager = GuildCommandManager()


def find_guild_commands(incoming_guild_id: int) -> GuildSlashCommands:
    """Tries to find out if the guild can be found in the list of configured commands"""

    if guild_manager.guild_command_list:
        guild_manager.load_guild_list()
    for guild_commands in guild_manager.guild_command_list:
        if guild_commands.guild_id == incoming_guild_id:
            return guild_commands
    raise CommandException(CommandExceptionMessage.GuildNotFound)


def create_guild_list(guild_id: int) -> GuildSlashCommands:
    guild_slash_commands = GuildSlashCommands(guild_id)
    guild_manager.introduce_guild(guild_slash_commands)
    return guild_slash_commands


def add_global_command_to_guild_list(guild_commands: GuildSlashCommands, global_command: SlashCommand) -> SlashCommand:
    guild_global_command = SlashCommand(global_command.command, global_command.perms)
    guild_commands.commands.append(guild_global_command)
    return guild_global_command


def add_global_to_guild(slash_command: ISlashCommand, guild_and_its_commands: GuildSlashCommands) -> SlashCommand:
    """Adds global command to guild"""
    global_command = find_global_command(slash_command)
    return add_global_command_to_guild_list(guild_and_its_commands, global_command)


def create_guild_and_add_global(slash_command: ISlashCommand, incoming_guild_id: int) -> SlashCommand:
    """"Creates instance of the guild and adds the global command"""
    guild_commands = create_guild_list(incoming_guild_id)
    global_command = find_global_command(slash_command)
    guild_global_command = add_global_command_to_guild_list(guild_commands, global_command)
    return guild_global_command
