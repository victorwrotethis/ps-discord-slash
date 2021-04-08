from gecore.ps_discord_slash.commands.command_interface import ISlashCommand
from gecore.ps_discord_slash.implementations.load_commands import load_guild_commands, load_commands
from gecore.ps_discord_slash.commands.models.slash_commands import GuildSlashCommands, GuildSlashCommand
from gecore.ps_discord_slash.exception.exceptions import CommandException, CommandExceptionMessage
from gecore.ps_discord_slash.models.default_interaction_responses import default_command_channel, forbidden_response, \
    not_configured_response
from gecore.ps_discord_slash.models.flags import DiscordFlags
from gecore.ps_discord_slash.models.interactions import InteractionResponseType, InteractionResponse, \
    InteractionResponseData
from gecore.ps_discord_slash.processing.role_checker import check_if_correct_channel, check_if_allowed_role

guilds_command_list = load_guild_commands()
command_list: [ISlashCommand] = load_commands()


def process_command(command_body: {}) -> InteractionResponse:
    incoming_guild_id = int(command_body['guild_id'])
    for guild_commands in guilds_command_list:
        if guild_commands.guild_id == incoming_guild_id:
            print(command_body)
            ovo_command, guild_slash_command = find_command(command_body['data']['name'], guild_commands)
            return process_guild_command(command_body, guild_slash_command, ovo_command)
        else:
            return InteractionResponse(InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE, forbidden_response())


def process_guild_command(command_body: {}, guild_slash_command: GuildSlashCommand, slash_command: ISlashCommand)\
        -> InteractionResponse:
    """"Will perform the command if it is allowed to be executed based on channel and roles"""
    if check_if_allowed_role(command_body['member']['roles'], guild_slash_command):
        if check_if_correct_channel(command_body['channel_id'], guild_slash_command):
            return process_actual_command(command_body, slash_command)
        else:
            return InteractionResponse(
                InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
                default_command_channel(guild_slash_command)
            )
    else:
        return InteractionResponse(InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE, forbidden_response())


def process_actual_command(command_body: {}, slash_command: ISlashCommand):
    """"Will execute the interface method"""
    return slash_command.execute(command_body)


def find_command(incoming_command: str, guild_command_list: GuildSlashCommands) -> {ISlashCommand, GuildSlashCommand}:
    try:
        slash_command = retrieve_command(incoming_command)
        for guild_command in guild_command_list.guild_commands:
            if guild_command.command.name == slash_command.identify():
                return slash_command, guild_command
    except CommandException:
        return not_configured_response()


def retrieve_command(incoming_command: str) -> ISlashCommand:
    for ovo_slash_command in command_list:
        if ovo_slash_command.identify().value == incoming_command:
            return ovo_slash_command
    raise CommandException(CommandExceptionMessage.GuildCommandNotFound)
