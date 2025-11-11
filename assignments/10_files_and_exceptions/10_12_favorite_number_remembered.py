from pathlib import Path
import json

def get_stored_number(path):
    if path.exists():
        info = path.read_text()
        favorite_number = json.loads(info)
        return favorite_number
    else:
        return None

def store_number():
        favorite_number = input('\nFavorite number: ')
        info = json.dumps(favorite_number)
        path.write_text(info)
        print(f"We'll remember you favorite number is {favorite_number}")

path = Path('favorite_number.json')
favorite = get_stored_number(path)

if favorite:
     print(f'I know your favorite number its {favorite}')
store_number()