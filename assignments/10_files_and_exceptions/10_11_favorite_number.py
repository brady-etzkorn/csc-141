from pathlib import Path
import json

favorite_number = input('\nFavorite number: ')

path = Path('favorite_number.json')
info = json.dumps(favorite_number)
path.write_text(info)

print(f"We'll remember you favorite number is {favorite_number}")