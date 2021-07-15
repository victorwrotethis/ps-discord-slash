from gecore.ps_discord_slash.commands.command_interface import InteractionCommand
from gecore.ps_discord_slash.commands.models.local_commands import CommandSearchResult, GuildSlashCommands
from gecore.ps_discord_slash.exception.exceptions import CommandException, CommandExceptionMessage
from gecore.ps_discord_slash.processing.global_command_service import find_global_command
from gecore.ps_discord_slash.processing.guild_command_service import find_guild_commands, create_guild_and_add_global, \
    add_global_to_guild


def check_for_guild_and_command(slash_command: InteractionCommand, incoming_guild_id: int) -> CommandSearchResult:
    """Checks if it can find the guild commands. On the absence of the guild in system, it will add it."""
    try:
        guild_and_its_commands = find_guild_commands(incoming_guild_id)
        return check_for_command_in_guild(slash_command, guild_and_its_commands)
    except CommandException as err:
        if err.message is CommandExceptionMessage.GuildNotFound:
            guild_global_command = create_guild_and_add_global(slash_command, incoming_guild_id)
            return CommandSearchResult(has_been_found=True, found_command=guild_global_command)
        return CommandSearchResult(has_been_found=False, error_response=err)


def check_for_command_in_guild(slash_command: InteractionCommand, guild_and_its_commands: GuildSlashCommands) \
        -> CommandSearchResult:
    """"Checks if a command is in a guild, adds it if absent."""
    try:
        guild_command = guild_and_its_commands.find_command(slash_command)
        return CommandSearchResult(has_been_found=True, found_command=guild_command)
    except CommandException as err:
        if err.message is CommandExceptionMessage.GuildCommandNotFound:
            guild_command = add_global_to_guild(slash_command, guild_and_its_commands)
            return CommandSearchResult(has_been_found=True, found_command=guild_command)
        return CommandSearchResult(has_been_found=False, error_response=err)


def check_for_command_in_global(slash_command: InteractionCommand) -> CommandSearchResult:
    try:
        global_command = find_global_command(slash_command)
        return CommandSearchResult(has_been_found=True, found_command=global_command)
    except CommandException as err:
        return CommandSearchResult(has_been_found=False, error_response=err)
