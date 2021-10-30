from enum import Enum


class TimeVariant(Enum):
    AM = 'AM'
    PM = 'PM'


class TimeZoneVariant(Enum):
    EASTERN = 'Eastern US Time'
    PACIFIC = 'Pacific US Time'
    UTC = 'Coordinated Universal Time'


class MonthVariant(Enum):
    JAN = 'January', 1
    FEB = 'February', 2
    MAR = 'March', 3
    APR = 'April', 4
    MAY = 'May', 5
    JUN = 'June', 6
    JUL = 'July', 7
    AUG = 'August', 8
    SEP = 'September', 9
    OCT = 'October', 10
    NOV = 'November', 11
    DEC = 'December', 12


def grab_timezone_variant(timezone: str) -> TimeZoneVariant:
    for enum in TimeZoneVariant:
        if enum.name == timezone:
            return enum


def grab_time_variant(time_variant: str) -> TimeVariant:
    for enum in TimeVariant:
        if enum.value == time_variant:
            return enum


def grab_month_variant(month: str) -> MonthVariant:
    for enum in MonthVariant:
        if enum.name == month:
            return enum


def grab_month_variant_by_number(month: int) -> MonthVariant:
    for enum in MonthVariant:
        if enum.value[1] == month:
            return enum
