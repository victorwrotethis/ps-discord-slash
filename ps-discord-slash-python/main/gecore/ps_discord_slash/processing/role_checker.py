from typing import List

from gecore.ps_discord_slash.commands.models.guild_commands import GuildSlashCommand


def check_if_allowed_role(role_list: List[str], guild_command: GuildSlashCommand) -> bool:
    for role_id in role_list:
        if int(role_id) in guild_command.perms.allowed_roles:
            return True
    return False


def check_if_correct_channel(request_channel: str, guild_command: GuildSlashCommand) -> bool:
    if int(request_channel) in guild_command.perms.request_channels:
        return True
    else:
        return False
