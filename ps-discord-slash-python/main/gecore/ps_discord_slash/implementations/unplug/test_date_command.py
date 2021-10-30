import datetime

from gecore.ps_discord_slash.commands.command_interface import IGlobalInteractionCommand, InteractionCommandType, StartingPerms
from gecore.ps_discord_slash.commands.command_name_interface import InteractionCommandName
from gecore.ps_discord_slash.commands.support.date_picker_buttons.date_picker_buttons import create_date_buttons_from
from gecore.ps_discord_slash.implementations.unplug.create_date_buttons import create_date_components
from gecore.ps_discord_slash.models.commands import ApplicationCommand
from gecore.ps_discord_slash.models.discord_config import GenericConfig
from gecore.ps_discord_slash.models.flags import DiscordFlags
from gecore.ps_discord_slash.models.interactions import InteractionResponse, InteractionResponseData, \
    InteractionResponseType


class TestDateCommand(InteractionCommandName):
    TESTDATE = 'testdate'
    TESTDATECOMPONENTS = 't_d'


def find_abbreviated_manage_command(incoming_name: str) -> TestDateCommand:
    for enum in TestDateCommand:
        if enum.value == incoming_name:
            return enum


class TestDateInteractionCommand(IGlobalInteractionCommand):

    @staticmethod
    def allow_dm_usage() -> bool:
        return False

    @staticmethod
    def supports_components() -> bool:
        return True

    @staticmethod
    def component_identify() -> InteractionCommandName:
        return TestDateCommand.TESTDATECOMPONENTS

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
        print(command_body)
        action_rows = create_date_buttons_from(
            command_id=TestDateCommand.TESTDATECOMPONENTS.value,
            start_date=int(datetime.datetime.now().timestamp()),
            disable_old=True
        )
        return InteractionResponse(
            response_type=InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
            response_data=InteractionResponseData(
                content='Please pick a date',
                flags=DiscordFlags.NONE,
                components=action_rows
            )
        )

    def execute_component(self, command_body: {}) -> InteractionResponse:
        #todo depending on what we get
        # if navigation button-> we change the exiting message
        # if specific date button we ask for a confirmation.
        return InteractionResponse(
            response_type=InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
            response_data=InteractionResponseData(
                content=f'Thank you for your contribution: {command_body["data"]["custom_id"]}',
                flags=DiscordFlags.NONE
            )
        )
