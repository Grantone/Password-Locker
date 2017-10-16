import unittest
from credential import Credential


class TestUser(unittest.TestCase)


def setUp(self):
    """
    Class that runs every new instances of credentials
    """


self.new_credent = Credential
('Mchana', 'q1234', 'email')

    credential_list = []  # Empty contact list
    # Init method up here

    def setUp(self):
        '''
        to set up all the credentials as created
        '''

        self.assertEqual(self.new_credent.username, 'Mchana')
        self.assertEqual(self.new_credent.password, 'q1234')
        self.assertEqual(self.new_credent.account, 'email')

    def test_save(self):
        '''
        Test to save the credentials created for each user
        '''
        self.new_credent.save_credential()
        self.assertEqual(len(Credential.credent_list), 1)


if __name__ == '__main__':
    unittest.main()
