class Credential:

    """
    class that creates a new credential(cred)
    """
    credent_list=[]

def __init__(self,username,password,account):
    '''
    class for credentials
    '''
    self.username=username
    self.password=password
    self.account=account

def save_credential(self):
    '''
    class method to save the credentials
    '''
    Credential.credent_list.append(self)
    return self.credent_list
