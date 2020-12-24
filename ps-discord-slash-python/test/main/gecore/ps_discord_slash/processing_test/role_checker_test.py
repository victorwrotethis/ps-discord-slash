import unittest

from gecore.ps_discord_slash.processing.role_checker import check_if_allowed_role


class RoleCheckerTest(unittest.TestCase):
    def test_check_if_allowed_role_true(self):
        test_roles = ['332587654111821827']
        result = check_if_allowed_role(test_roles)
        self.assertTrue(result)

    def test_check_if_allowed_role_false(self):
        test_roles = ['123456']
        result = check_if_allowed_role(test_roles)
        self.assertFalse(result)
