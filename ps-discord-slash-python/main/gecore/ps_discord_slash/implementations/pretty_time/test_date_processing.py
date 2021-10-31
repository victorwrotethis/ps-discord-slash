from gecore.ps_discord_slash.commands.support.date_picker_buttons.date_picker_buttons import DatePickerButtons, \
    create_date_buttons_from
from gecore.ps_discord_slash.commands.support.date_picker_buttons.date_picker_interaction import \
    process_datepicker_interaction
from gecore.ps_discord_slash.models.flags import DiscordFlags
from gecore.ps_discord_slash.models.interactions import InteractionResponse, InteractionResponseData, \
    InteractionResponseType


def process_datepicker_entry(command_id: str, command_body: {}) -> InteractionResponse:

    parsed_custom_id, timestamp = process_datepicker_interaction(command_body=command_body)

    if parsed_custom_id.task == DatePickerButtons.SPECIFIC_DAY:
        return InteractionResponse(
            response_type=InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
            response_data=InteractionResponseData(
                content=f'Thank you for your contribution: <t:{timestamp}:R>',
                flags=DiscordFlags.NONE
            )
        )
    else:
        action_rows = create_date_buttons_from(
            command_id=command_id,
            start_date=timestamp,
            disable_old=True,
            skip_pst_check=True
        )
        return InteractionResponse(
            response_type=InteractionResponseType.UPDATE_MESSAGE,
            response_data=InteractionResponseData(
                content='Please pick a date again',
                flags=DiscordFlags.NONE,
                components=action_rows
            )
        )

