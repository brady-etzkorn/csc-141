def build_profile(first, last, **user_info):
    #This program is to present a list of information of a person
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('brady', 'etzkorn',location='albright',field='game and sim',sport='lax')
print(user_profile)