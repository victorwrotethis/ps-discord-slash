import json
import unittest

from gecore.ps_discord_slash.implementations.created_commands import OvOInteractionCommand
from gecore.ps_discord_slash.implementations.load_available_commands import check_if_commands_loaded
from gecore.ps_discord_slash.processing.interaction_processor import InteractionProcessor


class CommandProcessorTest(unittest.TestCase):
    def test_find_command_from_list(self):
        search_base_id = 'searchbaseid'
        command_processor = InteractionProcessor()
        check_if_commands_loaded(command_processor)
        result = command_processor.available_commands.retrieve_command(search_base_id)
        self.assertEqual(OvOInteractionCommand.SEARCH_BASE_ID, result.identify())

    def test_process_command(self):
        json_stuff = '{"channel_id":"790298629721554974","data":{"id":"790273936511336468","name":"searchbaseid","options":[{"name":"byname","value":"bridgewater"}]},"guild_id":"207168033918025729","id":"796053701664047134","member":{"deaf":false,"is_pending":false,"joined_at":"2016-08-15T22:22:27.871000+00:00","mute":false,"nick":null,"pending":false,"permissions":"1610608631","premium_since":null,"roles":["207168817749557248","332587654111821827","333398154739187722","702306952507555870","711008764291186698","711355090711216210","739498857192489020"],"user":{"avatar":"omitted","discriminator":"omitted","id":"omitted","public_flags":512,"username":"omitted"}},"token":"token","type":2,"version":1}'
        loaded_json = json.loads(json_stuff)
        command_processor = InteractionProcessor()
        check_if_commands_loaded(command_processor)
        result = command_processor.process_command_request(loaded_json)
        print(result.data.content)

    def test_process_comman_dm(self):
        json_stuff = '{"application_id":"789525379047358464","channel_id":"790393329975820319","data":{"id":"861062885790187590","name":"unplug","options":[{"name":"system","type":3,"value":"DMTest"}]},"id":"861074690676228116","token":"aW50ZXJhY3Rpb246ODYxMDc0NjkwNjc2MjI4MTE2OkZWVk9oNFRnOWt1RE5rUGRPMUppRm41VkhhMm0xUUlHVkVaYzVsU1dlOFdUemxEb3lJZVZaWHVvWTlPU0g3dXROckpuS3FwS1JyQk9Zd2xiNVc0SlpsN216SXpzMkl1Z3FHSFRhR1c1a25jWVpQbEZFeXROY2IzbzViOW5NU1pv","type":2,"user":{"avatar":"8d45452671e91d7052a4d56c39150cc7","discriminator":"3554","id":"97325654688681984","public_flags":512,"username":"Pronam"},"version":1}'
        loaded_json = json.loads(json_stuff)
        command_processor = InteractionProcessor()
        check_if_commands_loaded(command_processor)
        result = command_processor.process_command_request(loaded_json)
        print(result.data.content)

    def test_enum(self):
        for ovo_thing in OvOInteractionCommand:
            print(ovo_thing)
