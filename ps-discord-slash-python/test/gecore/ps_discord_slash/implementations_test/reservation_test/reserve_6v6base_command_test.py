import json
import unittest
from datetime import datetime

import jsonpickle

from gecore.ps_discord_slash.commands.command_manager.manage_commands import create_command_submission
from gecore.ps_discord_slash.implementations.reservation.reserve_6v6base_command import Reserve6v6BaseSlashCommand
from gecore.ps_discord_slash.tools.time.pick_time import provide_months


class Reserve6v6BaseCommandTest(unittest.TestCase):
    def test_things(self):
        command = Reserve6v6BaseSlashCommand.build(1)
        submission = create_command_submission(command)
        result = json.loads(jsonpickle.encode(submission, unpicklable=False))
        print(json.dumps(result))

    def test_month(self):
        mydate = datetime.now()
        print(provide_months())
