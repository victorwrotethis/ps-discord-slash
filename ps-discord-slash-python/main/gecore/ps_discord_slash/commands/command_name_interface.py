from enum import Enum


class SlashCommandName(Enum):
    """Enforces enum usage for slash command names for processing"""

    @staticmethod
    def provide_members():
        pass

    def __getstate__(self):
        """Allows JsonPickle just to retrieve the value"""
        return self.value
