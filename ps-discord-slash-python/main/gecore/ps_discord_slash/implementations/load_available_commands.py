from gecore.ps_discord_slash.commands.command_manager.command_manager_command import CommandManagerInteractionCommand
from gecore.ps_discord_slash.commands.models.available_commands import AvailableCommands
from gecore.ps_discord_slash.implementations.bases.search_base_command import SearchBaseSlashCommand
from gecore.ps_discord_slash.implementations.unplug.unplug_command import UnplugInteractionCommand
from gecore.ps_discord_slash.processing.interaction_processor import InteractionProcessor, available_commands_attr


def check_if_commands_loaded(command_processor: InteractionProcessor):
    if not hasattr(command_processor, available_commands_attr):
        load_commands(command_processor)


def load_commands(command_processor: InteractionProcessor):
    command_processor.add_commands(
        AvailableCommands(
            command_list=[SearchBaseSlashCommand(), UnplugInteractionCommand()]
        )
    )
    command_processor.add_command(CommandManagerInteractionCommand(command_processor.available_commands))
