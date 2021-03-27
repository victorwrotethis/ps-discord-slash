from enum import Enum

from gecore.ps_discord_slash.models.commands import ApplicationCommand, \
    ApplicationCommandOption, ApplicationCommandOptionType, ApplicationCommandSubmission
from gecore.ps_discord_slash.models.discord_config import GenericConfig


def build_search_base_id(command_id: int, guild_id: int, version: int) -> ApplicationCommand:
    return ApplicationCommand(
        command_id=str(command_id),
        app_id=str(GenericConfig.APP_ID),
        name=OvOSlashCommand.SEARCH_BASE_ID,
        description='Search a facility Id [v2]',
        version=version,
        guild_id=guild_id,
        options=[ApplicationCommandOption(
            a_type=ApplicationCommandOptionType.STRING,
            name='ByName',
            description='Put in a name to return matching bases and their ids',
            required=True
        )]
    )


def create_command_submission(command: ApplicationCommand):
    return ApplicationCommandSubmission(
        name=command.name,
        description=command.description,
        options=command.options
    )


class OvOSlashCommand(Enum):
    SEARCH_BASE_ID = 'searchbaseid'
    REQUEST_ACCOUNTS = 'requestaccounts'

    def __getstate__(self):
        """Allows JsonPickle just to retrieve the value"""
        return self
