from gecore.ps_discord_slash.bases.parse_bases import load_bases
from gecore.ps_discord_slash.bases.search_bases import find_bases
from gecore.ps_discord_slash.models.base_response import create_base_response
from gecore.ps_discord_slash.models.discord_config import JaegerEventChannel
from gecore.ps_discord_slash.models.flags import DiscordFlags
from gecore.ps_discord_slash.models.interactions import InteractionResponseType, InteractionResponse, \
    InteractionResponseData
from gecore.ps_discord_slash.processing.role_checker import check_if_allowed_role, check_if_correct_channel

base_list = load_bases()
empty_response = InteractionResponseData(None, None, DiscordFlags.NONE)
forbidden_response = InteractionResponseData('You are not allowed to use this command', None, DiscordFlags.HIDDEN)
wrong_channel_response = InteractionResponseData(f'Please use the <#{JaegerEventChannel.SLASH_SPAM}>',
                                                 None, DiscordFlags.HIDDEN)


def process_command(command_body) -> InteractionResponse:
    member_roles = command_body['member']['roles']
    if check_if_allowed_role(member_roles):
        if check_if_correct_channel(command_body['channel_id']):
            search_base = command_body['data']['name'] == 'searchbaseid'
            if search_base:
                search_arg = command_body['data']['options'][0]['value']
                base_result = find_bases(base_list, search_arg)
                return create_base_response(base_result, search_arg)
            else:
                return InteractionResponse(InteractionResponseType.ACKNOWLEDGE, empty_response)
        else:
            return InteractionResponse(InteractionResponseType.CHANNEL_MESSAGE, wrong_channel_response)
    else:
        return InteractionResponse(InteractionResponseType.CHANNEL_MESSAGE, forbidden_response)
