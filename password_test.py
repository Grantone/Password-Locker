from credential import Credential
import unittest


class TestCredential(unittest.TestCase):

    def __init__(self, login_name, user_password, user_account):
        '''
        Args:
        login_name: New credential login name.
        user_password: New credential user password.
        user_account: New password user account.
        '''

        def setUp(self):

            self.user_details = Password("Mchana", "G1234", "Facebook")

            def test_init(self):
                '''
                Set up method to run before each test cases.
                '''
                self.assertEqual(self.user_details.login_name, "Mchana")
                self.assertEqual(self.user_details.user_password, "G1234")
                self.assertEqual(self.user_details.user_account, "Facebook")


if __name__ == '__main__':
    unittest.main()
