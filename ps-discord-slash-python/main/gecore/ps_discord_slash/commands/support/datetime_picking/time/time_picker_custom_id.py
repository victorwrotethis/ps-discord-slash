
class TimePickerCustomId:
    def __init__(self, command_id: str, task: str, timezone: str, hour_system: str, hours: int, minutes: int):
        self.command_id = command_id
        self.task = task
        self.timezone = timezone
        self.hour_system = hour_system
        self.hours = hours
        self.minutes = minutes


def retrieve_custom_id(incoming_custom_id: str) -> TimePickerCustomId:
    split_id = incoming_custom_id.split('|')
    return TimePickerCustomId(
        command_id=split_id[0],
        task=split_id[1],
        timezone=split_id[2],
        hour_system=split_id[3],
        hours=int(split_id[4]),
        minutes=int(split_id[5])
    )
