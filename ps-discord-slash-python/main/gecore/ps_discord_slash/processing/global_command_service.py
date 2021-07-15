from gecore.ps_discord_slash.commands.command_interface import InteractionCommand
from gecore.ps_discord_slash.commands.models.local_commands import SlashCommand
from gecore.ps_discord_slash.exception.exceptions import CommandException, CommandExceptionMessage
from gecore.ps_discord_slash.implementations.global_command_list_manager import GlobalCommandManager

global_command_manager = GlobalCommandManager()


def find_global_command(slash_command: InteractionCommand) -> SlashCommand:
    if global_command_manager.global_command_list:
        global_command_manager.load_global_list()
    for global_command in global_command_manager.global_command_list.commands:
        if global_command.command.name is slash_command.identify():
            return global_command
    raise CommandException(CommandExceptionMessage.CommandNotFound)
# Todo add case of having a global command referenced that's not actually in the code?
