from gecore.ps_discord_slash.commands.models.local_commands import GuildSlashCommands, SlashCommand
from gecore.ps_discord_slash.commands.models.local_permissions import CommandPermissions
from gecore.ps_discord_slash.implementations.bob_commands.roll_call_command import RollCallInteractionCommand
from gecore.ps_discord_slash.implementations.pretty_time.test_date_command import TestDateInteractionCommand
from gecore.ps_discord_slash.implementations.discord_config import GenericConfig, NoFunChannel, NoFunRoles

# Should also be loaded in load_available_commands to show up


def load_guild_commands() -> list[GuildSlashCommands]:
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

    devispora_guild_perms = CommandPermissions(
        guild=GenericConfig.DEVISPORA
    )

    test_date = TestDateInteractionCommand.build(test_guild_perms.guild)
    td_guild_command = SlashCommand(test_date, test_guild_perms)

    test_date2 = TestDateInteractionCommand.build(devispora_guild_perms.guild)
    td_guild_command2 = SlashCommand(test_date, devispora_guild_perms)

    testing_roll_call = RollCallInteractionCommand.build(test_guild_perms.guild)
    trc_guild_command = SlashCommand(testing_roll_call, test_guild_perms)

    return [
        GuildSlashCommands(test_date.guild_id, [td_guild_command, trc_guild_command]),
        GuildSlashCommands(test_date2.guild_id, [td_guild_command2]),
    ]
