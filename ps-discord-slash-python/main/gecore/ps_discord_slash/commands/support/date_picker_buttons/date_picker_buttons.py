


# todo create from start of a date buttons up to a certain area.
# Limit it to a month I guess?
# Disable -5d or +5d if max has been reached?
# errr what are we doing with years?


def create_date_buttons_from(command_id: str, start_date: int, disable_old: bool = False):
    """
    command_id: The command id that is required to link these buttons to a command
    start_date: The timestamp date used as as starting point to create buttons from for 20 days.
    Includes previous 2 days if disable_old is False.
    disable_old: Bool Disables buttons of the past 2 days.
    """
    # Add up to the next 20 days
    # Refuse to add more days if the month ended.
    # Maybe a flag for *previous days* if to disable those buttons

    pass
