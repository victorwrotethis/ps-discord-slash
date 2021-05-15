from gecore.ps_discord_slash.commands.command_interface import ISlashCommand, SlashCommandType, StartingPerms
from gecore.ps_discord_slash.implementations.created_commands import OvOSlashCommand
from gecore.ps_discord_slash.models.commands import ApplicationCommand, ApplicationCommandOption, \
    ApplicationCommandOptionType
from gecore.ps_discord_slash.models.discord_config import GenericConfig


class ReservationSlashCommand(ISlashCommand):

    @staticmethod
    def command_type() -> SlashCommandType:
        return SlashCommandType.GUILD

    @staticmethod
    def identify() -> OvOSlashCommand:
        return OvOSlashCommand.RESERVATION

    @staticmethod
    def starting_perms() -> StartingPerms:
        return StartingPerms.ADMINISTRATOR_ONLY

    @staticmethod
    def build(command_id: int, guild_id: int, version: int) -> ApplicationCommand:
        return ApplicationCommand(
            command_id=str(command_id),
            app_id=str(GenericConfig.APP_ID),
            name=OvOSlashCommand.RESERVATION,
            description='Search a facility Id [v2]',
            version=version,
            guild_id=guild_id,
            options=[ApplicationCommandOption(
                a_type=ApplicationCommandOptionType.STRING,
                name='ByName',
                description='Put in a name to return matching bases and their ids',
                required=True
            )]
        )
