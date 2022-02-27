import unittest

from gecore.ps_discord_slash.implementations.reservation.start_reservation_processing import retrieve_ids_if_rep, \
    retrieve_group_name, retrieve_required_info


class StartReservationProcessTest(unittest.TestCase):

    def test_retrieve_ids_if_rep_ok(self):
        example_event = basic_example()
        result = retrieve_ids_if_rep(example_event)
        self.assertEqual(482534612, result[0])

    def test_retrieve_group_name(self):
        example_event = basic_example()
        result = retrieve_group_name(example_event)
        self.assertEqual('HELP', result)

    def test_retrieve_required_info(self):
        example_event = basic_example()
        result = retrieve_required_info(example_event)
        self.assertEqual('HELP', result.group_name)
        self.assertEqual(482534611, result.requester_id)
        self.assertEqual([482534612], result.approved_ids)


def basic_example():
    return {
        "data": {
            "name": "startreservation",
            "options": [
                {
                    "name": "group",
                    "type": 3,
                    "value": "HELP"
                },
                {
                    "name": "extrareps",
                    "type": 3,
                    "value": "<@!482534612>"
                }
            ],
            "resolved": {
                "members": {
                    "482534612": {
                        "nick": "TestUser",
                        "roles": [
                            "298828610590998528"
                        ]
                    }
                },
                "users": {
                    "482534612": {
                        "discriminator": "4642",
                        "id": "482534612",
                        "public_flags": 640,
                        "username": "TestUser"
                    }
                }
            },
            "type": 1
        },
        "member": {
            "user": {
                "id": "482534611"
            }
        }
    }
