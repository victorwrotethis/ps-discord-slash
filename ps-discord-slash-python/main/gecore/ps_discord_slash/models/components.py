from enum import Enum


class ComponentType(Enum):
    """
        Reflects: https://discord.com/developers/docs/interactions/message-components#component-object-component-types
    """
    ActionRow = 1
    Button = 2
    SelectMenu = 3
    TextInput = 4
    UserSelect = 5
    RoleSelect = 6
    MentionableSelect = 7
    ChannelSelect = 8

    def __getstate__(self):
        """Allows JsonPickle just to retrieve the value"""
        return self.value


class Component:
    def __init__(self, component_type: ComponentType, custom_id: str = None, disabled: bool = None):
        self.type = component_type
        self.custom_id = custom_id
        self.disabled = disabled

    def __getstate__(self):
        """"Checks if choices or options are filled in, otherwise omits them for JsonPickle"""
        state = self.__dict__.copy()
        if not state['custom_id']:
            del state['custom_id']
        if not state['disabled']:
            del state['disabled']
        return state


class ActionRow(Component):
    def __init__(self, component_type: ComponentType, components: [Component]):
        super().__init__(component_type)
        self.components = components


class ButtonStyle(Enum):
    """Reflects: https://discord.com/developers/docs/interactions/message-components#button-object-button-styles"""
    Primary = 1
    Secondary = 2
    Success = 3
    Danger = 4
    Link = 5
    Premium = 6

    def __getstate__(self):
        """Allows JsonPickle just to retrieve the value"""
        return self.value


class ButtonEmoji:
    def __init__(self, name: str, emoji_id: str, animated: bool = False):
        self.id: emoji_id
        self.name = name
        self.animated = animated


class Button(Component):
    def __init__(self, component_type: ComponentType, style: ButtonStyle, custom_id: str = None, label: str = None,
                 emoji: ButtonEmoji = None, url: str = None, disabled: bool = False):
        super().__init__(component_type, custom_id, disabled)
        self.style = style
        self.label = label
        self.emoji = emoji
        self.url = url

    def __getstate__(self):
        """"Checks if choices or options are filled in, otherwise omits them for JsonPickle"""
        state = self.__dict__.copy()
        if not state['label']:
            del state['label']
        if not state['emoji']:
            del state['emoji']
        if not state['url']:
            del state['url']
        return state


class SelectOption:
    def __init__(self, label: str, value: str, description: str = None,
                 emoji: ButtonEmoji = None, default: bool = False):
        self.label = label
        self.value = value
        self.description = description
        self.emoji = emoji
        self.default = default

    def __getstate__(self):
        """"Checks if choices or options are filled in, otherwise omits them for JsonPickle"""
        state = self.__dict__.copy()
        if not state['description']:
            del state['description']
        if not state['emoji']:
            del state['emoji']
        return state


class SelectMenu(Component):
    def __init__(self, component_type: ComponentType, custom_id: str, options: [SelectOption], placeholder: str = None,
                 min_values: int = 1, max_values: int = 1, disabled: bool = False):
        super().__init__(component_type, custom_id, disabled)
        self.options = options
        self.placeholder = placeholder
        self.min_values = min_values
        self.max_values = max_values

    def __getstate__(self):
        """"Checks if choices or options are filled in, otherwise omits them for JsonPickle"""
        state = self.__dict__.copy()
        if not state['placeholder']:
            del state['placeholder']
        return state
