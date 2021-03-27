from enum import IntEnum
from typing import List


class ApplicationCommandOptionType(IntEnum):
    """"reflects: https://discord.com/developers/docs/interactions/slash-commands#applicationcommandoptiontype"""
    SUB_COMMAND = 1
    SUB_COMMAND_GROUP = 2
    STRING = 3
    INTEGER = 4
    BOOLEAN = 5
    USER = 6
    CHANNEL = 7
    ROLE = 8

    def __getstate__(self):
        """Allows JsonPickle just to retrieve the value"""
        return self.value


class ApplicationCommandOptionChoice:
    """"
    Create a new ApplicationCommandOptionChoice. Value can be a string or int
    reflects: https://discord.com/developers/docs/interactions/slash-commands#applicationcommandoptionchoice
    """

    def __init__(self, name: str, value):
        self.name = name
        self.value = value

    def __getstate__(self):
        return self.name, self.value


class ApplicationCommandOption:
    """
    Creates new Discord ApplicationCommandOption option. A maximum of 10 choices is allowed.
    It is recommended making the name camelcase for clarity, even though Discord will lowercase it.
    reflects: https://discord.com/developers/docs/interactions/slash-commands#applicationcommandoption
    """

    def __init__(self, a_type: ApplicationCommandOptionType, name: str, description: str, **kwargs):
        self.type = a_type
        self.name = name
        self.description = description
        self.default = kwargs.get('default', None)
        self.required = kwargs.get('required', None)
        self.choices = kwargs.get('choices', [])
        self.options = kwargs.get('options', [])

    def __getstate__(self):
        """"Checks if choices or options are filled in, otherwise omits them for JsonPickle"""
        state = self.__dict__.copy()
        if not state['default']:
            del state['default']
        if not state['required']:
            del state['required']
        if not state['choices']:
            del state['choices']
        if not state['options']:
            del state['options']
        return state


class ApplicationCommandSubmission:
    """
    Creates a new Discord ApplicationCommandSubmission to be sent to the api.
    Can contain nested ApplicationCommandOption.
    reflects:
        https://discord.com/developers/docs/interactions/slash-commands#create-global-application-command
        https://discord.com/developers/docs/interactions/slash-commands#create-guild-application-command
    """

    def __init__(self, name: str, description: str, options: List[ApplicationCommandOption]):
        self.name = name
        self.description = description
        self.options = options


class ApplicationCommand:
    """
    Resulting application command response from Discord API upon creating command.
    It is recommended making the name camelcase for clarity, even though Discord will lowercase it.
    reflects: https://discord.com/developers/docs/interactions/slash-commands#applicationcommand
    """

    def __init__(self, command_id: str, app_id: str, name: str, description: str,
                 version: int, guild_id: int, options: List[ApplicationCommandOption]):
        self.id = command_id
        self.application_id = app_id
        self.name = name
        self.description = description
        self.version = version
        self.guild_id = guild_id
        self.options = options
