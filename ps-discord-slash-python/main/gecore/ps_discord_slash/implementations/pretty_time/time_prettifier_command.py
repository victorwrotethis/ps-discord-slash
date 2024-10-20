from gecore.ps_discord_slash.commands.command_interface import IGlobalInteractionCommand, InteractionCommandType, StartingPerms
from gecore.ps_discord_slash.commands.command_name_interface import InteractionCommandName
from gecore.ps_discord_slash.configuration.config_constants import ConfigConstants
from gecore.ps_discord_slash.implementations.pretty_time.time_request import create_time_request, PrettyTimeArgument
from gecore.ps_discord_slash.models.commands import ApplicationCommand, ApplicationCommandOption, \
    ApplicationCommandOptionType
from gecore.ps_discord_slash.models.flags import DiscordFlags
from gecore.ps_discord_slash.models.interactions import InteractionResponse, InteractionResponseData, \
    InteractionResponseType
from gecore.ps_discord_slash.tools.time.pick_time import provide_months
from gecore.ps_discord_slash.tools.time.time_converter import create_utc_timestamp
from gecore.ps_discord_slash.tools.time.time_variants import TimeZoneVariant, TimeVariant


class PrettyTimeCommand(InteractionCommandName):
    PrettyTime = 'pretty_time'


class PrettyTimeInteractionCommand(IGlobalInteractionCommand):

    @staticmethod
    def allow_dm_usage() -> bool:
        return False

    @staticmethod
    def command_type() -> InteractionCommandType:
        return InteractionCommandType.GLOBAL

    @staticmethod
    def identify() -> InteractionCommandName:
        return PrettyTimeCommand.PrettyTime

    @staticmethod
    def starting_perms() -> StartingPerms:
        return StartingPerms.EVERYONE

    @staticmethod
    def build(guild_id: int = None) -> ApplicationCommand:
        return ApplicationCommand(
            app_id=str(ConfigConstants.discord_app_id),
            name=PrettyTimeCommand.PrettyTime,
            description='Helps you make pretty discord countdowns',
            guild_id=guild_id,
            options=[
                ApplicationCommandOption(
                    a_type=ApplicationCommandOptionType.STRING,
                    name='month',
                    required=True,
                    description='Pick the month',
                    choices=provide_months()
                ),
                ApplicationCommandOption(
                    a_type=ApplicationCommandOptionType.INTEGER,
                    name='day',
                    required=True,
                    description='Pick the day'
                ),
                ApplicationCommandOption(
                    a_type=ApplicationCommandOptionType.STRING,
                    name='timezone',
                    description='Pick the timezone',
                    required=True,
                    choices=[
                        {'name': TimeZoneVariant.EASTERN.value, 'value': TimeZoneVariant.EASTERN.name},
                        {'name': TimeZoneVariant.PACIFIC.value, 'value': TimeZoneVariant.PACIFIC.name},
                        {'name': TimeZoneVariant.UTC.value, 'value': TimeZoneVariant.UTC.name}
                    ]
                ),
                ApplicationCommandOption(
                    a_type=ApplicationCommandOptionType.INTEGER,
                    name='hour',
                    required=True,
                    description='Pick an hour'
                ),
                ApplicationCommandOption(
                    a_type=ApplicationCommandOptionType.INTEGER,
                    name='minutes',
                    required=False,
                    description='Pick the amount of minutes'
                ),
                ApplicationCommandOption(
                    a_type=ApplicationCommandOptionType.STRING,
                    name='timeofday',
                    description='Only use when using a 1-12 time',
                    required=False,
                    choices=[
                        {'name': TimeVariant.AM.value, 'value': TimeVariant.AM.value},
                        {'name': TimeVariant.PM.value, 'value': TimeVariant.PM.value}
                    ]
                )
            ]
        )

    def execute(self, command_body: {}) -> InteractionResponse:
        time_req = create_time_request(command_body)
        created_timestamp = create_utc_timestamp(
            hour=time_req.hour,
            day=time_req.day,
            minute=time_req.minute if hasattr(time_req, PrettyTimeArgument.MINUTES.value) else 0,
            month_variant=time_req.month,
            time_variant=time_req.time_variant if hasattr(time_req, 'time_variant') else None,
            timezone_variant=time_req.timezone_variant
        )

        data = InteractionResponseData(
            content=f'Your time is in <t:{created_timestamp}:R> when using: `<t:{created_timestamp}:R>`',
            flags=DiscordFlags.NONE
        )
        return InteractionResponse(InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE, data)



