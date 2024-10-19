from gecore.ps_discord_slash.commands.command_interface import InteractionCommand, InteractionCommandType, StartingPerms
from gecore.ps_discord_slash.implementations.created_commands import OvOInteractionCommand
from gecore.ps_discord_slash.models.commands import ApplicationCommand, ApplicationCommandOption, \
    ApplicationCommandOptionType
from gecore.ps_discord_slash.implementations.discord_config import GenericConfig


class ReservationSlashCommand(InteractionCommand):

    @staticmethod
    def command_type() -> InteractionCommandType:
        return InteractionCommandType.GUILD

    @staticmethod
    def identify() -> OvOInteractionCommand:
        return OvOInteractionCommand.RESERVATION

    @staticmethod
    def starting_perms() -> StartingPerms:
        return StartingPerms.ADMINISTRATOR_ONLY

    @staticmethod
    def build(guild_id: int = None) -> ApplicationCommand:
        return ApplicationCommand(
            app_id=str(GenericConfig.APP_ID),
            name=OvOInteractionCommand.RESERVATION,
            description='Reserve a base [v2]',
            guild_id=guild_id,
            options=[ApplicationCommandOption(
                a_type=ApplicationCommandOptionType.STRING,
                name='ByName',
                description='Put in a name to return matching bases and their ids',
                required=True
            )]
        )
