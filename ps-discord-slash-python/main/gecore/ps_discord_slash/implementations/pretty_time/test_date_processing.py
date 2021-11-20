from gecore.ps_discord_slash.commands.support.datetime_picking.date.date_picker_buttons import DatePickerTask
from gecore.ps_discord_slash.commands.support.datetime_picking.date.date_picker_interaction import \
    process_datepicker_interaction, process_date_navigation, init_date_picker
from gecore.ps_discord_slash.models.flags import DiscordFlags
from gecore.ps_discord_slash.models.interactions import InteractionResponse, InteractionResponseData, \
    InteractionResponseType
from gecore.ps_discord_slash.tools.time.time_service import check_if_before_pst_midnight, get_earlier_day, \
    is_current_day_in_utc, get_current_time


def make_pst_friendly_utc_day(reference_time: int):
    if check_if_before_pst_midnight(reference_time) is True:
        return get_earlier_day(reference_time, 1)
    else:
        return reference_time

# todo do we want to make this more generic and allowing to chose timezones remotely? Do we limit it to a few for now?
#  some function that calculates
def kickstart_datepicker(command_id: str) -> InteractionResponse:
    current_time = get_current_time()
    reference_time = make_pst_friendly_utc_day(current_time)
    return init_date_picker(command_id=command_id, timestamp=reference_time)


# Todo but we have the PST thing in here, which isn't great/
#  we're going to move out later so this particular function can move towards support
def process_datepicker_entry(command_id: str, command_body: {}, picked_date_function) -> InteractionResponse:
    """
    Processes incoming picked datepicker-options and uses the provided picked_date_function to handle your
    custom implementations from that moment.
    """
    parsed_custom_id, timestamp = process_datepicker_interaction(command_body=command_body, disable_old=True)
    if parsed_custom_id.task == DatePickerTask.SPECIFIC_DAY:
        return picked_date_function(timestamp)
    else:
        if is_current_day_in_utc(timestamp):
            timestamp = make_pst_friendly_utc_day(reference_time=timestamp)
        return process_date_navigation(command_id=command_id, timestamp=timestamp)


def process_date_picked(timestamp: int):
    return InteractionResponse(
        response_type=InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
        response_data=InteractionResponseData(
            content=f'Thank you for your contribution: <t:{timestamp}:R>',
            flags=DiscordFlags.NONE
        )
    )
