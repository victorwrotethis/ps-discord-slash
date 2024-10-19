from gecore.ps_discord_slash.commands.command_interface import IGlobalInteractionCommand, InteractionCommandType, StartingPerms
from gecore.ps_discord_slash.implementations.bases.models.base_response import create_base_embeds
from gecore.ps_discord_slash.implementations.created_commands import OvOInteractionCommand
from gecore.ps_discord_slash.models.commands import ApplicationCommand, ApplicationCommandOption, \
    ApplicationCommandOptionType
from gecore.ps_discord_slash.implementations.discord_config import GenericConfig
from gecore.ps_discord_slash.models.flags import DiscordFlags
from gecore.ps_discord_slash.models.interactions import InteractionResponse, Embed, InteractionResponseData, \
    InteractionResponseType


class GlobalPublicTestCommand(IGlobalInteractionCommand):

    @staticmethod
    def command_type() -> InteractionCommandType:
        return InteractionCommandType.GLOBAL

    @staticmethod
    def identify() -> OvOInteractionCommand:
        return OvOInteractionCommand.TEST_GLOBAL

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
            name=OvOInteractionCommand.RESERVATION,
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
