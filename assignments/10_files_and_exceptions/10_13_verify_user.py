from pathlib import Path 
import json

path = Path('user_info.json')

user_info = {}
user_info['name'] = input('What is your name? ')
user_info['age'] = input('How old are you? ')
user_info['school'] = input('What school do you go to? ')

path.write_text(json.dumps(user_info))

info = path.read_text()
load_info = json.loads(info)
print(load_info)