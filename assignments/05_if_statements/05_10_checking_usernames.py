current_users = ['John','Mike','Pat','Mason','Charles']
new_users = ['Kate','John','Tyler','Mike','Hank']
for new_user in new_users:
    if new_user in current_users:
        print('You will need to enter a new username')
    else:
        print('That username is available')