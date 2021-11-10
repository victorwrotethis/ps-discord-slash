from gecore.ps_discord_slash.commands.command_interface import IGlobalInteractionCommand, InteractionCommandType, StartingPerms
from gecore.ps_discord_slash.commands.command_name_interface import InteractionCommandName
from gecore.ps_discord_slash.implementations.pretty_time.test_date_processing import process_datepicker_entry, \
    kickstart_datepicker
from gecore.ps_discord_slash.models.commands import ApplicationCommand
from gecore.ps_discord_slash.models.discord_config import GenericConfig
from gecore.ps_discord_slash.models.interactions import InteractionResponse


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
        return kickstart_datepicker(command_id=TestDateCommand.TESTDATECOMPONENTS.value)

    def execute_component(self, command_body: {}) -> InteractionResponse:
        return process_datepicker_entry(
            command_id=TestDateCommand.TESTDATECOMPONENTS.value,
            command_body=command_body
        )
