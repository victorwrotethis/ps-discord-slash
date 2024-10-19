from gecore.ps_discord_slash.commands.command_interface import InteractionCommand, InteractionCommandType, StartingPerms
from gecore.ps_discord_slash.implementations.bases.models.base_response import create_base_response
from gecore.ps_discord_slash.implementations.bases.parse_bases import BasesParser
from gecore.ps_discord_slash.implementations.bases.search_bases import find_bases
from gecore.ps_discord_slash.implementations.created_commands import OvOInteractionCommand
# from gecore.ps_discord_slash.implementations.bases.models.base_response import create_base_response
# from gecore.ps_discord_slash.implementations.bases.parse_bases import BasesParser
# from gecore.ps_discord_slash.implementations.bases.search_bases import find_bases
from gecore.ps_discord_slash.models.commands import ApplicationCommand, ApplicationCommandOption, \
    ApplicationCommandOptionType
from gecore.ps_discord_slash.implementations.discord_config import GenericConfig
from gecore.ps_discord_slash.models.flags import DiscordFlags
from gecore.ps_discord_slash.models.interactions import InteractionResponse, InteractionResponseData, \
    InteractionResponseType


class SearchBaseSlashCommand(InteractionCommand):

    def __init__(self):
        self.base_list = BasesParser().create_base_list()

    @staticmethod
    def starting_perms() -> StartingPerms:
        return StartingPerms.EVERYONE

    @staticmethod
    def identify() -> OvOInteractionCommand:
        return OvOInteractionCommand.SEARCH_BASE_ID

    @staticmethod
    def command_type() -> InteractionCommandType:
        return InteractionCommandType.GUILD

    @staticmethod
    def build(guild_id: int = None) -> ApplicationCommand:
        return ApplicationCommand(
            app_id=str(GenericConfig.APP_ID),
            name=OvOInteractionCommand.SEARCH_BASE_ID,
            description='Search a facility Id [v2]',
            guild_id=guild_id,
            options=[ApplicationCommandOption(
                a_type=ApplicationCommandOptionType.STRING,
                name='ByName',
                description='Put in a name to return matching bases and their ids',
                required=True
            )]
        )

    def execute(self, command_body: {}) -> InteractionResponse:
        search_arg = command_body['data']['options'][0]['value']
        base_result = find_bases(self.base_list, search_arg)
        return create_base_response(base_result, search_arg)
        # data = InteractionResponseData(
        #     content=f'Lost made me disable this :(',
        #     flags=DiscordFlags.HIDDEN
        # )
        # return InteractionResponse(InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE, data)
