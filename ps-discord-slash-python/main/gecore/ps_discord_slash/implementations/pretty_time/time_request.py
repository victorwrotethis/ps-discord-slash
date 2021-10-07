from enum import Enum

from gecore.ps_discord_slash.tools.time.time_variants import grab_timezone_variant, grab_time_variant, \
    grab_month_variant, TimeZoneVariant, MonthVariant, TimeVariant


class PrettyTimeArgument(Enum):
    DAY = 'day'
    HOUR = 'hour'
    MINUTES = 'minutes'
    MONTH = 'month'
    TIMEOFDAY = 'timeofday'
    TIMEZONE = 'timezone'


class TimeRequest:
    hour: int
    day: int
    minute: int
    month: MonthVariant
    timezone_variant: TimeZoneVariant
    time_variant: TimeVariant


def create_time_request(command_body: {}) -> TimeRequest:
    command_data_opt = command_body['data']['options']
    time_request = TimeRequest()
    for answer in command_data_opt:
        answer_name = answer['name']
        answer_value = answer['value']
        if answer_name == PrettyTimeArgument.HOUR.value:
            time_request.hour = answer_value
        if answer_name == PrettyTimeArgument.DAY.value:
            time_request.day = answer_value
        if answer_name == PrettyTimeArgument.MINUTES.value:
            time_request.minute = answer_value
        if answer_name == PrettyTimeArgument.MONTH.value:
            time_request.month = grab_month_variant(answer_value)
        if answer_name == PrettyTimeArgument.TIMEZONE.value:
            time_request.timezone_variant = grab_timezone_variant(answer_value)
        if answer_name == PrettyTimeArgument.TIMEOFDAY.value:
            time_request.time_variant = grab_time_variant(answer_value)
    return time_request
