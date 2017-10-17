from credential import Credential


class User:
    """
    A class for user credentials
    """
    users_list = []
    user_credentials = []

    def __init__(self, username, userpassword):
        '''
        Properties of the user
        '''
        self.username = username
        self.userpassword = userpassword

    def register(self):
        '''
        Method that saves a new credentials created by new user
        '''
        User.users_list.append(self)

    @classmethod
    def save_credent_user(cls, credent):
        '''
        An instance to save a credential for a user
        '''

    @classmethod
    def login_checker(cls, username, userpassword):
        '''
        Method that confirms the entry of the user if already registered and then allows him/her to log in
        '''
        for user in User.users_list:
            if user.username == username and user.userpassword == userpassword:
                return user
        return False

    @classmethod
    def display_users(cls):
        return cls.users_list
