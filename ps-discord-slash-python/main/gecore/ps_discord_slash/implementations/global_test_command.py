from gecore.ps_discord_slash.commands.command_interface import IGlobalSlashCommand, SlashCommandType, StartingPerms
from gecore.ps_discord_slash.implementations.bases.models.base_response import create_base_embeds
from gecore.ps_discord_slash.implementations.created_commands import OvOSlashCommand
from gecore.ps_discord_slash.models.commands import ApplicationCommand, ApplicationCommandOption, \
    ApplicationCommandOptionType
from gecore.ps_discord_slash.models.discord_config import GenericConfig
from gecore.ps_discord_slash.models.flags import DiscordFlags
from gecore.ps_discord_slash.models.interactions import InteractionResponse, Embed, InteractionResponseData, \
    InteractionResponseType


class GlobalPublicTestCommand(IGlobalSlashCommand):

    @staticmethod
    def command_type() -> SlashCommandType:
        return SlashCommandType.GLOBAL

    @staticmethod
    def identify() -> OvOSlashCommand:
        return OvOSlashCommand.TEST_GLOBAL

    @staticmethod
    def starting_perms() -> StartingPerms:
        return StartingPerms.EVERYONE

    @staticmethod
    def allow_dm_usage() -> bool:
        return True

    @staticmethod
    def build(guild_id: int = None) -> ApplicationCommand:
        return ApplicationCommand(
            app_id=str(GenericConfig.APP_ID),
            name=OvOSlashCommand.RESERVATION,
            description='Test this global command',
            guild_id=guild_id,
            options=[ApplicationCommandOption(
                a_type=ApplicationCommandOptionType.STRING,
                name='RightNow',
                description='Just give any input',
                required=True
            )]
        )

    def execute(self, command_body: {}) -> InteractionResponse:
        text_input = command_body['data']['options'][0]['value']
        data = InteractionResponseData(
            content=f'Your input: {text_input}',
            flags=DiscordFlags.NONE
        )
        return InteractionResponse(InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE, data)
