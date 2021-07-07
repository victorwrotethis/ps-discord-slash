import logging

from gecore.ps_discord_slash.commands.command_interface import ISlashCommand
from gecore.ps_discord_slash.commands.models.local_commands import SlashCommand
from gecore.ps_discord_slash.exception.exceptions import CommandException, CommandExceptionMessage
from gecore.ps_discord_slash.implementations.load_available_commands import LoadedCommands
from gecore.ps_discord_slash.models.default_interaction_responses import command_error_response, forbidden_response, \
    not_configured_response
from gecore.ps_discord_slash.models.interactions import InteractionResponse, InteractionResponseType
from gecore.ps_discord_slash.processing.command_searcher import check_for_guild_and_command, check_for_command_in_global
from gecore.ps_discord_slash.processing.perm_checker import check_if_permitted

loaded_commands = LoadedCommands()

# these must be the commands loaded in as created. Not guild related
# not entirely sure why None'd it before :thinking:
# maybe we wanted to load it in later because of the 'oh please don't break on my tests'
# Likely a bit pre-done being that it's not even connected to Dynamo yet at all


def process_command_request(command_body: {}) -> InteractionResponse:
    """Tries to find the command and sends it off to check if it can be executed."""
    incoming_command = command_body['data']['name']
    try:
        if not hasattr(loaded_commands, 'available_commands'):
            loaded_commands.load_commands()
        slash_command = loaded_commands.available_commands.retrieve_command(incoming_command)
        return segment_and_execute(command_body, slash_command)
    except CommandException as err:
        if err is CommandExceptionMessage.CommandNotFound:
            logging.error(f'{err.message}: {command_body}')
        return InteractionResponse(
            InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE, command_error_response(err.message)
        )


def segment_and_execute(command_body: {}, slash_command: ISlashCommand) -> InteractionResponse:
    """

    """
    if 'guild_id' in command_body:
        incoming_guild_id = int(command_body['guild_id'])
        command_search_result = check_for_guild_and_command(slash_command, incoming_guild_id)
        if command_search_result.has_been_found:
            guild_command = command_search_result.found_command
            permission_check_result = check_if_permitted(command_body, guild_command)
            if permission_check_result.approved:
                if permission_check_result.has_set_perms:
                    return slash_command.execute(command_body)
                else:
                    if slash_command.starting_perms().EVERYONE:
                        return slash_command.execute(command_body)
            else:
                return InteractionResponse(
                    InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE, permission_check_result.error_response
                )
        else:
            # todo sync up with not finding guild or global command
            return InteractionResponse(
                InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE, not_configured_response()
            )
    # check if error is command not found?
    # todo process as command that might have guild perms
    else:
        command_search_result = check_for_command_in_global(slash_command)
        if command_search_result.has_been_found:
            global_command = command_search_result.found_command
            permission_check_result = check_if_permitted(command_body, global_command)
            if permission_check_result.approved:
                if slash_command.starting_perms().EVERYONE:
                    return slash_command.execute(command_body)
            else:
                return InteractionResponse(
                    InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE, permission_check_result.error_response
                )
        else:
            return InteractionResponse(
                InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
                command_error_response(command_search_result.error_response.message)
            )

# todo
#   We left off at splitting into going to check if there's any permissions, if not do pass on the guild id
#   Maybe at that point it needs to go through a bare flow Being GuildSlash typed shouldn't matter at this stage.
#   So we need a flow for without stored perms at guild to -> perms at command itself.
#   If there's no perms that either means it's free for all or it in the process of being setup.
#   Guild specific commands generally aren't part of this flow as they won't be there unless someone force added them


def retrieve_command_permissions(command_body: {}, slash_command: SlashCommand):
    pass



# Currently mimics loading them from persistence
