print('Give me two numbers to add together.')
print('Enter "quit" to quit.')

first_number = input('\nFirst number:')
    
second_number = input('Second number: ')
   
try:
    total = int(first_number) + int(second_number)
except ValueError:
    print("You can't input words")
else:    
    print(total)