from enum import Enum

from gecore.ps_discord_slash.models.commands import ApplicationCommand
from gecore.ps_discord_slash.commands.command_name_interface import SlashCommandName
from gecore.ps_discord_slash.models.interactions import InteractionResponse


class SlashCommandType(Enum):
    """"The type of command.
    Guild commands can only be used in a specific guild once added to that guild.
    Global commands can be used in any guild and direct messages.
    For more info: https://discord.com/developers/docs/interactions/slash-commands#registering-a-command
    """
    GLOBAL = 1,
    GUILD = 2


class ISlashCommand:

    @staticmethod
    def allow_dm_usage() -> bool:
        """Signifies if this particular command is allowed in DMs
        Only has an effect on Global Commands.
        If false, this means the command will only be accepted when used in guilds.
        Default is False
        """
        return False

    @staticmethod
    def command_type() -> SlashCommandType:
        """"Returns the SlashCommand Enum type variant tied to a specific command"""

    @staticmethod
    def identify() -> SlashCommandName:
        """Returns the SlashCommand Enum name variant tied to a specific command"""
        pass

    @staticmethod
    def build(command_id: int, guild_id: int, version: int) -> ApplicationCommand:
        """Builds an existing command"""
        pass

    def execute(self, command_body: {}) -> InteractionResponse:
        """Executes the tied command"""
        pass
