from decimal import Decimal
from enum import Enum

from gecore.ps_discord_slash.models.components import ActionRow, ComponentType, Button, ButtonStyle
from gecore.ps_discord_slash.tools.time.time_service import get_twenty_days, get_month_from_timestamp, get_current_time, \
    can_move_5days_forward, check_if_5days_backward_is_prohibited


class DatePickerButtons(str, Enum):
    PREVIOUS_MONTH = 'previousMonth'
    PREVIOUS_5DAYS = 'previous5Days'
    NEXT_5DAYS = 'next5Days'
    NEXT_MONTH = 'nextMonth'
    SPECIFIC_DAY = 'specificDay'


def create_date_buttons_from(command_id: str, start_date: int, disable_old: bool = False):
    """
    command_id: The command id that is required to link these buttons to a command
    start_date: The timestamp date used as as starting point to create buttons from for 20 days.
    disable_old: Bool Disables navigation buttons to go before current date.
    """
    up_to_twenty_days = get_twenty_days(start_date)
    date_button_components = create_buttons_from_days(command_id, up_to_twenty_days)
    action_rows = [add_navigation_buttons(command_id, start_date, disable_old)]
    return put_buttons_in_action_rows(action_rows, date_button_components)


def create_buttons_from_days(command_id: str, up_to_twenty_days: dict) -> []:
    date_button_components = []
    for date in up_to_twenty_days.items():
        button = Button(
            component_type=ComponentType.Button,
            custom_id=f'{command_id}|{DatePickerButtons.SPECIFIC_DAY}|{date[1]}',
            label=date[0],
            style=ButtonStyle.Primary
        )
        date_button_components.append(button)
    return date_button_components


def put_buttons_in_action_rows(action_rows: [], button_components: []):
    """Splits pool of buttons into action rows that can contain up to 5 buttons each."""
    amount_of_additional_rows = Decimal(len(button_components)) / Decimal(5)
    if amount_of_additional_rows <= 1:
        row = create_action_row_for(button_components)
        action_rows.append(row)
    else:
        if amount_of_additional_rows % 1 != 0:
            remainder = amount_of_additional_rows % 1
            exact_additional = remainder * 5
            row_range = amount_of_additional_rows - remainder
        else:
            exact_additional = 0
            row_range = amount_of_additional_rows
        count = 0
        for row in range(int(row_range)):
            row = create_action_row_for(button_components[count:count+5])
            action_rows.append(row)
            count = count + 5
        if exact_additional > 0:
            row = create_action_row_for(button_components[count:count + int(exact_additional)])
            action_rows.append(row)
    return action_rows


def create_action_row_for(button_list: [Button]) -> ActionRow:
    return ActionRow(
        component_type=ComponentType.ActionRow,
        components=button_list
    )


def add_navigation_buttons(command_id: str, reference_time: int, disable_old: bool) -> ActionRow:
    """
    Creates navigation buttons based on the reference time.
    Will disable backward buttons if disable_old is true and the reference time is before the current time.
    """
    month = get_month_from_timestamp(reference_time)
    current_time = get_current_time()
    buttons = [
        Button(
            component_type=ComponentType.Button,
            custom_id=f'{command_id}|{DatePickerButtons.PREVIOUS_MONTH}|{reference_time}',
            label='-1M',
            style=ButtonStyle.Danger,
            disabled=True if current_time > reference_time and disable_old is True else False
        ),
        Button(
            component_type=ComponentType.Button,
            custom_id=f'{command_id}|{DatePickerButtons.PREVIOUS_5DAYS}|{reference_time}',
            label='-5D',
            style=ButtonStyle.Success,
            disabled=check_if_5days_backward_is_prohibited(current_time, reference_time, disable_old)
        ),
        Button(
            component_type=ComponentType.Button,
            custom_id=f'{command_id}|{month.value[1]}|{reference_time}',
            label=f'{month.name}',
            style=ButtonStyle.Secondary,
            disabled=True
        ),
        Button(
            component_type=ComponentType.Button,
            custom_id=f'{command_id}|{DatePickerButtons.NEXT_5DAYS}|{reference_time}',
            label='+5D',
            style=ButtonStyle.Success,
            disabled=False if can_move_5days_forward(reference_time) else True
        ),
        Button(
            component_type=ComponentType.Button,
            custom_id=f'{command_id}|{DatePickerButtons.NEXT_MONTH}|{reference_time}',
            label='+1M',
            style=ButtonStyle.Danger
        )
    ]
    return ActionRow(
        component_type=ComponentType.ActionRow,
        components=buttons
    )
