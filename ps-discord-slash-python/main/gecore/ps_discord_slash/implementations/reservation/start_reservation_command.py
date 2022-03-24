from gecore.ps_discord_slash.commands.command_interface import InteractionCommand, InteractionCommandType, StartingPerms
from gecore.ps_discord_slash.implementations.created_commands import OvOInteractionCommand
from gecore.ps_discord_slash.implementations.reservation.start_reservation_processing import process_reservation_start
from gecore.ps_discord_slash.models.commands import ApplicationCommand, ApplicationCommandOption, \
    ApplicationCommandOptionType
from gecore.ps_discord_slash.models.default_interaction_responses import not_properly_executed_response
from gecore.ps_discord_slash.models.discord_config import GenericConfig
from gecore.ps_discord_slash.models.flags import DiscordFlags
from gecore.ps_discord_slash.models.interactions import InteractionResponse, InteractionResponseData, \
    InteractionResponseType


class StartReservationSlashCommand(InteractionCommand):

    @staticmethod
    def command_type() -> InteractionCommandType:
        return InteractionCommandType.GUILD

    @staticmethod
    def identify() -> OvOInteractionCommand:
        return OvOInteractionCommand.START_RESERVATION

    @staticmethod
    def starting_perms() -> StartingPerms:
        return StartingPerms.ADMINISTRATOR_ONLY

    @staticmethod
    def build(guild_id: int = None) -> ApplicationCommand:
        return ApplicationCommand(
            app_id=str(GenericConfig.APP_ID),
            name=OvOInteractionCommand.START_RESERVATION,
            description='Generate a code to start a reservation',
            guild_id=guild_id,
            options=[
                ApplicationCommandOption(
                    a_type=ApplicationCommandOptionType.STRING,
                    name='group',
                    description='The group name the reservation is for',
                    required=True
                ),
                ApplicationCommandOption(
                    a_type=ApplicationCommandOptionType.STRING,
                    name='extrareps',
                    description='Add additional reps using @',
                    required=False
                )
            ]
        )

    def execute(self, command_body: {}) -> InteractionResponse:
        print(command_body)
        generated_link, acceptable = process_reservation_start(command_body)
        if acceptable:
            data = InteractionResponseData(
                content=f'Alright, lets start [here]({generated_link})!',
                flags=DiscordFlags.HIDDEN
            )
        else:
            data = not_properly_executed_response()
        return InteractionResponse(InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE, data)
