from gecore.ps_discord_slash.commands.command_interface import ISlashCommand
from gecore.ps_discord_slash.exception.exceptions import CommandExceptionMessage, CommandException


class AvailableCommands:
    command_list = [ISlashCommand]

    def __init__(self, command_list: [ISlashCommand]):
        """"Creates the command list to make your own created commands available to be recognised and used"""
        verify_if_command_instances(command_list)
        self.command_list = command_list

    def add_command(self, command: ISlashCommand):
        """
        Adds any command to the pool to be available to be recognised and used.
        Mainly used to add the CommandManager Command afterwards.
        """
        verify_if_command_instance(command)
        self.command_list.append(command)

    def retrieve_command(self, incoming_command: str) -> ISlashCommand:
        for slash_command in self.command_list:
            if slash_command.identify().value == incoming_command:
                return slash_command
        raise CommandException(CommandExceptionMessage.CommandNotFound)


def verify_if_command_instances(commands: [ISlashCommand]):
    for command in commands:
        if not isinstance(command, ISlashCommand):
            raise CommandException(CommandExceptionMessage.CommandNotInstanced)


def verify_if_command_instance(command: ISlashCommand):
    if not isinstance(command, ISlashCommand):
        raise CommandException(CommandExceptionMessage.CommandNotInstanced)
