from gecore.ps_discord_slash.commands.command_manager.command_manager_command import CommandManagerInteractionCommand
from gecore.ps_discord_slash.commands.models.local_commands import SlashCommand, SlashCommands
from gecore.ps_discord_slash.commands.models.local_permissions import CommandPermissions
from gecore.ps_discord_slash.implementations.pretty_time.time_prettifier_command import PrettyTimeInteractionCommand
from gecore.ps_discord_slash.implementations.unplug.unplug_command import UnplugInteractionCommand


def load_global_commands() -> SlashCommands:
    global_perms = CommandPermissions(allowed_users=[97325654688681984])
    unplug_command = UnplugInteractionCommand.build()
    sb_unplug_command = SlashCommand(unplug_command, global_perms)
    management_command = CommandManagerInteractionCommand.build()
    sb_management_command = SlashCommand(management_command, global_perms)
    global_perms_free = CommandPermissions()
    pretty_time_command = PrettyTimeInteractionCommand.build()
    pt_command = SlashCommand(pretty_time_command, global_perms_free)
    return SlashCommands([sb_unplug_command, sb_management_command, pt_command])
