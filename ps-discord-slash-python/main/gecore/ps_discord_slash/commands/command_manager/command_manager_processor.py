from gecore.ps_discord_slash.commands.models.available_commands import AvailableCommands
from gecore.ps_discord_slash.models.interactions import InteractionResponse


def process_command_manager(available_commands: AvailableCommands, command_body: {}) -> InteractionResponse:
    # todo we're returning buttons here for the specific action the person wants to execute.
    pass
