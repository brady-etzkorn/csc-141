from admin import User,Privileges,Admin

new_admin = Admin('Ang','Allarde')
new_admin.describe_user()
print(new_admin.privileges.show_privileges())