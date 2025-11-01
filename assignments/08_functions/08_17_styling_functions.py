def make_sandwich(*toppings):
    #This program makes a list of toppings for you to put on sandwiches
    print('\nThis sandwich has the following toppings:')
    for topping in toppings:
        print(f'- {topping}')

make_sandwich('lettuce','tomato')
make_sandwich('tomato','onion')
make_sandwich('lettuce','onion')


def describe_city(city_name,city_country='United States'):
    #This is a program that writes a sentence for where a city is
    print(f'\n{city_name.title()} is in {city_country.title()}')

describe_city('los angeles')
describe_city('new york city')
describe_city('tokyo','japan')


def make_shirt(shirt_size,shirt_message):
    #This program makes a sentence based on your shirt size and the message you want on it
    print(f'\nMy shirt size is {shirt_size} and I want this message on it: {shirt_message}')

make_shirt('Large','Peace and Love')
make_shirt(shirt_size = 'Extra Large',shirt_message = 'I dont want to taco bout it')