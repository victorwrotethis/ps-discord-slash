from gecore.ps_discord_slash.implementations.reservation.popular_6v6_bases import Popular6v6Bases
from gecore.ps_discord_slash.models.commands import ApplicationCommandOption, ApplicationCommandOptionType


def hossin_6v6_bases() -> ApplicationCommandOption:
    return ApplicationCommandOption(
        a_type=ApplicationCommandOptionType.STRING,
        name=Popular6v6Bases.HOSSIN.value,
        description=f'Pick a base on {Popular6v6Bases.HOSSIN.value}',
        choices=[
            {
                'name': Popular6v6Bases.BRIDGEWATER_SHIPPING_YARD.value,
                'value': Popular6v6Bases.BRIDGEWATER_SHIPPING_YARD.name
            },
            {
                'name': Popular6v6Bases.CHAC_FUSION.value,
                'value': Popular6v6Bases.CHAC_FUSION.name
            },
            {
                'name': Popular6v6Bases.GHANAN_SOUTH.value,
                'value': Popular6v6Bases.GHANAN_SOUTH.name
            },
            {
                'name': Popular6v6Bases.NETTLEMIRE_GARDENS.value,
                'value': Popular6v6Bases.NETTLEMIRE_GARDENS.name
            }
        ]
    )
