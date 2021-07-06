from enum import Enum


class CommandException(Exception):

    def __init__(self, message):
        self.message = message


class CommandExceptionMessage(str, Enum):
    CommandNotAvailable = "This command is no longer available but still registered at the guild"
    GuildCommandNotFound = "The command has not been configured with the guild"
    GuildNotFound = "The guild has no configured commands yet"
    CommandNotFound = "The command could not be found, it might not be implemented"
    CommandNotInstanced = "The command-list requires instanced command variants"

