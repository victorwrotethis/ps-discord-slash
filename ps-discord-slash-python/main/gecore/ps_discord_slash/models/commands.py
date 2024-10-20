from enum import IntEnum

from gecore.ps_discord_slash.commands.command_name_interface import InteractionCommandName

class ApplicationCommandType(IntEnum):
    """"reflects: https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-types"""
    CHAT_INPUT = 1
    USER = 2
    MESSAGE = 3
    PRIMARY_ENTRY_POINT = 4

class ApplicationCommandOptionType(IntEnum):
    """reflects: https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-option-type"""
    SUB_COMMAND = 1
    SUB_COMMAND_GROUP = 2
    STRING = 3
    INTEGER = 4
    BOOLEAN = 5
    USER = 6
    CHANNEL = 7
    ROLE = 8
    MENTIONABLE = 9
    NUMBER = 10
    ATTACHMENT = 11

    def __getstate__(self):
        """Allows JsonPickle just to retrieve the value"""
        return self.value


class ApplicationCommandOptionChoice:
    """"
    Create a new ApplicationCommandOptionChoice. Discord accepts values that are a string, int or double
    reflects: https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-option-choice-structure
    """

    def __init__(self, name: str, value):
        self.name = name
        self.value = value


class ApplicationCommandOption:
    """
    Creates new Discord ApplicationCommandOption option. A maximum of 25 choices is allowed.
    reflects: https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-option-structure
    """

    def __init__(self, a_type: ApplicationCommandOptionType, name: str, description: str, **kwargs):
        self.type = a_type
        self.name = name
        self.description = description
        self.default = kwargs.get('default', None)
        self.required = kwargs.get('required', None)
        self.choices = kwargs.get('choices', [])
        self.options = kwargs.get('options', [])
        self.min_value = kwargs.get('min_value', None)
        self.max_value = kwargs.get('max_value', None)
        self.autocomplete = kwargs.get('autocomplete', None)

    def __getstate__(self):
        """"Checks if choices or options are filled in, otherwise omits them for JsonPickle"""
        state = self.__dict__.copy()
        if not state['default']:
            del state['default']
        if not state['required']:
            del state['required']
        else:
            if state['required']:
                state['required'] = 'True'
            else:
                state['required'] = 'False'
        if not state['choices']:
            del state['choices']
        if not state['options']:
            del state['options']
        if not state['min_value']:
            del state['min_value']
        if not state['max_value']:
            del state['max_value']
        if not state['autocomplete']:
            del state['autocomplete']
        return state


class ApplicationCommandSubmission:
    """
    Creates a new Discord ApplicationCommandSubmission to be sent to the api.
    Can contain nested ApplicationCommandOption.
    reflects:
        https://discord.com/developers/docs/interactions/application-commands#create-global-application-command
        https://discord.com/developers/docs/interactions/application-commands#create-guild-application-command
    """

    def __init__(self, name: InteractionCommandName, description: str, options: list[ApplicationCommandOption]):
        self.name = name
        self.description = description
        self.options = options


class ApplicationCommand:
    """
    Resulting application command response from Discord API upon creating command.
    The name has to be camel case.
    reflects: https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-structure
    """

    def __init__(self, app_id: str, name: InteractionCommandName, description: str, command_id: str = None,
                 version: int = None, guild_id: int = None, command_type: ApplicationCommandType = 1 , options: list[ApplicationCommandOption] = None):
        self.id = command_id
        self.application_id = app_id
        self.name = name
        self.description = description
        self.version = version
        self.guild_id = guild_id
        self.type = command_type
        self.options = options

    def __getstate__(self):
        """"Checks if choices or options are filled in, otherwise omits them for JsonPickle"""
        state = self.__dict__.copy()
        del state['application_id']
        del state['guild_id']
        del state['version']
        del state['id']
        return state
