from gecore.ps_discord_slash.commands.command_interface import IGlobalInteractionCommand, InteractionCommandType, StartingPerms
from gecore.ps_discord_slash.commands.command_name_interface import InteractionCommandName
from gecore.ps_discord_slash.configuration.config_constants import ConfigConstants
from gecore.ps_discord_slash.implementations.pretty_time.test_date_processing import process_datepicker_entry, \
    kickstart_datepicker, process_date_picked
from gecore.ps_discord_slash.models.commands import ApplicationCommand, ApplicationCommandOption, \
    ApplicationCommandOptionType
from gecore.ps_discord_slash.models.interactions import InteractionResponse


class RollCallCommand(InteractionCommandName):
    ROLL_CALL = 'roll_call'
    COMPONENTS = 't_d'


def find_abbreviated_manage_command(incoming_name: str) -> RollCallCommand:
    for enum in RollCallCommand:
        if enum.value == incoming_name:
            return enum


class RollCallInteractionCommand(IGlobalInteractionCommand):

    @staticmethod
    def allow_dm_usage() -> bool:
        return False

    @staticmethod
    def supports_components() -> bool:
        return True

    @staticmethod
    def component_identify() -> InteractionCommandName:
        return RollCallCommand.COMPONENTS

    @staticmethod
    def command_type() -> InteractionCommandType:
        return InteractionCommandType.GUILD

    @staticmethod
    def identify() -> InteractionCommandName:
        return RollCallCommand.ROLL_CALL

    @staticmethod
    def starting_perms() -> StartingPerms:
        return StartingPerms.EVERYONE

    @staticmethod
    def build(guild_id: int = None) -> ApplicationCommand:
        return ApplicationCommand(
            app_id=str(ConfigConstants.discord_app_id),
            name=RollCallCommand.ROLL_CALL,
            description='Give me the starting time',
            guild_id=guild_id,
            options=[
                ApplicationCommandOption(
                    a_type=ApplicationCommandOptionType.NUMBER,
                    name='hour',
                    description='Starting hour in UTC',
                    required=True
                ),
                ApplicationCommandOption(
                    a_type=ApplicationCommandOptionType.NUMBER,
                    name='minutes',
                    description='Starting minutes, use 0 if none',
                    required=True
                )
            ]
        )

    def execute(self, command_body: {}) -> InteractionResponse:
        print(command_body)
        return kickstart_datepicker(command_id=RollCallCommand.COMPONENTS.value)

    def execute_component(self, command_body: {}) -> InteractionResponse:
        return process_datepicker_entry(
            command_id=RollCallCommand.COMPONENTS.value,
            command_body=command_body,
            picked_date_function=process_date_picked
        )

# Create row of 5 buttons with 4 hours + 1 absence
# Then on reply update the message to include a person at a time?