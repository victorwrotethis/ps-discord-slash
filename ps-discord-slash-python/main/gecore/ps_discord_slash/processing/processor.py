from gecore.ps_discord_slash.bases.parse_bases import load_bases
from gecore.ps_discord_slash.bases.search_bases import find_bases
from gecore.ps_discord_slash.bases.models.base_response import create_base_response
from gecore.ps_discord_slash.commands.available_commands import OvOSlashCommand
from gecore.ps_discord_slash.commands.load_commands import load_commands
from gecore.ps_discord_slash.commands.models.slash_commands import GuildSlashCommands, GuildSlashCommand
from gecore.ps_discord_slash.exception.exceptions import CommandException, CommandExceptionMessage
from gecore.ps_discord_slash.models.discord_config import JaegerEventChannel
from gecore.ps_discord_slash.models.flags import DiscordFlags
from gecore.ps_discord_slash.models.interactions import InteractionResponseType, InteractionResponse, \
    InteractionResponseData
from gecore.ps_discord_slash.processing.role_checker import check_if_correct_channel, check_if_allowed_role

guilds_command_list = load_commands()
base_list = load_bases()
empty_response = InteractionResponseData(None, None, DiscordFlags.NONE)
forbidden_response = InteractionResponseData('You are not allowed to use this command', None, DiscordFlags.HIDDEN)
wrong_channel_response = InteractionResponseData(f'Please use the <#{JaegerEventChannel.SLASH_SPAM}> channel instead.',
                                                 None, DiscordFlags.HIDDEN)


def process_command(command_body) -> InteractionResponse:
    incoming_guild_id = int(command_body['guild_id'])
    for guild_commands in guilds_command_list:
        if guild_commands.guild_id == incoming_guild_id:
            ovo_command, guild_slash_command = find_command(command_body['data']['name'], guild_commands)
            return process_guild_command(command_body, guild_slash_command, ovo_command)
        else:
            return InteractionResponse(InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE, forbidden_response)


def process_guild_command(command_body, guild_slash_command: GuildSlashCommand, ovo_command: OvOSlashCommand)\
        -> InteractionResponse:
    """"Will perform the command if it is allowed to be executed based on channel and roles"""
    if check_if_allowed_role(command_body['member']['roles'], guild_slash_command):
        if check_if_correct_channel(command_body['channel_id'], guild_slash_command):
            return process_actual_command(command_body, ovo_command)
        else:
            return InteractionResponse(InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE, wrong_channel_response)
    else:
        return InteractionResponse(InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE, forbidden_response)


def process_actual_command(command_body, ovo_command: OvOSlashCommand):
    # todo this could probably be done generically? Like we can just add a 'command executor' with a base function.
    if ovo_command is ovo_command.SEARCH_BASE_ID:
        return process_search_base(command_body)
    else:
        return InteractionResponse(InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE, forbidden_response)


def process_search_base(command_body) -> InteractionResponse:
    search_arg = command_body['data']['options'][0]['value']
    base_result = find_bases(base_list, search_arg)
    return create_base_response(base_result, search_arg)


#  todo maybe throw an error if the command is not in the guild
def find_command(incoming_command: str, guild_command_list: GuildSlashCommands) -> {OvOSlashCommand, GuildSlashCommand}:
    try:
        ovo_slash_command = retrieve_command(incoming_command)
        for guild_command in guild_command_list.guild_commands:
            if guild_command.command.name == ovo_slash_command:
                return ovo_slash_command, guild_command
    except CommandException:
        pass


def retrieve_command(incoming_command: str) -> OvOSlashCommand:
    for ovo_slash_command in OvOSlashCommand.__members__.values():
        if ovo_slash_command.value == incoming_command:
            return ovo_slash_command
    raise CommandException(CommandExceptionMessage.GuildCommandNotFound)