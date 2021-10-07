import unittest

from gecore.ps_discord_slash.commands.models.command_decorator import try_wrapper, WrappedCommand


class CommandDecoratorTest(unittest.TestCase):
    def test_stuff(self):
        present = WrappedCommand("SpookieBoo")
        returned = try_wrapper(present)
        print('ok')
        print(returned)


if __name__ == '__main__':
    unittest.main()
