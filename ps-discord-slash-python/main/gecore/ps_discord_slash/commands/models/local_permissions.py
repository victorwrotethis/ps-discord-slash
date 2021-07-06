from gecore.ps_discord_slash.models.interactions import InteractionResponseData


class CommandPermissions:
    """"Governs permissions"""
    def __init__(self, guild: int = None, default_channel: int = None, request_channels: [int] = None,
                 response_channel: int = None, allowed_roles: [int] = None, allowed_users: [int] = None):
        self.guild = guild
        self.default_channel = default_channel
        self.request_channels = request_channels
        self.response_channel = response_channel
        self.allowed_roles = allowed_roles
        self.allowed_users = allowed_users


class CommandPermissionResult:
    def __init__(self, approved: bool, error_response: InteractionResponseData = None, has_set_perms: bool = False):
        self.approved = approved
        self.has_set_perms = has_set_perms
        self.error_response = error_response
