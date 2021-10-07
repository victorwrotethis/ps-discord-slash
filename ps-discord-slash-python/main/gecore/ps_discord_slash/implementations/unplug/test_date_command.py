from gecore.ps_discord_slash.commands.command_interface import IGlobalInteractionCommand, InteractionCommandType, StartingPerms
from gecore.ps_discord_slash.commands.command_name_interface import InteractionCommandName
from gecore.ps_discord_slash.implementations.unplug.create_date_buttons import create_date_components
from gecore.ps_discord_slash.models.commands import ApplicationCommand
from gecore.ps_discord_slash.models.discord_config import GenericConfig
from gecore.ps_discord_slash.models.flags import DiscordFlags
from gecore.ps_discord_slash.models.interactions import InteractionResponse, InteractionResponseData, \
    InteractionResponseType


class TestDateCommand(InteractionCommandName):
    TESTDATE = 'testdate'


class TestDateInteractionCommand(IGlobalInteractionCommand):

    @staticmethod
    def allow_dm_usage() -> bool:
        return False

    @staticmethod
    def command_type() -> InteractionCommandType:
        return InteractionCommandType.GUILD

    @staticmethod
    def identify() -> InteractionCommandName:
        return TestDateCommand.TESTDATE

    @staticmethod
    def starting_perms() -> StartingPerms:
        return StartingPerms.EVERYONE

    @staticmethod
    def build(guild_id: int = None) -> ApplicationCommand:
        return ApplicationCommand(
            app_id=str(GenericConfig.APP_ID),
            name=TestDateCommand.TESTDATE,
            description='Give me the dates',
            guild_id=guild_id
        )

    def execute(self, command_body: {}) -> InteractionResponse:
        # data = InteractionResponseData(
        #     content=f'Nice try',
        #     flags=DiscordFlags.NONE
        # )
        return create_date_components()
