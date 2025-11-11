from pathlib import Path 


guest_book = input('What is your name? ')
 
path = Path('10_files_and_exceptions/guests.txt')
path.write_text(guest_book)