from user import User
from privilege import Privileges,Admin

new_users = Admin('Michael','Hawkes')
new_users.describe_user()
print(new_users.privileges.show_privileges())