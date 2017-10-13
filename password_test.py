import unittest
from password import Password


class TestPassword(unittest.TestCase):

    def __init__(self, first_name, last_name, account_name, password):
        '''
        Args:
        first_name: New password first name.
        last_name: New password last name.
        account_name: New password account name.
        password: New password password.
        '''

        def setUp(self):

            self.user_details = Password("Mchana", "Grantone", "ABC", "1234")


if __name__ == '__main__':
    unittest.main()
