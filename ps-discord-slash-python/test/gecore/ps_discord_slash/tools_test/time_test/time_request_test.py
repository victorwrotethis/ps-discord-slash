import unittest

from gecore.ps_discord_slash.implementations.pretty_time.time_request import create_time_request


class TimeRequestTest(unittest.TestCase):

    def test_create_time_request_body(self):
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
            }, {
                "name": "minutes",
                "type": 4,
                "value": 30
            }, {
                "name": "timeofday",
                "type": 3,
                "value": "AM"
            }
            ],
            "type": 1
        }}
        result = create_time_request(command_body)
        print(result)
