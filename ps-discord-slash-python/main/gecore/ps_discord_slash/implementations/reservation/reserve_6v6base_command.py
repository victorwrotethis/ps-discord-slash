from gecore.ps_discord_slash.commands.command_interface import InteractionCommand, InteractionCommandType, StartingPerms
from gecore.ps_discord_slash.implementations.created_commands import OvOInteractionCommand
from gecore.ps_discord_slash.implementations.reservation.pools.scrim_6v6 import scrim_6v6_bases
from gecore.ps_discord_slash.tools.time.pick_time import provide_months
from gecore.ps_discord_slash.tools.time.time_variants import TimeZoneVariant, TimeVariant
from gecore.ps_discord_slash.models.commands import ApplicationCommand, ApplicationCommandOption, \
    ApplicationCommandOptionType
from gecore.ps_discord_slash.models.discord_config import GenericConfig


class Reserve6v6BaseSlashCommand(InteractionCommand):

    @staticmethod
    def command_type() -> InteractionCommandType:
        return InteractionCommandType.GUILD

    @staticmethod
    def identify() -> OvOInteractionCommand:
        return OvOInteractionCommand.RESERVE_6V6

    @staticmethod
    def starting_perms() -> StartingPerms:
        return StartingPerms.ADMINISTRATOR_ONLY

    @staticmethod
    def build(guild_id: int = None) -> ApplicationCommand:
        return ApplicationCommand(
            app_id=str(GenericConfig.APP_ID),
            name=OvOInteractionCommand.RESERVE,
            description='Reserve a 6v6 base',
            guild_id=guild_id,
            options=[
                ApplicationCommandOption(
                    a_type=ApplicationCommandOptionType.SUB_COMMAND,
                    name=OvOInteractionCommand.RESERVE_6V6.value,
                    description='Pick a start time and to use for 1 hour',
                    options=[
                        scrim_6v6_bases(),
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
                            a_type=ApplicationCommandOptionType.STRING,
                            name='timeofday',
                            description='Only use when using a 1-12 time',
                            choices=[
                                {'name': TimeVariant.AM.value, 'value': TimeVariant.AM.value},
                                {'name': TimeVariant.PM.value, 'value': TimeVariant.PM.value}
                            ]
                        )
                    ]
                )
            ]
        )
