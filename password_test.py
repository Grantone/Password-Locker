import unittest
from credential import Credential


class TestCredential(unittest.TestCase):

    def __init__(self, login_name, user_password, user_account):
        '''
        Args:
        login_name: New credential login name.
        user_password: New credential user password.
        user_account: New credential user account.
        '''

        def setUp(self):

            self.user_details = Credential("Mchana", "G1234", "Facebook")

            def test_init(self):
                '''
                Set up method to run before each test cases.
                '''
                self.assertEqual(self.user_details.login_name, "Mchana")
                self.assertEqual(self.user_details.user_password, "G1234")
                self.assertEqual(self.user_details.user_account, "Facebook")

                def test_save_credential(self):
                    '''
                    To save the credential test case to test if the credential object is being save in the credential list
                    '''
                    self.assertEqual(len(Credential.credential_list))


if __name__ == '__main__':
    unittest.main()
