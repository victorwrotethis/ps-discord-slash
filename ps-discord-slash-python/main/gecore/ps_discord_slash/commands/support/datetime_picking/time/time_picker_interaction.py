from enum import Enum


class TimePickerTask(str, Enum):
    TIMEZONE = 'timezone'
    HOUR_SYSTEM = 'hourSystem'
    HOUR = 'hour'
    MINUTES = 'minutes'
    CONFIRMATION = 'confirmation'

# todo we've made the decision how to split the custom id.
#  what's left is:
#  Create initial buttons/kickstart in time-picker-buttons
#  Write flow for each making below in processing
#  Add to command, new command I guess?
#  Merge flow with ability to pass Timezone + time to datepicker to continue processing I guess?

def process_timepicker_interaction(command_body: {}):
    pass
    # todo First part would be:
    #  Retrieve custom ID
    #  CustomID needs to contain empty unsetvalues maybe?
    #  Process TimeZone Change-> (Allow 12h/24h + change customid)
    #  Process 12h/24h Change -> (Allow Hour, change Hour default if changed and not unset + change customid)
    #  Process Hour (allow Minutes + change customid)
    #  Process Minutes (allow Confirmation + change customid)
    #  Process Confirmation (Results in UTC timestamp + chosen Timezone)
