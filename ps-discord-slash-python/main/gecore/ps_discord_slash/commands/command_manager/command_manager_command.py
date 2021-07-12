from gecore.ps_discord_slash.commands.command_interface import SlashCommandType, IGlobalSlashCommand, \
    StartingPerms
from gecore.ps_discord_slash.commands.command_manager.command_manager_processor import process_command_manager
from gecore.ps_discord_slash.commands.command_manager.manage_commands import ManageCommands
from gecore.ps_discord_slash.commands.models.available_commands import AvailableCommands
from gecore.ps_discord_slash.models.commands import ApplicationCommand, ApplicationCommandOption, \
    ApplicationCommandOptionType
from gecore.ps_discord_slash.models.discord_config import GenericConfig
from gecore.ps_discord_slash.models.interactions import InteractionResponse


class CommandManagerSlashCommand(IGlobalSlashCommand):

    def __init__(self, available_commands: AvailableCommands):
        self.available_commands = available_commands

    @staticmethod
    def allow_dm_usage() -> bool:
        """"Already False by default, but to put emphasis this command is meant for usage in guilds only"""
        return False

    @staticmethod
    def command_type() -> SlashCommandType:
        return SlashCommandType.GLOBAL

    @staticmethod
    def identify() -> ManageCommands:
        return ManageCommands.COMMAND_MANAGER

    @staticmethod
    def starting_perms() -> StartingPerms:
        return StartingPerms.ADMINISTRATOR_ONLY

    @staticmethod
    def build(guild_id: int = None) -> ApplicationCommand:
        return ApplicationCommand(
            app_id=str(GenericConfig.APP_ID),
            name=ManageCommands.COMMAND_MANAGER,
            description='Manage a particular command',
            options=[
                ApplicationCommandOption(
                    a_type=ApplicationCommandOptionType.SUB_COMMAND,
                    name=ManageCommands.GUILD_COMMAND.value,
                    description='Add or Remove a command',
                    options=[ApplicationCommandOption(
                        name=ManageCommands.ACTION.value,
                        description='On removal, all permissions will be destroyed.',
                        a_type=ApplicationCommandOptionType.STRING,
                        required=True,
                        choices=[
                            {'name': ManageCommands.ADD.value, 'value': ManageCommands.ADD.value},
                            {'name': ManageCommands.REMOVE.value, 'value': ManageCommands.REMOVE.value}
                        ]
                    )]
                ),
                ApplicationCommandOption(
                    a_type=ApplicationCommandOptionType.SUB_COMMAND,
                    name=ManageCommands.APPROVED_ROLE.value,
                    description='Manage roles that can use a specific command',
                    options=[
                        ApplicationCommandOption(
                            name=ManageCommands.ADD.value,
                            description='Add a role that is allowed to use a command',
                            a_type=ApplicationCommandOptionType.ROLE
                        ),
                        ApplicationCommandOption(
                            name=ManageCommands.REMOVE.value,
                            description='Remove a role from being allowed to use a command',
                            a_type=ApplicationCommandOptionType.ROLE
                        )
                    ]
                ),
                ApplicationCommandOption(
                    a_type=ApplicationCommandOptionType.SUB_COMMAND,
                    name=ManageCommands.APPROVED_CHANNEL.value,
                    description='Manage channels that can use a specific command',
                    options=[
                        ApplicationCommandOption(
                            name=ManageCommands.ADD.value,
                            description='Add a channel where a specific command can be used',
                            a_type=ApplicationCommandOptionType.CHANNEL
                        ),
                        ApplicationCommandOption(
                            name=ManageCommands.REMOVE.value,
                            description='Remove a channel where a specific command can be used',
                            a_type=ApplicationCommandOptionType.CHANNEL
                        )
                    ]
                ),
                ApplicationCommandOption(
                    a_type=ApplicationCommandOptionType.SUB_COMMAND,
                    name=ManageCommands.APPROVED_USER.value,
                    description='Manage channels that can use a specific command',
                    options=[
                        ApplicationCommandOption(
                            name=ManageCommands.ADD.value,
                            description='Add a user that can use a specific command',
                            a_type=ApplicationCommandOptionType.USER,
                        ),
                        ApplicationCommandOption(
                            name=ManageCommands.REMOVE.value,
                            description='Remove a user that can use a specific command',
                            a_type=ApplicationCommandOptionType.USER
                        )
                    ]
                ),
                ApplicationCommandOption(
                    a_type=ApplicationCommandOptionType.SUB_COMMAND,
                    name=ManageCommands.DEFAULT_CHANNEL.value,
                    description='Set where users will be recommended to use a specific command',
                    options=[
                        ApplicationCommandOption(
                            name=ManageCommands.SET.value,
                            description='will add channel if it is not in allowed channels',
                            a_type=ApplicationCommandOptionType.CHANNEL
                        )
                    ]
                )
            ]
        )

    def execute(self, command_body: {}) -> InteractionResponse:
        return process_command_manager(self.available_commands, command_body)
