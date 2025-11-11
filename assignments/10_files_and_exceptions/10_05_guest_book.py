from pathlib import Path 

path = Path('10_files_and_exceptions/guest_book.txt')

guests = []

while True:
    guest_book = input('What is your name? \n')
    if guest_book.strip().lower() == 'quit':
        break
    guests.append(guest_book)

guest_entries = ""
for guest in guests:
    guest_entries += f"{guest} has visited. \n"
 

path.write_text(guest_entries)