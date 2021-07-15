from gecore.ps_discord_slash.commands.command_interface import InteractionCommand
from gecore.ps_discord_slash.exception.exceptions import CommandExceptionMessage, CommandException


class AvailableCommands:
    command_list = [InteractionCommand]

    def __init__(self, command_list: [InteractionCommand]):
        """"Creates the command list to make your own created commands available to be recognised and used"""
        verify_if_command_instances(command_list)
        self.command_list = command_list

    def add_command(self, command: InteractionCommand):
        """
        Adds any command to the pool to be available to be recognised and used.
        Mainly used to add the CommandManager Command afterwards.
        """
        verify_if_command_instance(command)
        self.command_list.append(command)

    def retrieve_command(self, incoming_command: str) -> InteractionCommand:
        for slash_command in self.command_list:
            if slash_command.identify().value == incoming_command:
                return slash_command
        raise CommandException(CommandExceptionMessage.CommandNotFound)

    def retrieve_component_command(self, incoming_custom_id: str) -> InteractionCommand:
        split_id = split_custom_id(incoming_custom_id)
        for slash_command in self.command_list:
            if slash_command.supports_components():
                if slash_command.component_identify().value == split_id:
                    return slash_command
        raise CommandException(CommandExceptionMessage.CommandNotFound)


def split_custom_id(incoming_custom_id: str):
    split_id = incoming_custom_id.split('|')
    return split_id[0]


def verify_if_command_instances(commands: [InteractionCommand]):
    for command in commands:
        if not isinstance(command, InteractionCommand):
            raise CommandException(CommandExceptionMessage.CommandNotInstanced)


def verify_if_command_instance(command: InteractionCommand):
    if not isinstance(command, InteractionCommand):
        raise CommandException(CommandExceptionMessage.CommandNotInstanced)
