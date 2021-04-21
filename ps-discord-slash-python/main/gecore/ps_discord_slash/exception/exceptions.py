from enum import Enum


class CommandException(Exception):

    def __init__(self, message):
        self.message = message


class CommandExceptionMessage(str, Enum):
    CommandNotAvailable = "This command is no longer available but still registered at the guild"
    GuildCommandNotFound = "The command could not be found, unable to obtain permissions"
    CommandNotInstanced = "The command-list requires instanced command variants"
