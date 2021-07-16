from gecore.ps_discord_slash.commands.command_manager.manage_commands import find_management_command, ManageCommands, \
    ManageCommandAbbreviations
from gecore.ps_discord_slash.exception.exceptions import CommandException, CommandExceptionMessage


class ButtonSupportContent:

    def __init__(self, custom_id: str, content: str):
        self.custom_id = custom_id
        self.content = content


def create_button_support_content(command_body: {}) -> ButtonSupportContent:
    command_data = command_body['data']
    sub_command_data = command_data['options'][0]
    management_command = find_management_command(sub_command_data['name'])
    if management_command is ManageCommands.APPROVED_USER:
        return process_generic_addition(sub_command_data, ManageCommandAbbreviations.APPROVED_USER)
    elif management_command is ManageCommands.APPROVED_CHANNEL:
        return process_generic_addition(sub_command_data, ManageCommandAbbreviations.APPROVED_CHANNEL)
    elif management_command is ManageCommands.APPROVED_ROLE:
        return process_generic_addition(sub_command_data, ManageCommandAbbreviations.APPROVED_ROLE)


def process_generic_addition(sub_command_data: {}, command_type: ManageCommandAbbreviations) -> ButtonSupportContent:
    sub_command_data_options = sub_command_data['options']
    if is_duplicate_id(sub_command_data_options):
        raise CommandException(CommandExceptionMessage.DuplicateId)
    return process_multi_option_array(sub_command_data_options, command_type)


default_start = 'You to wish to'
default_end = 'from the permitted list to execute a command.'
default_pick_commands = 'Pick which commands you want to apply this to:'


def process_multi_option_array(sub_command_data_options: {}, command_type: ManageCommandAbbreviations) -> \
        ButtonSupportContent:
    custom_id = f'{command_type.value}'
    custom_message = f'{default_start}'
    option_count = 0
    for add_or_remove in sub_command_data_options:
        option_count = option_count + 1
        option_name = find_management_command(add_or_remove['name'])
        supplied_id = add_or_remove['value']
        custom_id = f'{custom_id}|{option_name.value}|{supplied_id}'
        if option_count > 1:
            custom_message = f'{custom_message} and'
        mention_prefix = grab_mention_prefix(command_type)
        mention_type = grab_mention_type(command_type)
        custom_message = f'{custom_message} {option_name.value} the {mention_type} <{mention_prefix}{supplied_id}>'
    custom_message = f'{custom_message} {default_end} {default_pick_commands}'
    return ButtonSupportContent(custom_id, custom_message)


def grab_mention_type(command: ManageCommandAbbreviations) -> str:
    if command is ManageCommandAbbreviations.APPROVED_USER:
        return 'user'
    if command is ManageCommandAbbreviations.APPROVED_CHANNEL:
        return 'channel'
    if command is ManageCommandAbbreviations.APPROVED_ROLE:
        return 'role'


def grab_mention_prefix(command: ManageCommandAbbreviations) -> str:
    if command is ManageCommandAbbreviations.APPROVED_USER:
        return '@'
    if command is ManageCommandAbbreviations.APPROVED_CHANNEL:
        return '#'
    if command is ManageCommandAbbreviations.APPROVED_ROLE:
        return '@&'


def is_duplicate_id(sub_command_data_options: {}) -> bool:
    """"Checks if the supplied arguments are the same or not"""
    id_list = []
    for add_or_remove in sub_command_data_options:
        id_list.append(add_or_remove['value'])
    return len(id_list) > len(set(id_list))
