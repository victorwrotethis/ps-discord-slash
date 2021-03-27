from typing import List

from gecore.ps_discord_slash.commands.available_commands import build_search_base_id
from gecore.ps_discord_slash.commands.models.slash_commands import GuildSlashCommand, GuildPermissions, \
    GuildSlashCommands
from gecore.ps_discord_slash.models.discord_config import GenericConfig, JaegerEventChannel, JaegerEventRoles


def load_commands() -> List[GuildSlashCommands]:
    """Loads in slash commands, currently in a manual fashion as there is just one guild served"""
    guild_perms = GuildPermissions(
        GenericConfig.JAEGER_EVENTS_GUILD,
        [JaegerEventChannel.SLASH_SPAM, JaegerEventChannel.OVO_BOT_DEV],
        JaegerEventChannel.SLASH_SPAM,
        [role.value for role in JaegerEventRoles]
    )
    command_id = 790273936511336468
    command_guild_version = 809455046730186762
    search_base_id = build_search_base_id(command_id, guild_perms.guild, command_guild_version)
    guild_command = GuildSlashCommand(search_base_id, guild_perms)
    return [GuildSlashCommands(search_base_id.guild_id, [guild_command])]

