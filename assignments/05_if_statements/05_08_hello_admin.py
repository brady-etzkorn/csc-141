usernames = ['Frank','Charles','Janine','Lois','Admin']
for username in usernames:
    if username == 'Admin':
        print('Hello Admin would you like to see a status report?')
    else:
        print(f'Thank you for logging in {username}.')