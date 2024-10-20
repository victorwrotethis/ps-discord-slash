from datetime import datetime, timedelta
import pytz
from dateutil.relativedelta import relativedelta

from gecore.ps_discord_slash.tools.time.time_variants import grab_month_variant_by_number, MonthVariant

one_hour_in_seconds = 3600
day_in_seconds = 86400
three_days = (day_in_seconds * 3)


def get_utc_day_from_timestamp(timestamp: int) -> int:
    current_date = datetime.fromtimestamp(timestamp, tz=pytz.utc)
    result = current_date.replace(hour=0, minute=0, second=0, microsecond=0)
    return int(result.timestamp())


def get_earlier_day(timestamp: int, days: int) -> int:
    previous_day = timestamp - (day_in_seconds * days)
    calibrated_day = get_utc_day_from_timestamp(previous_day)
    return calibrated_day


def get_current_time() -> int:
    return int(datetime.now(tz=pytz.utc).timestamp())


def get_month_from_timestamp(timestamp: int) -> MonthVariant:
    utc_datetime = datetime.fromtimestamp(timestamp, tz=pytz.utc)
    return grab_month_variant_by_number(utc_datetime.month)


def check_if_before_pst_midnight(timestamp: int) -> bool:
    utc_datetime = datetime.fromtimestamp(timestamp, tz=pytz.utc)
    if utc_datetime.hour < 7:
        return True
    else:
        return False


def move_to_next_month(starting_day: int) -> int:
    ref_date = datetime.fromtimestamp(starting_day, tz=pytz.utc)
    next_month = ref_date + relativedelta(months=+1)
    next_month = next_month.replace(day=1)
    return int(next_month.timestamp())


def move_back_a_month(starting_day: int, disable_old: bool) -> int:
    ref_date = datetime.fromtimestamp(starting_day, tz=pytz.utc)
    previous_month = ref_date + relativedelta(months=-1)
    previous_month_day = previous_month.replace(day=1)
    previous_month_timestamp = int(previous_month_day.timestamp())
    if disable_old is True:
        return validate_is_before_current_time(previous_month_timestamp)
    return previous_month_timestamp


def can_move_5days_forward(starting_day: int) -> bool:
    ref_date = datetime.fromtimestamp(starting_day, tz=pytz.utc)
    twenty_days_end = ref_date + timedelta(days=20)
    return ref_date.month == twenty_days_end.month


def move_5days_forward(starting_day: int) -> int:
    ref_date = datetime.fromtimestamp(starting_day, tz=pytz.utc)
    plus_5_days = ref_date + timedelta(days=5)
    return int(plus_5_days.timestamp())


def is_current_day_in_utc(reference_day: int) -> bool:
    current_utc_day = get_utc_day_from_timestamp(get_current_time())
    return reference_day == current_utc_day


def validate_is_before_current_time(reference_time: int) -> int:
    current_time = get_current_time()
    if reference_time < current_time:
        return get_utc_day_from_timestamp(current_time)
    else:
        return reference_time


def check_if_5days_backward_is_prohibited(current_time: int, reference_time: int, disable_old: bool) -> bool:
    if disable_old is True and current_time > reference_time:
        return True
    else:
        current_start_day = get_utc_day_from_timestamp(reference_time)
        five_days_check = move_5days_backward(reference_time, disable_old)
        return current_start_day != five_days_check


def move_5days_backward(starting_day: int, disable_old: bool) -> int:
    ref_date = datetime.fromtimestamp(starting_day, tz=pytz.utc)
    minus_5_days = ref_date - timedelta(days=5)
    if ref_date.month == minus_5_days.month:
        minus_5_days_timestamp = int(minus_5_days.timestamp())
        if disable_old is True:
            return validate_is_before_current_time(minus_5_days_timestamp)
        else:
            return minus_5_days_timestamp
    else:
        return int(ref_date.replace(day=1).timestamp())


def get_twenty_days(starting_day: int) -> dict:
    day_list: dict = {}
    ref_date = datetime.fromtimestamp(starting_day, tz=pytz.utc)
    for day in range(20):
        new_ref_date = ref_date + timedelta(days=day)
        if new_ref_date.day >= ref_date.day:
            day_list[new_ref_date.day] = int(new_ref_date.timestamp())
        else:
            break
    return day_list
    # we're making a dictionary of days + time. Because the custom id needs the timestamp instead of the day.
