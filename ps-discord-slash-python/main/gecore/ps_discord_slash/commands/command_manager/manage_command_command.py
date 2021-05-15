from gecore.ps_discord_slash.commands.command_interface import ISlashCommand, SlashCommandType, IGlobalSlashCommand, \
    StartingPerms
from gecore.ps_discord_slash.commands.command_manager.manage_commands import ManageCommand
from gecore.ps_discord_slash.implementations.created_commands import OvOSlashCommand
from gecore.ps_discord_slash.models.commands import ApplicationCommand, ApplicationCommandOption, \
    ApplicationCommandOptionType, ApplicationCommandOptionChoice
from gecore.ps_discord_slash.models.discord_config import GenericConfig
from gecore.ps_discord_slash.models.interactions import InteractionResponse

# todo become generic so you can add commands to it.


class ManageCommandSlashCommand(IGlobalSlashCommand):

    @staticmethod
    def allow_dm_usage() -> bool:
        """"Already False by default, but to put emphasis this command is meant for usage in guilds only"""
        return False

    @staticmethod
    def command_type() -> SlashCommandType:
        return SlashCommandType.GLOBAL

    @staticmethod
    def identify() -> ManageCommand:
        return ManageCommand.MANAGE_COMMAND

    @staticmethod
    def starting_perms() -> StartingPerms:
        return StartingPerms.ADMINISTRATOR_ONLY

    @staticmethod
    def build(command_id: int, guild_id: int, version: int) -> ApplicationCommand:
        return ApplicationCommand(
            command_id=str(command_id),
            app_id=str(GenericConfig.APP_ID),
            name=OvOSlashCommand.MANAGE_COMMAND,
            description='Manage a particular command',
            version=version,
            guild_id=guild_id,
            options=[
                ApplicationCommandOption(
                    a_type=ApplicationCommandOptionType.SUB_COMMAND_GROUP,
                    name=OvOSlashCommand.SEARCH_BASE_ID.value,
                    description='The command you want to address',
                    options=[
                        ApplicationCommandOption(
                            a_type=ApplicationCommandOptionType.SUB_COMMAND,
                            name='enable',
                            description='Enable the command for this server',
                            options=[
                                ApplicationCommandOption(
                                    name='enable_command',
                                    description='Setting to false will remove all role permissions permanently',
                                    a_type=ApplicationCommandOptionType.BOOLEAN
                                )
                            ]
                        ),
                        ApplicationCommandOption(
                            a_type=ApplicationCommandOptionType.SUB_COMMAND,
                            name='role',
                            description='Manage roles',
                            options=[
                                ApplicationCommandOption(
                                    name='add',
                                    description='Add a role that is allowed to use the command',
                                    a_type=ApplicationCommandOptionType.ROLE
                                ),
                                ApplicationCommandOption(
                                    name='remove',
                                    description='Remove a role from being allowed to use the command',
                                    a_type=ApplicationCommandOptionType.ROLE
                                )
                            ]
                        ),
                        ApplicationCommandOption(
                            a_type=ApplicationCommandOptionType.SUB_COMMAND,
                            name='channel',
                            description='Manage channels',
                            options=[
                                ApplicationCommandOption(
                                    name='add',
                                    description='Add a channel where this command can be used',
                                    a_type=ApplicationCommandOptionType.CHANNEL
                                ),
                                ApplicationCommandOption(
                                    name='remove',
                                    description='Remove a channel where this command can be used',
                                    a_type=ApplicationCommandOptionType.CHANNEL
                                )
                            ]
                        )
                    ]
                )
            ]
        )

    def execute(self, command_body: {}) -> InteractionResponse:
        search_arg = command_body['data']['options'][0]['value']
        return None
