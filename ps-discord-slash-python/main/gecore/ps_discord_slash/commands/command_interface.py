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
    GLOBAL = 1
    GUILD = 2


class StartingPerms(Enum):
    """
    Starting permissions for commands meant for when a command just got available to users.
    --Variants--
    ADMINISTRATOR_ONLY: This command can never deviate from being used only by guild administrators.
    ADMINISTRATOR: Can initially only be used by guild administrators, but it can be modified after to allow others.
    EVERYONE: Literally every user that has access to slash commands can use this command from the start.
    """
    ADMINISTRATOR_ONLY = 1
    ADMINISTRATOR = 2
    EVERYONE = 3


class ISlashCommand:
    """"Can be extended when creating normal Guild type commands"""

    @staticmethod
    def command_type() -> SlashCommandType:
        """"Returns the SlashCommand Enum type variant tied to a specific command"""

    @staticmethod
    def identify() -> SlashCommandName:
        """Returns the SlashCommand Enum name variant tied to a specific command"""
        pass

    @staticmethod
    def starting_perms() -> StartingPerms:
        """
        Returns who can use the commands when the command becomes initially available
        Only meant to be used before the Discord Slash and bigger GuildPermission system
        """
        pass

    @staticmethod
    def build(guild_id: int = None) -> ApplicationCommand:
        """Builds an existing command"""
        pass

    def execute(self, command_body: {}) -> InteractionResponse:
        """Executes the tied command"""
        pass


class IGlobalSlashCommand(ISlashCommand):
    """"Global Slash commands"""

    @staticmethod
    def allow_dm_usage() -> bool:
        """
        Signifies if this particular command is allowed in DMs
        If false, this means the command will only be accepted when used in guilds.
        Default is False
        """
        return False
