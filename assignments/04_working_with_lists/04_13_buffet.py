buffet = ('chicken','potatoes','cake','fish','lobster')
print('Old Menu:')
for food in buffet:
    print(food)

#food[0]='ice cream' - this is what I had used to cause the intentional error

updated_menu =list(buffet)
updated_menu[0]='beef'
updated_menu[2]= 'ice cream'

buffet = tuple(updated_menu)

print('\nNew Menu:')
for menu in updated_menu:
    print(menu)

