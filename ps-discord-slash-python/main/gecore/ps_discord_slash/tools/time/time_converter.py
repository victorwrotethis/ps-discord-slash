from datetime import datetime
import pytz

from gecore.ps_discord_slash.tools.time.time_variants import TimeZoneVariant, TimeVariant, MonthVariant


def create_utc_timestamp(
        hour: int, timezone_variant: TimeZoneVariant, minute: int = 0, month_variant: MonthVariant = None, day: int = 0,
        time_variant: TimeVariant = None) -> int:
    current_date = datetime.now()
    if day == 0 or day is None:
        day = current_date.day
    if month_variant is None:
        month = current_date.month
    else:
        month = month_variant.value[1]
    if time_variant is not None:
        hour = convert_time_of_day_to_24h(hour, time_variant)

    time_zone = convert_timezone(timezone_variant)
    desired_date = datetime(
        year=current_date.year,
        month=month,
        day=day,
        hour=hour,
        minute=minute
    )
    localised_time = time_zone.localize(desired_date)
    normalised_time = datetime.fromisoformat(str(localised_time))
    return int(normalised_time.timestamp())


def convert_timezone(timezone_variant: TimeZoneVariant):
    if timezone_variant is TimeZoneVariant.EASTERN:
        return pytz.timezone('US/Eastern')
    if timezone_variant is TimeZoneVariant.PACIFIC:
        return pytz.timezone('US/Pacific')
    if timezone_variant is TimeZoneVariant.UTC:
        return pytz.utc


def convert_time_of_day_to_24h(hour: int, time_variant: TimeVariant) -> int:
    """"Turns AM/PM system into 24 hour one"""
    if time_variant is TimeVariant.AM:
        if hour == 12:
            return 0
        else:
            return hour
    if time_variant is TimeVariant.PM:
        if hour == 12:
            return 12
        else:
            return hour + 12
