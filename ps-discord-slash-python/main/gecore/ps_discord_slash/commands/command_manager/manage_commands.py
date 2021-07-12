from gecore.ps_discord_slash.commands.command_name_interface import SlashCommandName
from gecore.ps_discord_slash.models.commands import ApplicationCommand, ApplicationCommandSubmission


class ManageCommands(SlashCommandName):
    COMMAND_MANAGER = 'command_manager'
    GUILD_COMMAND = 'guild_command'
    ADD = 'add'
    REMOVE = 'remove'
    SET = 'set'
    LIST = 'list'
    DEFAULT_CHANNEL = 'default_channel'
    APPROVED_CHANNEL = 'approved_channel'
    APPROVED_USER = 'approved_user'
    APPROVED_ROLE = 'approved_role'


def create_command_submission(command: ApplicationCommand):
    return ApplicationCommandSubmission(
        name=command.name,
        description=command.description,
        options=command.options
    )
