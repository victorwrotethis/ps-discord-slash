import datetime
from decimal import Decimal
from enum import Enum

from gecore.ps_discord_slash.models.components import ActionRow, ComponentType, Button, ButtonStyle
from gecore.ps_discord_slash.tools.time.time_service import get_earlier_day, get_utc_day_from_timestamp, \
    check_if_before_pst_midnight, get_twenty_days, get_month_from_timestamp, get_current_time, move_5days_backward, \
    can_move_5days_forward


# todo create from start of a date buttons up to a certain area.
#  Limit it to a month I guess?
#  Disable -5d or +5d if max has been reached?
#  errr what are we doing with years?


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

    if check_if_before_pst_midnight(start_date) is True:
        earlier_time = get_earlier_day(start_date, 1)
        reference_time = get_utc_day_from_timestamp(earlier_time)
    else:
        utc_time = get_utc_day_from_timestamp(start_date)
        reference_time = utc_time
    up_to_twenty_days = get_twenty_days(reference_time)
    action_rows = [add_navigation_buttons(command_id, reference_time, disable_old)]

    # todo split this one definitely
    date_button_components = []
    for date in up_to_twenty_days.items():
        button = Button(
            component_type=ComponentType.Button,
            custom_id=f'{command_id}|{DatePickerButtons.SPECIFIC_DAY}|{date[1]}',
            label=date[0],
            style=ButtonStyle.Primary
        )
        date_button_components.append(button)
    # using the length to determine the amount of iterations/rows of datepicker buttons
    amount_of_additional_rows = Decimal(len(date_button_components)) / Decimal(5)
    if amount_of_additional_rows <= 1:
        # create simple row
        row = create_action_row_for(date_button_components)
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
            action_rows.append(date_button_components[count:count+5])
            count = count + 5
        if exact_additional > 0:
            action_rows.append(date_button_components[count:count + int(exact_additional)])

    # todo See if we want to split up this method more.
    #  Actually use this is in testdate and flip the day back/forth?
    #  Move towards fixing pretty_time so we can get some feedback.
    #  We pretty much did the flow inside here. now we just need to process the navigation buttons.
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
            disabled=check_if_5days_backward_is_allowed(current_time, reference_time, disable_old)
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
            disabled=False if can_move_5days_forward(current_time) else True
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


def check_if_5days_backward_is_allowed(current_time: int, reference_time: int, disable_old: bool) -> bool:
    if disable_old is True:
        return current_time > reference_time
    else:
        current_day = get_utc_day_from_timestamp(current_time)
        five_days_check = move_5days_backward(current_time)
        return current_day != five_days_check
