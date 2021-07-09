from gecore.ps_discord_slash.commands.command_name_interface import SlashCommandName
from gecore.ps_discord_slash.models.commands import ApplicationCommand, ApplicationCommandSubmission


class ManageCommand(SlashCommandName):
    MANAGE_COMMAND = 'manage'


def create_command_submission(command: ApplicationCommand):
    return ApplicationCommandSubmission(
        name=command.name,
        description=command.description,
        options=command.options
    )
