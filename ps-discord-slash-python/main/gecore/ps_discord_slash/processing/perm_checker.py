from typing import List

from gecore.ps_discord_slash.commands.models.local_commands import SlashCommand
from gecore.ps_discord_slash.commands.models.local_permissions import CommandPermissionResult
from gecore.ps_discord_slash.models.default_interaction_responses import forbidden_response, default_command_channel
from gecore.ps_discord_slash.models.interactions import InteractionResponse, InteractionResponseType


def check_if_permitted(command_body: {}, slash_command: SlashCommand) -> CommandPermissionResult:
    """
    Checks if there are any guild permissions preventing from executing the command.
    If there are no permissions, it will check if the generic permissions will allow execution.
    """
    perms = slash_command.perms
    has_set_perms = False
    if perms.allowed_roles:
        has_set_perms = True
        if not check_if_allowed_role(command_body['member']['roles'], slash_command):
            return CommandPermissionResult(False, forbidden_response())
    if perms.allowed_users:
        has_set_perms = True
        if perms.guild:
            if not check_if_allowed_user(command_body['member']['user']['id'], slash_command):
                return CommandPermissionResult(False, forbidden_response())
        else:
            if 'user' in command_body:
                if not check_if_allowed_user(command_body['user']['id'], slash_command):
                    return CommandPermissionResult(False, forbidden_response())
    if perms.request_channels:
        if not check_if_correct_channel(command_body['channel_id'], slash_command):
            return CommandPermissionResult(False, default_command_channel(slash_command))

    # Passed through general perms
    return CommandPermissionResult(approved=True, has_set_perms=has_set_perms)


def check_if_allowed_role(role_list: List[str], guild_command: SlashCommand) -> bool:
    for role_id in role_list:
        if int(role_id) in guild_command.perms.allowed_roles:
            return True
    return False


def check_if_correct_channel(request_channel: str, guild_command: SlashCommand) -> bool:
    if int(request_channel) in guild_command.perms.request_channels:
        return True
    else:
        return False


def check_if_allowed_user(user_id: str, guild_command: SlashCommand) -> bool:
    if int(user_id) in guild_command.perms.allowed_users:
        return True
    else:
        return False


def return_not_permitted() -> InteractionResponse:
    return InteractionResponse(
        InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE, forbidden_response()
    )
