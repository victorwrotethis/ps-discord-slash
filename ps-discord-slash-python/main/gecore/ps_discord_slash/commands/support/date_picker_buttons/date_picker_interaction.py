from gecore.ps_discord_slash.commands.support.date_picker_buttons.date_picker_buttons import DatePickerButtons, \
    create_date_buttons_from
from gecore.ps_discord_slash.models.flags import DiscordFlags
from gecore.ps_discord_slash.models.interactions import InteractionResponse, InteractionResponseType, \
    InteractionResponseData
from gecore.ps_discord_slash.tools.time.time_service import move_back_a_month, move_5days_backward, \
    move_5days_forward, move_to_next_month


class DatePickerCustomId:
    def __init__(self, custom_id: str, task: str, timestamp: int):
        self.custom_id = custom_id
        self.task = task
        self.timestamp = timestamp


def process_datepicker_interaction(command_body: {}, disable_old: bool = False) -> (DatePickerCustomId, int):
    custom_id = command_body["data"]["custom_id"]
    parsed_custom_id = retrieve_custom_id(custom_id)
    if parsed_custom_id.task == DatePickerButtons.PREVIOUS_MONTH:
        return parsed_custom_id, move_back_a_month(parsed_custom_id.timestamp, disable_old)
    elif parsed_custom_id.task == DatePickerButtons.PREVIOUS_5DAYS:
        return parsed_custom_id, move_5days_backward(parsed_custom_id.timestamp, disable_old)
    elif parsed_custom_id.task == DatePickerButtons.NEXT_5DAYS:
        return parsed_custom_id, move_5days_forward(parsed_custom_id.timestamp)
    elif parsed_custom_id.task == DatePickerButtons.NEXT_MONTH:
        return parsed_custom_id, move_to_next_month(parsed_custom_id.timestamp)
    elif parsed_custom_id.task == DatePickerButtons.SPECIFIC_DAY:
        return parsed_custom_id, parsed_custom_id.timestamp


def retrieve_custom_id(incoming_custom_id: str) -> DatePickerCustomId:
    split_id = incoming_custom_id.split('|')
    return DatePickerCustomId(
        custom_id=split_id[0],
        task=split_id[1],
        timestamp=int(split_id[2])
    )


def init_date_picker(command_id: str, timestamp: int) -> InteractionResponse:
    action_rows = create_date_buttons_from(
        command_id=command_id,
        start_date=timestamp,
        disable_old=True
    )
    return InteractionResponse(
        response_type=InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
        response_data=InteractionResponseData(
            content='Please pick a date',
            flags=DiscordFlags.NONE,
            components=action_rows
        )
    )


def process_date_navigation(command_id: str, timestamp: int) -> InteractionResponse:
    action_rows = create_date_buttons_from(
        command_id=command_id,
        start_date=timestamp,
        disable_old=True
    )
    return InteractionResponse(
        response_type=InteractionResponseType.UPDATE_MESSAGE,
        response_data=InteractionResponseData(
            content='Please pick a date again',
            flags=DiscordFlags.NONE,
            components=action_rows
        )
    )

