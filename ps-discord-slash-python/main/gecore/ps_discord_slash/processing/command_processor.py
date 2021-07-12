import logging

from gecore.ps_discord_slash.commands.command_interface import ISlashCommand, IGlobalSlashCommand
from gecore.ps_discord_slash.commands.models.available_commands import AvailableCommands
from gecore.ps_discord_slash.exception.exceptions import CommandException, CommandExceptionMessage
from gecore.ps_discord_slash.models.default_interaction_responses import command_error_response, \
    not_configured_response, forbidden_dm_response
from gecore.ps_discord_slash.models.interactions import InteractionResponse, InteractionResponseType
from gecore.ps_discord_slash.processing.command_searcher import check_for_guild_and_command, check_for_command_in_global
from gecore.ps_discord_slash.processing.perm_checker import check_if_permitted

available_commands_attr = 'available_commands'


class CommandProcessor:
    available_commands: AvailableCommands

    def add_commands(self, available_commands: AvailableCommands):
        self.available_commands = available_commands

    def add_command(self, command: ISlashCommand):
        self.available_commands.add_command(command)

    def process_command_request(self, command_body: {}) -> InteractionResponse:
        """Tries to find the command and sends it off to check if it can be executed."""
        incoming_command = command_body['data']['name']
        try:
            slash_command = self.available_commands.retrieve_command(incoming_command)
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
        if isinstance(slash_command, IGlobalSlashCommand):
            if not slash_command.allow_dm_usage():
                return InteractionResponse(InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE, forbidden_dm_response())
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
