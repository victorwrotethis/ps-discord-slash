from gecore.ps_discord_slash.tools.time.time_variants import MonthVariant


def provide_months() -> []:
    months = []
    for month in MonthVariant:
        months.append(create_month_choice(month))
    return months


def create_month_choice(month: MonthVariant):
    return {
        'name': month.value[0],
        'value': month.name
    }
