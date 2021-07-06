from gecore.ps_discord_slash.commands.models.local_commands import SlashCommand, SlashCommands
from gecore.ps_discord_slash.commands.models.local_permissions import CommandPermissions
from gecore.ps_discord_slash.implementations.unplug.unplug_command import UnplugSlashCommand


def load_global_commands() -> SlashCommands:
    global_perms = CommandPermissions(allowed_users=[97325654688681984])
    test_global_command_id = 861062885790187590
    test_global_command_version = 861062885790187591
    unplug_command = UnplugSlashCommand.build(test_global_command_id, test_global_command_version)
    sb_unplug_command = SlashCommand(unplug_command, global_perms)
    return SlashCommands([sb_unplug_command])
