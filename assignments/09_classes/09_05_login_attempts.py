class User:
    '''A class that calls for the information of users'''
    
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login = 0
    
    def describe_user(self):
        print(f"\nThe users name is {self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"\nHello {self.first_name} {self.last_name}, thank you for joining")
    
    def login_attempts(self):
        print(f"There were {self.login} attempts to login.")
    
    def increment_login_attempts(self,users):
        self.login += users
    
    def reset_login_attempts(self,users):
        self.login -= users
    
user_1 = User('Patrick','Cruz')
user_1.describe_user()
user_1.greet_user()

user_2 = User('Mason','Florek')
user_2.describe_user()
user_2.greet_user()

user_1.increment_login_attempts(1)
user_1.login_attempts()

user_1.reset_login_attempts(1)
user_1.login_attempts()

user_1.increment_login_attempts(1)
user_1.login_attempts()