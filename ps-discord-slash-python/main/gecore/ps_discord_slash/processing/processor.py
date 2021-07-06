from gecore.ps_discord_slash.commands.command_interface import ISlashCommand
from gecore.ps_discord_slash.commands.models.local_commands import SlashCommand
from gecore.ps_discord_slash.models.default_interaction_responses import default_command_channel, forbidden_response
from gecore.ps_discord_slash.models.interactions import InteractionResponseType, InteractionResponse
from gecore.ps_discord_slash.processing.perm_checker import check_if_correct_channel, check_if_allowed_role

# deprecated
def process_guild_command(command_body: {}, guild_command: SlashCommand, command: ISlashCommand) \
        -> InteractionResponse:
    """"Will perform the command if it is allowed to be executed based on channel and roles"""
    if check_if_allowed_role(command_body['member']['roles'], guild_command):
        if check_if_correct_channel(command_body['channel_id'], guild_command):
            return process_actual_command(command_body, command)
        else:
            return InteractionResponse(
                InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
                default_command_channel(guild_command)
            )
    else:
        return InteractionResponse(InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE, forbidden_response())


def process_actual_command(command_body: {}, slash_command: ISlashCommand):
    """"Will execute the interface method"""
    return slash_command.execute(command_body=command_body)
