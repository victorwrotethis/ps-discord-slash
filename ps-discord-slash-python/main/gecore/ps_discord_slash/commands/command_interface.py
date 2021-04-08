from gecore.ps_discord_slash.models.commands import ApplicationCommand
from gecore.ps_discord_slash.commands.command_name_interface import SlashCommandName
from gecore.ps_discord_slash.models.interactions import InteractionResponse


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
