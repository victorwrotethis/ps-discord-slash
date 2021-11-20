

class DatePickerCustomId:
    def __init__(self, command_id: str, task: str, timestamp: int):
        self.command_id = command_id
        self.task = task
        self.timestamp = timestamp


def retrieve_custom_id(incoming_custom_id: str) -> DatePickerCustomId:
    split_id = incoming_custom_id.split('|')
    return DatePickerCustomId(
        command_id=split_id[0],
        task=split_id[1],
        timestamp=int(split_id[2])
    )
