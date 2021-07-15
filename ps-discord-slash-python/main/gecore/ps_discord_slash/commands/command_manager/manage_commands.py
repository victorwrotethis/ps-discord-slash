from enum import Enum

from gecore.ps_discord_slash.commands.command_name_interface import InteractionCommandName
from gecore.ps_discord_slash.models.commands import ApplicationCommand, ApplicationCommandSubmission


class ManageCommands(InteractionCommandName):
    COMMAND_MANAGER = 'command_manager'
    GUILD_COMMAND = 'guild_command'
    DEFAULT_CHANNEL = 'default_channel'
    APPROVED_CHANNEL = 'approved_channel'
    APPROVED_USER = 'approved_user'
    APPROVED_ROLE = 'approved_role'
    ACTION = 'action'
    ADD = 'add'
    REMOVE = 'remove'
    SET = 'set'
    LIST = 'list'


class ManageCommandAbbreviations(InteractionCommandName):
    COMMAND_MANAGER = 'c_m'
    GUILD_COMMAND = 'g_c'
    DEFAULT_CHANNEL = 'd_c'
    APPROVED_CHANNEL = 'a_c'
    APPROVED_USER = 'a_u'
    APPROVED_ROLE = 'a_r'


def find_management_command(incoming_name: str) -> ManageCommands:
    for enum in ManageCommands:
        if enum.value == incoming_name:
            return enum


def find_abbreviated_manage_command(incoming_name: str) -> ManageCommandAbbreviations:
    for enum in ManageCommandAbbreviations:
        if enum.value == incoming_name:
            return enum


def find_abbreviated_manage_command_variant(management_command: ManageCommands) -> ManageCommandAbbreviations:
    """Returns the abbreviated version of the management command"""
    for enum in ManageCommandAbbreviations:
        if enum.name == management_command.name:
            return enum


def create_command_submission(command: ApplicationCommand):
    return ApplicationCommandSubmission(
        name=command.name,
        description=command.description,
        options=command.options
    )
