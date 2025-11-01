def make_sandwich(*toppings):
    #This program gives a list of what people ordered on their sandwiches
    print('\nThis sandwich has the following toppings:')
    for topping in toppings:
        print(f'- {topping}')

make_sandwich('lettuce','tomato')
make_sandwich('tomato','onion')
make_sandwich('lettuce','onion')