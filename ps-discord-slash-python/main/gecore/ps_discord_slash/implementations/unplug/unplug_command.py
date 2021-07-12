from gecore.ps_discord_slash.commands.command_interface import IGlobalSlashCommand, SlashCommandType, StartingPerms
from gecore.ps_discord_slash.commands.command_name_interface import SlashCommandName
from gecore.ps_discord_slash.models.commands import ApplicationCommand, ApplicationCommandOption, \
    ApplicationCommandOptionType
from gecore.ps_discord_slash.models.discord_config import GenericConfig
from gecore.ps_discord_slash.models.flags import DiscordFlags
from gecore.ps_discord_slash.models.interactions import InteractionResponse, InteractionResponseData, \
    InteractionResponseType


class UnplugCommand(SlashCommandName):
    UNPLUG = 'unplug'


class UnplugSlashCommand(IGlobalSlashCommand):

    @staticmethod
    def allow_dm_usage() -> bool:
        return False

    @staticmethod
    def command_type() -> SlashCommandType:
        return SlashCommandType.GLOBAL

    @staticmethod
    def identify() -> SlashCommandName:
        return UnplugCommand.UNPLUG

    @staticmethod
    def starting_perms() -> StartingPerms:
        return StartingPerms.EVERYONE

    @staticmethod
    def build(guild_id: int = None) -> ApplicationCommand:
        return ApplicationCommand(
            app_id=str(GenericConfig.APP_ID),
            name=UnplugCommand.UNPLUG,
            description='Turn off',
            options=[ApplicationCommandOption(
                a_type=ApplicationCommandOptionType.STRING,
                name='system',
                description='Put in a service to turn off',
                required=True
            )]
        )

    def execute(self, command_body: {}) -> InteractionResponse:
        data = InteractionResponseData(
            content=f'Nice try',
            flags=DiscordFlags.NONE
        )
        return InteractionResponse(InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE, data)
