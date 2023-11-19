import unittest
from gecore.ps_discord_slash.implementations.accounts.request_accounts import request_account


class RequestAccountsTest(unittest.TestCase):
    def test_request_account(self):
        requested_account = request_account()
        print(requested_account)
        self.assertEqual()


if __name__ == '__main__':
    unittest.main()
