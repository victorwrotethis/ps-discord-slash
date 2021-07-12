from gecore.ps_discord_slash.commands.command_manager.command_manager_command import CommandManagerSlashCommand
from gecore.ps_discord_slash.commands.models.local_commands import SlashCommand, SlashCommands
from gecore.ps_discord_slash.commands.models.local_permissions import CommandPermissions
from gecore.ps_discord_slash.implementations.unplug.unplug_command import UnplugSlashCommand


def load_global_commands() -> SlashCommands:
    global_perms = CommandPermissions(allowed_users=[97325654688681984])
    unplug_command = UnplugSlashCommand.build()
    sb_unplug_command = SlashCommand(unplug_command, global_perms)
    management_command = CommandManagerSlashCommand.build()
    sb_management_command = SlashCommand(management_command, global_perms)
    return SlashCommands([sb_unplug_command, sb_management_command])
