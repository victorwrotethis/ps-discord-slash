from gecore.ps_discord_slash.commands.command_interface import InteractionCommand
from gecore.ps_discord_slash.commands.models.local_permissions import CommandPermissions
from gecore.ps_discord_slash.exception.exceptions import CommandException, CommandExceptionMessage
from gecore.ps_discord_slash.models.commands import ApplicationCommand


class SlashCommand:
    """
     Local SlashCommand instance containing the Application command and permissions
     Stored including generic perms
     """
    def __init__(self, command: ApplicationCommand, permissions: CommandPermissions):
        self.perms = permissions
        self.command = command


class SlashCommands:
    def __init__(self, commands: list[SlashCommand], missing_response=CommandExceptionMessage.CommandNotFound):
        self.commands = commands
        self.missing_response = missing_response

    def find_command(self, incoming_command: InteractionCommand) -> SlashCommand:
        for slash_command in self.commands:
            if slash_command.command.name == incoming_command.identify():
                return slash_command
        raise CommandException(self.missing_response)


class GuildSlashCommands(SlashCommands):
    """
    Includes Guild id and provides a different message when the guild has no configuration for the command.
    Creates a new list if no command list is supplied.
    """
    def __init__(self, guild_id: int, commands: list[SlashCommand]):
        super().__init__(commands, CommandExceptionMessage.GuildCommandNotFound)
        self.guild_id = guild_id


class CommandSearchResult:
    def __init__(self, has_been_found: bool, found_command: SlashCommand = None, error_response: CommandException = None):
        self.has_been_found = has_been_found
        self.found_command = found_command
        self.error_response = error_response
