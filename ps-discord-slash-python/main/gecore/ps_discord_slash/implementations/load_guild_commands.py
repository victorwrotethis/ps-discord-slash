from typing import List

from gecore.ps_discord_slash.commands.models.local_commands import GuildSlashCommands, SlashCommand
from gecore.ps_discord_slash.commands.models.local_permissions import CommandPermissions
from gecore.ps_discord_slash.implementations.bases.search_base_command import SearchBaseSlashCommand
from gecore.ps_discord_slash.implementations.pretty_time.test_date_command import TestDateInteractionCommand
from gecore.ps_discord_slash.implementations.reservation.start_reservation_command import StartReservationSlashCommand
from gecore.ps_discord_slash.models.discord_config import GenericConfig, JaegerEventChannel, JaegerEventRoles


def load_guild_commands() -> List[GuildSlashCommands]:
    """Loads in slash commands, currently in a manual fashion as there is just one guild served"""
    jaeger_guild_perms = CommandPermissions(
        guild=GenericConfig.JAEGER_EVENTS_GUILD,
        default_channel=JaegerEventChannel.SLASH_SPAM,
        request_channels=[JaegerEventChannel.SLASH_SPAM, JaegerEventChannel.OVO_BOT_DEV],
        response_channel=JaegerEventChannel.SLASH_SPAM,
        allowed_roles=[role.value for role in JaegerEventRoles]
    )
    search_base_id = SearchBaseSlashCommand.build(jaeger_guild_perms.guild)
    sb_guild_command = SlashCommand(search_base_id, jaeger_guild_perms)

    just_ovo_dev_perms = just_ovo_dev()
    start_reservation = StartReservationSlashCommand.build(just_ovo_dev_perms.guild)
    sr_command = SlashCommand(start_reservation, just_ovo_dev_perms)

    test_guild_perms = CommandPermissions(
        guild=GenericConfig.TEST_GUILD
    )

    test_date = TestDateInteractionCommand.build(test_guild_perms.guild)
    td_guild_command = SlashCommand(test_date, test_guild_perms)

    return [
        GuildSlashCommands(search_base_id.guild_id, [sb_guild_command, sr_command]),
        GuildSlashCommands(test_date.guild_id, [td_guild_command])
    ]


def just_ovo_dev() -> CommandPermissions:
    return CommandPermissions(
        guild=GenericConfig.JAEGER_EVENTS_GUILD,
        default_channel=JaegerEventChannel.SLASH_SPAM,
        request_channels=[JaegerEventChannel.OVO_BOT_DEV, JaegerEventChannel.SLASH_SPAM],
        response_channel=JaegerEventChannel.SLASH_SPAM,
        allowed_roles=[JaegerEventRoles.OVO_STAFF]
    )
