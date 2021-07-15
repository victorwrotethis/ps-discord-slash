from typing import List

from gecore.ps_discord_slash.models.flags import DiscordFlags


# https://discord.com/developers/docs/interactions/slash-commands#interaction-object-interaction-request-type
class InteractionType:
    PING = 1
    APPLICATION_COMMAND = 2
    MESSAGE_COMPONENT = 3


# https://discord.com/developers/docs/interactions/slash-commands#interaction-response-object-interaction-callback-type
class InteractionResponseType:
    PONG = 1
    ACKNOWLEDGE = 2  # Deprecated
    CHANNEL_MESSAGE = 3  # Deprecated
    CHANNEL_MESSAGE_WITH_SOURCE = 4
    DEFERRED_CHANNEL_MESSAGE_WITH_SOURCE = 5
    DEFERRED_UPDATE_MESSAGE = 6
    UPDATE_MESSAGE = 7


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
        self.options = kwargs.get('options', List[ApplicationCommandInteractionDataOption])


# https://discord.com/developers/docs/interactions/slash-commands#interaction
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
    def __init__(self, content, flags: DiscordFlags, embeds: [] = None, components: [] = None):
        self.tts = False
        self.content = content
        self.flags = flags
        self.embeds = embeds
        self.allowed_mentions = []
        self.components = components

    def __getstate__(self):
        """"Checks if choices or options are filled in, otherwise omits them for JsonPickle"""
        state = self.__dict__.copy()
        if not state['embeds']:
            del state['embeds']
        if not state['components']:
            del state['components']
        return state


# https://discord.com/developers/docs/interactions/slash-commands#interaction-response
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
