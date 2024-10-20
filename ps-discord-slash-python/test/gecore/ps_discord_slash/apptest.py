import json
import unittest

import jsonpickle

from gecore.ps_discord_slash.app import lambda_handler
from gecore.ps_discord_slash.commands.command_manager.command_manager_command import CommandManagerInteractionCommand
from gecore.ps_discord_slash.commands.command_manager.manage_commands import create_command_submission


class AppTest(unittest.TestCase):

    def test_lambda_handler(self):
        event = {'version': '2.0', 'routeKey': 'POST /discordTest', 'rawPath': '/discordTest', 'rawQueryString': '', 'headers': {'accept': '*/*', 'content-length': '271', 'content-type': 'application/json', 'host': 'j1j1rs3l43.execute-api.eu-west-1.amazonaws.com', 'user-agent': 'Discord-Interactions/1.0 (+https://discord.com)', 'x-amzn-trace-id': 'Root=1-5fdcd619-0409d579295ebc56477732a4', 'x-forwarded-for': '34.74.32.1', 'x-forwarded-port': '443', 'x-forwarded-proto': 'https', 'x-signature-ed25519': '529a52bbb95275760b82020cdf8a22f96c78dda953bf0195e2b4102659ebdc53d3a34d541b44a447c75939aa17905f273182111a582223dc7a2d5451bd75df0d', 'x-signature-timestamp': '1608308249'}, 'requestContext': {'accountId': '311378485556', 'apiId': 'j1j1rs3l43', 'domainName': 'j1j1rs3l43.execute-api.eu-west-1.amazonaws.com', 'domainPrefix': 'j1j1rs3l43', 'http': {'method': 'POST', 'path': '/discordTest', 'protocol': 'HTTP/1.1', 'sourceIp': '34.74.32.1', 'userAgent': 'Discord-Interactions/1.0 (+https://discord.com)'}, 'requestId': 'XwZkCioLjoEEPew=', 'routeKey': 'POST /discordTest', 'stage': '$default', 'time': '18/Dec/2020:16:17:29 +0000', 'timeEpoch': 1608308249751}, 'body': '{"id":"789526763960139777","token":"aW50ZXJhY3Rpb246Nzg5NTI2NzYzOTYwMTM5Nzc3OmxoVVNrUTY4SWNjRHoyN1JRUENhdlVGNWdtbmZWSnlLQTN4SFBmM2VEcmhPb3M3M1pxOG1Sbkc2V1J1SEZjdVN2Nkl3d0xDZDJGWUlGWkY5ZzNHTjNRQzZKbVVzeG84bjdxTk1ZTnNPa3NhTVoxVXVvWXdKR3F0a29EVTdBOW5l","type":1,"version":1}', 'isBase64Encoded': False}
        result = lambda_handler(event, None)
        print(result)

    def test_command(self):
        command = CommandManagerInteractionCommand.build(1)
        submission = create_command_submission(command)

        result = json.loads(jsonpickle.encode(submission, unpicklable=False))
        print(json.dumps(result))


if __name__ == '__main__':
    unittest.main()
