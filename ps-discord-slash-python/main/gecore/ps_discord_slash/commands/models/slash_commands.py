from typing import List

from gecore.ps_discord_slash.models.commands import ApplicationCommand


class GuildPermissions:
    """"Governs guild permissions"""
    def __init__(self, guild: int, default_channel: int, request_channels: [int],
                 response_channel: int, allowed_roles: [int]):
        self.guild = guild
        self.default_channel = default_channel
        self.request_channels = request_channels
        self.response_channel = response_channel
        self.allowed_roles = allowed_roles


class GuildSlashCommand:
    """
    Local SlashCommand instance containing the Application command and permissions
    Stored including guild perms
    """
    def __init__(self, command: ApplicationCommand, guild_perms: GuildPermissions):
        self.perms = guild_perms
        self.command = command


class GuildSlashCommands:
    def __init__(self, guild_id: int, commands: List[GuildSlashCommand]):
        self.guild_id = guild_id
        self.guild_commands = commands
