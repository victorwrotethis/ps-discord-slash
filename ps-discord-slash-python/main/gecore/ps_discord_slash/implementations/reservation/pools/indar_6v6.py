from gecore.ps_discord_slash.implementations.reservation.popular_6v6_bases import Popular6v6Bases
from gecore.ps_discord_slash.models.commands import ApplicationCommandOption, ApplicationCommandOptionType


def indar_6v6_bases() -> ApplicationCommandOption:
    return ApplicationCommandOption(
        a_type=ApplicationCommandOptionType.STRING,
        name=Popular6v6Bases.INDAR.value,
        description=f'Pick a base on {Popular6v6Bases.INDAR.value}',
        required=True,
        choices=[
            {
                'name': Popular6v6Bases.NS_MATERIAL_STORAGE.value,
                'value': Popular6v6Bases.NS_MATERIAL_STORAGE.name
            },
            {
                'name': Popular6v6Bases.PERIS_EASTERN_GROVE.value,
                'value': Popular6v6Bases.PERIS_EASTERN_GROVE.name
            },
            {
                'name': Popular6v6Bases.RASHNU_WATCHTOWER.value,
                'value': Popular6v6Bases.RASHNU_WATCHTOWER.name
            },
            {
                'name': Popular6v6Bases.XENOTECH_LABS.value,
                'value': Popular6v6Bases.XENOTECH_LABS.name
            }
        ]
    )
