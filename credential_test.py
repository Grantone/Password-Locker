import unittest
from credential import Credential

class TestUser(unittest.TestCase):
    '''
    Class to test the functionality of the credentials
    '''
def setUp(self):
    '''
    setUp method to test if the creentials run
    '''
    self.new_credent = Credential
    ('Mchana', 'q1234', 'email') # create acredential object

def test_init(self):
    '''
    credentials objects initialization
    '''
    self.assertEqual(self.new_credent.username,'Mchana')
    self.assertEqual(self.new_credent.password,'q1234')
    self.assertEqual(self.new_credent.account,'email')
def test_save(self):
    '''
    class for saving credentials
    '''
    self.new_credent.save_credential()
    self.assertEqual(len(Credential.credent_list),1)

if __name__=='__main__':
    unittest.main()
