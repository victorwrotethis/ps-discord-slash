from gecore.ps_discord_slash.commands.command_manager.command_button_creator import create_button_components
from gecore.ps_discord_slash.commands.command_manager.custom_id_creator import create_button_support_content
from gecore.ps_discord_slash.commands.models.available_commands import AvailableCommands
from gecore.ps_discord_slash.models.interactions import InteractionResponse


def process_command_manager(available_commands: AvailableCommands, command_body: {}) -> InteractionResponse:
    # todo we're returning buttons here for the specific action the person wants to execute.
    #  So the job of this function is to turn this into components.
    prep_custom_id = create_button_support_content(command_body)
    return create_button_components(available_commands.command_list, prep_custom_id)

# todo additionally, it needs to split between incoming components and the original request.
#  It does currently recognise it, because we did at the flow it'll check the first bit for commands.
#  However, it will currently break because it'll try and perform a flow it can't execute.
#  This is also due to the fact we're splitting between execute and component_execute
