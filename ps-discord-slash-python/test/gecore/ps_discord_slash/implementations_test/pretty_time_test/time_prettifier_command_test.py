import unittest

from gecore.ps_discord_slash.implementations.pretty_time.time_prettifier_command import PrettyTimeInteractionCommand


class TimePrettifierCommandTest(unittest.TestCase):

    def test_execute(self):
        command_body = {"data": {
            "id": "882470755709886515",
            "name": "pretty_time",
            "options": [{
                "name": "month",
                "type": 3,
                "value": "JAN"
            }, {
                "name": "day",
                "type": 4,
                "value": 3
            }, {
                "name": "timezone",
                "type": 3,
                "value": "EASTERN"
            }, {
                "name": "hour",
                "type": 4,
                "value": 3
            },
             #    ,
             #    {
             #    "name": "minutes",
             #    "type": 4,
             #    "value": 30
             # }
             {
                "name": "timeofday",
                "type": 3,
                "value": "PM"
            }
            ],
            "type": 1
        }}
        command = PrettyTimeInteractionCommand()
        result = command.execute(command_body)
        print(result)
