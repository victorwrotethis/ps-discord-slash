import json
import unittest

from gecore.ps_discord_slash.implementations.created_commands import OvOSlashCommand
from gecore.ps_discord_slash.commands.models.available_commands import load_guild_commands
from gecore.ps_discord_slash.processing.processor import find_command, process_command


class CommandProcessorTest(unittest.TestCase):
    def test_find_command_from_list(self):
        search_base_id = 'searchbaseid'
        loaded_commands = load_guild_commands()
        result = find_command(search_base_id, loaded_commands[0])
        self.assertEqual(OvOSlashCommand.SEARCH_BASE_ID, result[0].identify())

    def test_process_command(self):
        json_stuff = '{"channel_id":"790298629721554974","data":{"id":"790273936511336468","name":"searchbaseid","options":[{"name":"byname","value":"bridgewater"}]},"guild_id":"207168033918025729","id":"796053701664047134","member":{"deaf":false,"is_pending":false,"joined_at":"2016-08-15T22:22:27.871000+00:00","mute":false,"nick":null,"pending":false,"permissions":"1610608631","premium_since":null,"roles":["207168817749557248","332587654111821827","333398154739187722","702306952507555870","711008764291186698","711355090711216210","739498857192489020"],"user":{"avatar":"omitted","discriminator":"omitted","id":"omitted","public_flags":512,"username":"omitted"}},"token":"token","type":2,"version":1}'
        loaded_json = json.loads(json_stuff)
        result = process_command(loaded_json)
        print(result.data.content)

    def test_enum(self):
        for ovo_thing in OvOSlashCommand:
            print(ovo_thing)
