from gecore.ps_discord_slash.implementations.reservation.popular_6v6_bases import Popular6v6Bases
from gecore.ps_discord_slash.models.commands import ApplicationCommandOption, ApplicationCommandOptionType


def esamir_6v6_bases() -> ApplicationCommandOption:
    return ApplicationCommandOption(
        a_type=ApplicationCommandOptionType.STRING,
        name=Popular6v6Bases.ESAMIR.value,
        description=f'Pick a base on {Popular6v6Bases.ESAMIR.value}',
        choices=[
            {
                'name': Popular6v6Bases.PALE_CANYON_CHEMICAL.value,
                'value': Popular6v6Bases.PALE_CANYON_CHEMICAL.name
            },
            {
                'name': Popular6v6Bases.RIME_ANALYTICS.value,
                'value': Popular6v6Bases.RIME_ANALYTICS.name
            },
        ]
    )
