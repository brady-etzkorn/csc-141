'''Used to store the user class for 9.12'''

class User:
    '''A class that calls for the information of users'''
    
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
       
    def describe_user(self):
        print(f"\nThe users name is {self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"\nHello {self.first_name} {self.last_name}, thank you for joining")
    