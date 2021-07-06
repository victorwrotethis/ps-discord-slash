from gecore.ps_discord_slash.commands.models.local_commands import SlashCommand
from gecore.ps_discord_slash.exception.exceptions import CommandExceptionMessage
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


def command_error_response(message: CommandExceptionMessage) -> InteractionResponseData:
    return InteractionResponseData(
        content=message,
        flags=DiscordFlags.HIDDEN)


def default_command_channel(guild_slash_command: SlashCommand) -> InteractionResponseData:
    if guild_slash_command.perms.default_channel:
        return InteractionResponseData(
            content=f'Please use the <#{guild_slash_command.perms.default_channel}> channel instead.',
            flags=DiscordFlags.HIDDEN)
    else:
        return InteractionResponseData(
            content=f'You cannot use this command in this channel, but no default recommendation has been added',
            flags=DiscordFlags.HIDDEN)
