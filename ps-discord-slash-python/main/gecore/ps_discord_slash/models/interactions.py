
# https://discord.com/developers/docs/interactions/slash-commands#interaction-interactiontype
from gecore.ps_discord_slash.models.flags import DiscordFlags


class InteractionType:
    PING = 1
    APPLICATION_COMMAND = 2


# https://discord.com/developers/docs/interactions/slash-commands#interaction-interactionresponsetype
class InteractionResponseType:
    PONG = 1
    ACKNOWLEDGE = 2
    CHANNEL_MESSAGE = 3
    CHANNEL_MESSAGE_WITH_SOURCE = 4
    ACKNOWLEDGE_WITH_SOURCE = 5


# https://discord.com/developers/docs/interactions/slash-commands#interaction-applicationcommandinteractiondataoption
class ApplicationCommandInteractionDataOption:
    def __init__(self, name: str, **kwargs):
        self.name = name
        self.value = kwargs.get('value')
        self.options = kwargs.get('options')


# https://discord.com/developers/docs/interactions/slash-commands#interaction-applicationcommandinteractiondata
class ApplicationCommandInteractionData:
    def __init__(self, a_id, name: str, **kwargs):
        self.id = a_id,
        self.name = name
        self.options = kwargs.get('options', [ApplicationCommandInteractionDataOption])


class Interaction:
    def __init__(self, i_id, i_type: InteractionType, guild_id, channel_id, member, token: str, version: int):
        self.id = i_id
        self.type = i_type
        self.guild_id = guild_id
        self.channel_id = channel_id
        self.member = member
        self.token = token
        self.version = version


# https://discord.com/developers/docs/interactions/slash-commands#interaction-interactionapplicationcommandcallbackdata
class InteractionResponseData:
    def __init__(self, content, embeds, flags: DiscordFlags):
        self.tts = False
        self.content = content
        self.flags = flags
        self.embeds = embeds
        self.allowed_mentions = []


class InteractionResponse:
    def __init__(self, response_type: InteractionResponseType, response_data: InteractionResponseData):
        self.type = response_type
        self.data = response_data


class Embed:
    def __init__(self, title, fields):
        self.title = title
        self.type = 'rich'
        self.fields = fields


class EmbedField:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.inline = False
