from gecore.ps_discord_slash.commands.models.slash_commands import GuildSlashCommand
from gecore.ps_discord_slash.models.flags import DiscordFlags
from gecore.ps_discord_slash.models.interactions import InteractionResponseData


def empty_response() -> InteractionResponseData:
    return InteractionResponseData(
        content=None,
        flags=DiscordFlags.NONE)


def forbidden_response() -> InteractionResponseData:
    return InteractionResponseData(
        content='You are not allowed to use this command',
        flags=DiscordFlags.HIDDEN)


def not_configured_response() -> InteractionResponseData:
    return InteractionResponseData(
        content='This command has not been configured',
        flags=DiscordFlags.HIDDEN)


def default_command_channel(guild_slash_command: GuildSlashCommand) -> InteractionResponseData:
    return InteractionResponseData(
        content=f'Please use the <#{guild_slash_command.perms.default_channel}> channel instead.',
        flags=DiscordFlags.HIDDEN)
