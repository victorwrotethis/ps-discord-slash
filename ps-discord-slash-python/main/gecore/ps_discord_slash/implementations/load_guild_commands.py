from typing import List

from gecore.ps_discord_slash.commands.models.guild_commands import GuildPermissions, GuildSlashCommands, \
    GuildSlashCommand
from gecore.ps_discord_slash.implementations.bases.search_base_command import SearchBaseSlashCommand
from gecore.ps_discord_slash.models.discord_config import GenericConfig, JaegerEventChannel, JaegerEventRoles


def load_guild_commands() -> List[GuildSlashCommands]:
    """Loads in slash commands, currently in a manual fashion as there is just one guild served"""
    guild_perms = GuildPermissions(
        guild=GenericConfig.JAEGER_EVENTS_GUILD,
        default_channel=JaegerEventChannel.SLASH_SPAM,
        request_channels=[JaegerEventChannel.SLASH_SPAM, JaegerEventChannel.OVO_BOT_DEV],
        response_channel=JaegerEventChannel.SLASH_SPAM,
        allowed_roles=[role.value for role in JaegerEventRoles]
    )
    sb_command_id = 828139760362192897
    sb_command_guild_version = 828139760362192898
    search_base_id = SearchBaseSlashCommand.build(sb_command_id, guild_perms.guild, sb_command_guild_version)
    sb_guild_command = GuildSlashCommand(search_base_id, guild_perms)
    return [GuildSlashCommands(search_base_id.guild_id, [sb_guild_command])]