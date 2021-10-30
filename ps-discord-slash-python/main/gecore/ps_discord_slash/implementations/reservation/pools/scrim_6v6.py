from gecore.ps_discord_slash.implementations.reservation.popular_6v6_bases import Popular6v6Bases
from gecore.ps_discord_slash.models.commands import ApplicationCommandOption, ApplicationCommandOptionType


def scrim_6v6_bases() -> ApplicationCommandOption:
    return ApplicationCommandOption(
        a_type=ApplicationCommandOptionType.STRING,
        name='base',
        description='Pick a scrim base',
        required=True,
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
                'name': Popular6v6Bases.PALE_CANYON_CHEMICAL.value,
                'value': Popular6v6Bases.PALE_CANYON_CHEMICAL.name
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
                'name': Popular6v6Bases.RIME_ANALYTICS.value,
                'value': Popular6v6Bases.RIME_ANALYTICS.name
            },
            {
                'name': Popular6v6Bases.NETTLEMIRE_GARDENS.value,
                'value': Popular6v6Bases.NETTLEMIRE_GARDENS.name
            },
            {
                'name': Popular6v6Bases.NS_MATERIAL_STORAGE.value,
                'value': Popular6v6Bases.NS_MATERIAL_STORAGE.name
            },
            {
                'name': Popular6v6Bases.XENOTECH_LABS.value,
                'value': Popular6v6Bases.XENOTECH_LABS.name
            }
        ]
    )
