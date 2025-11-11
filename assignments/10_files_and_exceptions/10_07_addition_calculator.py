print('Give me two numbers to add together.')
print('Enter "quit" to quit.')

while True:
    first_number = input('\nFirst number:')
    if first_number == 'quit':
        break 
    second_number = input('Second number: ')
    if second_number == 'quit':
        break
    try:
        total = int(first_number) + int(second_number)
    except ValueError:
        print("You can't input words")
    else:    
        print(total)