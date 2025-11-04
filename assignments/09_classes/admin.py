'''Used for 9.11 to store the classes that are imported'''
class User:
    '''A class that calls for the information of users'''
    
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
       
    def describe_user(self):
        print(f"\nThe users name is {self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"\nHello {self.first_name} {self.last_name}, thank you for joining")
    
user_1 = User('Patrick','Cruz')
user_1.describe_user()
user_1.greet_user()

user_2 = User('Mason','Florek')
user_2.describe_user()
user_2.greet_user()

class Privileges:

    def __init__(self,privileges=None):
        if privileges is None:
            privileges = []
        self.privileges = privileges
    
    def show_privileges(self):
        print('Admin privileges:')
        for privilege in self.privileges:
            print(f" {privilege}")

class Admin(User):

    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges= Privileges(['can add post',
                                     'can delete post','can ban user'])
        
admin_user = Admin('Brady','Etzkorn')
admin_user.describe_user()
admin_user.privileges.show_privileges()
