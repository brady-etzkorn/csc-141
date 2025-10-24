users = {'aeinstein': {'first': 'albert','last': 'einstein','location': 'princeton',},'mcurie': {'first': 'marie','last': 'curie','location': 'paris'},'kornboy' : {'first' : 'brady','last' : 'etzkorn','location' : 'pennsylvania'}}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\n There full name is {full_name.title()} and they are from {location.title()}")