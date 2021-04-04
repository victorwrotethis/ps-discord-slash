from enum import Enum

from gecore.ps_discord_slash.models.commands import ApplicationCommand
from gecore.ps_discord_slash.models.interactions import InteractionResponse


class SlashCommandName(Enum):

    @staticmethod
    def provide_members():
        pass


class ISlashCommand:

    @staticmethod
    def identify() -> SlashCommandName:
        """Returns the SlashCommand Enum variant tied to a specific command"""
        pass

    @staticmethod
    def build(command_id: int, guild_id: int, version: int) -> ApplicationCommand:
        """Builds an existing command"""
        pass

    @staticmethod
    def execute(command_body: {}) -> InteractionResponse:
        """Executes the tied command"""
        pass
