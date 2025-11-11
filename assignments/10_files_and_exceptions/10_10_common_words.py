from pathlib import Path 

path = Path('10_files_and_exceptions/gutenberg.txt')
word_to_count = 'the'
try:
    file = path.read_text()
    word = file.lower().count('the ')
   
    print(f'The word "{word_to_count}" appears about {word} times.')
except FileNotFoundError:
    print(f'Sorry the file {path} was not found')

