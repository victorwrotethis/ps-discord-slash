class ApplicationCommandOptionType:
    SUB_COMMAND = 1
    SUB_COMMAND_GROUP = 2
    STRING = 3
    INTEGER = 4
    BOOLEAN = 5
    USER = 6
    CHANNEL = 7
    ROLE = 8


class ApplicationCommandOptionChoice:
    """"Create a new ApplicationCommandOptionChoice. Value can be a string or int"""
    def __init__(self, name: str, value):
        self.name = name
        self.value = value


class ApplicationCommandOption:
    """ Creates new Discord ApplicationCommandOption option. A maximum of 10 choices is allowed"""
    def __init__(self, a_type: ApplicationCommandOptionType, name: str, description: str, **kwargs):
        self.type = a_type
        self.name = name
        self.description = description
        self.default = kwargs.get('default', True)
        self.required = kwargs.get('required', False)
        self.choices = kwargs.get('choices', [ApplicationCommandOptionChoice])
        self.options = kwargs.get('options', [ApplicationCommandOption])


class ApplicationCommandSubmission:
    """ Creates a new Discord ApplicationCommandSubmission to be sent to the api. Which can have nested options."""
    def __init__(self, name: str, description: str, options: [ApplicationCommandOption]):
        self.name = name
        self.description = description
        self.options = options


class ApplicationCommand:
    """ Resulting application command response from Discord API upon creating command"""
    def __init__(self, command_id: str, app_id: str,  name: str, description: str, options: [ApplicationCommandOption]):
        self.id = command_id
        self.application_id = app_id
        self.name = name
        self.description = description
        self.options = options
