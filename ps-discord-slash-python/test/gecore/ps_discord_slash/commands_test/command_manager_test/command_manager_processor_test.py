import json
import unittest

from gecore.ps_discord_slash.commands.command_manager.command_manager_processor import process_command_manager
from gecore.ps_discord_slash.commands.models.available_commands import AvailableCommands
from gecore.ps_discord_slash.implementations.unplug.unplug_command import UnplugInteractionCommand


class CommandManagerProcessorTest(unittest.TestCase):


    def test_things_approved_role(self):

        incoming_role_request = '{"application_id":"789525379047358464","channel_id":"621502108080013352","data":{"id":"864331747390652427","name":"command_manager","options":[{"name":"approved_role","options":[{"name":"add","type":8,"value":"830241300275134494"},{"name":"remove","type":8,"value":"742175592861925447"}],"type":1}],"resolved":{"roles":{"742175592861925447":{"color":3447003,"hoist":false,"id":"742175592861925447","managed":false,"mentionable":false,"name":"notify role","permissions":"4399291969","position":3},"830241300275134494":{"color":15158332,"hoist":false,"id":"830241300275134494","managed":false,"mentionable":false,"name":"Slash Role","permissions":"4399291969","position":2}}}},"guild_id":"621502053373706241","id":"864670857557573673","member":{"roles":["742175417628360725"],"user":{"id":"97325654688681984"}},"type":2,"version":1}'
        request = json.loads(incoming_role_request)
        result = process_command_manager(give_commands(), request)
        print(result.data.content)


def give_commands() -> AvailableCommands:
    return AvailableCommands(
            command_list=[UnplugInteractionCommand()]
        )


