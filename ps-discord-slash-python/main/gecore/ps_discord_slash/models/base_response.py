from gecore.ps_discord_slash.models.flags import DiscordFlags
from gecore.ps_discord_slash.models.interactions import InteractionResponseData, InteractionResponse, \
    InteractionResponseType, Embed, EmbedField

message_content = 'I found the following bases for'


def create_base_response(base_list, search_arg) -> InteractionResponse:
    base_embeds = Embed('Bases', create_base_embeds(base_list))
    data = InteractionResponseData(f'{message_content}: {search_arg}', [base_embeds], DiscordFlags.NONE)
    return InteractionResponse(InteractionResponseType.ACKNOWLEDGE_WITH_SOURCE, data)


def create_base_embeds(base_list):
    base_embeds = []
    for name, base_id in base_list.items():
        base_embeds.append(EmbedField(name, base_id))
    return base_embeds
