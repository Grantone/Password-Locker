class Credential:

    """
    class that creates a new credential(cred)
    """
    credent_list=[]

def __init__(self,username,password,account):
    '''
    define the properties of the class
    '''
    self.username=username
    self.password=password
    self.account=account

def save_credential(self):
    '''
    method to save the credentials inputted
    '''
    Credential.credent_list.append(self)
    return self.credent_list
