class Credential:
    """
    Class that generates new instances of credentials
    """

    credential_list = []  # Empty contact list
    # Init method up here

    def save_credential(self):
        '''
        save_credential method saves credential objects into credntial_list
        '''

        Credential.credential_list.append(self)

    def __init__(self, login_name, user_password, user_account):

        # docstring removed for simplicity

        self.login_name = login_name
        self.user_password = user_password
        self.user_account = user_account
