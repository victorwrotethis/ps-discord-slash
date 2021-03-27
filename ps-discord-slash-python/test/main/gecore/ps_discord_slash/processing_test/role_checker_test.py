import unittest

from gecore.ps_discord_slash.processing.role_checker import check_if_allowed_role

# todo update to reflect changes to models

class RoleCheckerTest(unittest.TestCase):
    def test_check_if_allowed_role_true(self):
        test_roles = ['332587654111821827']
        result = check_if_allowed_role(test_roles)
        self.assertTrue(result)

    def test_check_if_allowed_role_false(self):
        test_roles = ['123456']
        result = check_if_allowed_role(test_roles)
        self.assertFalse(result)

    def test_bitstuff(self):
        varunda_result = (8053059559 & 0x00000008) != 0
        tafficante_result = (8053059431 & 0x00000008) != 0
        admin = (8589934591 & 0x00000008) != 0
        print(f'varunda: {varunda_result}')
        print(f'tafficante_: {tafficante_result}')
        print(f'admin: {admin}')


if __name__ == '__main__':
    unittest.main()
