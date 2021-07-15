from enum import Enum


class InteractionCommandName(Enum):
    """Enforces enum usage for interaction command names for processing"""

    @staticmethod
    def provide_members():
        pass

    def __getstate__(self):
        """Allows JsonPickle just to retrieve the value"""
        return self.value
