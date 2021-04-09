from enum import Enum

from gecore.ps_discord_slash.commands.command_name_interface import SlashCommandName
from gecore.ps_discord_slash.models.commands import ApplicationCommand, ApplicationCommandSubmission


def create_command_submission(command: ApplicationCommand):
    return ApplicationCommandSubmission(
        name=command.name,
        description=command.description,
        options=command.options
    )


class OvOSlashCommand(SlashCommandName):
    SEARCH_BASE_ID = 'searchbaseid'
    REQUEST_ACCOUNTS = 'requestaccounts'
    REQUEST_ACCOUNT = 'requestaccount'
    RESERVATION = 'reservation'

    @staticmethod
    def provide_members():
        return OvOSlashCommand.__members__.values()
