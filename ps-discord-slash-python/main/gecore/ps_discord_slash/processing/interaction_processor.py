import logging

from gecore.ps_discord_slash.commands.command_interface import InteractionCommand, IGlobalInteractionCommand
from gecore.ps_discord_slash.commands.models.available_commands import AvailableCommands
from gecore.ps_discord_slash.commands.models.local_commands import CommandSearchResult
from gecore.ps_discord_slash.exception.exceptions import CommandException, CommandExceptionMessage
from gecore.ps_discord_slash.models.default_interaction_responses import command_error_response, \
    forbidden_dm_response
from gecore.ps_discord_slash.models.interactions import InteractionResponse, InteractionResponseType, InteractionType
from gecore.ps_discord_slash.processing.command_searcher import check_for_guild_and_command, check_for_command_in_global
from gecore.ps_discord_slash.processing.perm_checker import check_if_permitted

available_commands_attr = 'available_commands'


class InteractionProcessor:
    available_commands: AvailableCommands

    def add_commands(self, available_commands: AvailableCommands):
        self.available_commands = available_commands

    def add_command(self, command: InteractionCommand):
        self.available_commands.add_command(command)

    def process_command_request(self, command_body: {}) -> InteractionResponse:
        """Tries to find the command and sends it off to check if it can be executed."""
        try:
            interaction_type = command_body['type']
            if interaction_type is InteractionType.APPLICATION_COMMAND:
                incoming_command = command_body['data']['name']
                interaction_command = self.available_commands.retrieve_command(incoming_command)
                return segment_and_execute(command_body, interaction_command)
            elif interaction_type is InteractionType.MESSAGE_COMPONENT:
                incoming_custom_id = command_body['data']['custom_id']
                interaction_command = self.available_commands.retrieve_component_command(incoming_custom_id)
                return segment_and_execute(command_body, interaction_command)
        except CommandException as err:
            if err is CommandExceptionMessage.CommandNotFound:
                logging.error(f'{err.message}: {command_body}')
            return InteractionResponse(
                InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE, command_error_response(err.message)
            )


def segment_and_execute(command_body: {}, interaction_command: InteractionCommand) -> InteractionResponse:
    """

    """
    # todo check if we can refactor both perm lower checks into an abstracted method again.
    if 'guild_id' in command_body:
        incoming_guild_id = int(command_body['guild_id'])
        command_search_result = check_for_guild_and_command(interaction_command, incoming_guild_id)
        return execute_if_permitted(command_body, interaction_command, command_search_result)
    else:
        if isinstance(interaction_command, IGlobalInteractionCommand):
            if not interaction_command.allow_dm_usage():
                return InteractionResponse(InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE, forbidden_dm_response())
        command_search_result = check_for_command_in_global(interaction_command)
        return execute_if_permitted(command_body, interaction_command, command_search_result)


def execute_if_permitted(command_body: {}, interaction_command: InteractionCommand,
                         command_search_result: CommandSearchResult) -> InteractionResponse:
    if command_search_result.has_been_found:
        guild_command = command_search_result.found_command
        permission_check_result = check_if_permitted(command_body, guild_command)
        if permission_check_result.approved:
            if permission_check_result.has_set_perms:
                return perform_execution(command_body, interaction_command)
            else:
                if interaction_command.starting_perms().EVERYONE:
                    return perform_execution(command_body, interaction_command)
        else:
            return InteractionResponse(
                InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE, permission_check_result.error_response
            )
    else:
        return InteractionResponse(
            InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
            command_error_response(command_search_result.error_response.message)
        )


def perform_execution(command_body: {}, interaction_command: InteractionCommand) -> InteractionResponse:
    """"Executes a interaction command. Splits between slash commands and components"""
    interaction_type = command_body['type']
    if interaction_type is InteractionType.APPLICATION_COMMAND:
        return interaction_command.execute(command_body)
    elif interaction_type is InteractionType.MESSAGE_COMPONENT:
        return interaction_command.execute_component(command_body)
