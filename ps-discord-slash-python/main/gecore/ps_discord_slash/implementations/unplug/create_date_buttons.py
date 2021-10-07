from gecore.ps_discord_slash.models.components import Button, ComponentType, ButtonStyle, ActionRow
from gecore.ps_discord_slash.models.flags import DiscordFlags
from gecore.ps_discord_slash.models.interactions import InteractionResponse, InteractionResponseType, \
    InteractionResponseData


def create_date_components() -> InteractionResponse:
    date_button_components = []
    action_rows = [add_navigation_buttons()]
    date_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    for date in date_list:
        button = Button(
            component_type=ComponentType.Button,
            custom_id=f'test|{date}|extract',
            label=date,
            style=ButtonStyle.Primary
        )
        date_button_components.append(button)
    count = 0
    while count < 20:
        action_rows.append(create_action_row_for(date_button_components[count:count+5]))
        count = count + 5
    return InteractionResponse(
        response_type=InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
        response_data=InteractionResponseData(
            content='Please pick a date',
            flags=DiscordFlags.NONE,
            components=action_rows
        )
    )


def create_action_row_for(button_list: [Button]) -> ActionRow:
    return ActionRow(
        component_type=ComponentType.ActionRow,
        components=button_list
    )


def add_navigation_buttons() -> ActionRow:
    buttons = [
        Button(
            component_type=ComponentType.Button,
            custom_id=f'test|previousMonth|extract',
            label='-1M',
            style=ButtonStyle.Danger
        ),
        Button(
            component_type=ComponentType.Button,
            custom_id=f'test|previous5Days|extract',
            label='-5D',
            style=ButtonStyle.Success
        ),
        Button(
            component_type=ComponentType.Button,
            custom_id=f'test|September|extract',
            label='SEP',
            style=ButtonStyle.Secondary,
            disabled=True
        ),
        Button(
            component_type=ComponentType.Button,
            custom_id=f'test|next5Days|extract',
            label='+5D',
            style=ButtonStyle.Success
        ),
        Button(
            component_type=ComponentType.Button,
            custom_id=f'test|nextMonth|extract',
            label='+1M',
            style=ButtonStyle.Danger
        )
    ]
    return ActionRow(
        component_type=ComponentType.ActionRow,
        components=buttons
    )
