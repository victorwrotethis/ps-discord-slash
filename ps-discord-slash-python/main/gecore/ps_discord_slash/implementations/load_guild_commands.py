from typing import List

from gecore.ps_discord_slash.commands.models.local_commands import GuildSlashCommands, SlashCommand
from gecore.ps_discord_slash.commands.models.local_permissions import CommandPermissions
from gecore.ps_discord_slash.implementations.pretty_time.test_date_command import TestDateInteractionCommand
from gecore.ps_discord_slash.models.discord_config import GenericConfig, NoFunChannel, NoFunRoles


def load_guild_commands() -> List[GuildSlashCommands]:
    """Loads in slash commands, currently in a manual fashion as there is just one guild served"""
    no_fun_permissions = CommandPermissions(
        guild=GenericConfig.NO_FUN,
        default_channel=NoFunChannel.ROLL_CALL,
        request_channels=[NoFunChannel.ROLL_CALL, NoFunChannel.ROLL_CALL_BOT],
        response_channel=NoFunChannel.ROLL_CALL_BOT,
        allowed_roles=[role.value for role in NoFunRoles]
    )

    test_guild_perms = CommandPermissions(
        guild=GenericConfig.TEST_GUILD
    )

    test_date = TestDateInteractionCommand.build(test_guild_perms.guild)
    td_guild_command = SlashCommand(test_date, test_guild_perms)

    return [
        GuildSlashCommands(test_date.guild_id, [td_guild_command])
    ]
