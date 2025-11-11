from pathlib import Path 
import json

path = Path('favorite_number.json')
info = path.read_text()
favorite_number = json.loads(info)

print(f'I know your favorite number! Its {favorite_number}')