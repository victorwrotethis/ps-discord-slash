from gecore.ps_discord_slash.commands.command_interface import InteractionCommand
from gecore.ps_discord_slash.commands.command_manager.custom_id_creator import ButtonSupportContent
from gecore.ps_discord_slash.commands.command_manager.manage_commands import ManageCommandAbbreviations
from gecore.ps_discord_slash.models.components import Button, ComponentType, ButtonStyle, ActionRow
from gecore.ps_discord_slash.models.flags import DiscordFlags
from gecore.ps_discord_slash.models.interactions import InteractionResponse, InteractionResponseType, \
    InteractionResponseData


def create_button_components(available_commands: [InteractionCommand], support_content: ButtonSupportContent) \
        -> InteractionResponse:
    button_components = []
    for command in available_commands:
        command_name = command.identify().value
        button = Button(
            component_type=ComponentType.Button,
            custom_id=f'{ManageCommandAbbreviations.COMMAND_MANAGER.value}|{command_name}|{support_content.custom_id}',
            label=command_name,
            style=ButtonStyle.Primary
        )
        button_components.append(button)
    action_row_component = ActionRow(
        component_type=ComponentType.ActionRow,
        components=button_components
    )
    return InteractionResponse(
        response_type=InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
        response_data=InteractionResponseData(
            content=support_content.content,
            flags=DiscordFlags.NONE,
            components=[action_row_component]
        )
    )
