from gecore.ps_discord_slash.commands.command_interface import ISlashCommand
from gecore.ps_discord_slash.commands.command_manager.manage_commands import find_management_command, ManageCommands, \
    ManageCommandAbbreviations
from gecore.ps_discord_slash.commands.models.available_commands import AvailableCommands
from gecore.ps_discord_slash.models.components import Button, ComponentType, ButtonStyle, ActionRow
from gecore.ps_discord_slash.models.flags import DiscordFlags
from gecore.ps_discord_slash.models.interactions import InteractionResponse, InteractionResponseType, \
    InteractionResponseData


def process_command_manager(available_commands: AvailableCommands, command_body: {}) -> InteractionResponse:
    # todo we're returning buttons here for the specific action the person wants to execute.
    #  So the job of this function is to turn this into components.
    command_data = command_body['data']
    sub_command_data = command_data['options'][0]
    management_command = find_management_command(sub_command_data['name'])
    if management_command is ManageCommands.APPROVED_ROLE:
        prep_custom_id = process_approve_role(sub_command_data)
        return create_button_components(available_commands.command_list, prep_custom_id)


def create_button_components(available_commands: [ISlashCommand], prep_custom_id: str) -> InteractionResponse:
    button_components = []
    for command in available_commands:
        command_name = command.identify().value
        button = Button(
            component_type=ComponentType.Button,
            custom_id=f'{ManageCommandAbbreviations.COMMAND_MANAGER.value}|{command_name}|{prep_custom_id}',
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
            content='Hello buttons',
            flags=DiscordFlags.HIDDEN,
            components=[action_row_component]
        )
    )


def process_approve_role(sub_command_data: {}) -> str:
    custom_id = f'{ManageCommandAbbreviations.APPROVED_ROLE.value}'
    for add_or_remove in sub_command_data['options']:
        option_name = find_management_command(add_or_remove['name'])
        role_id = add_or_remove['value']
        custom_id = f'{custom_id}|{option_name.value}|{role_id}'
    return custom_id
