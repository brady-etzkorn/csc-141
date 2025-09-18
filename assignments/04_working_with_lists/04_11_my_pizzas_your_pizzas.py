my_pizza = ['pepperoni','cheese','BBQ chicken','White']
friend_pizza = my_pizza[:]

my_pizza.append('Meatball')
friend_pizza.append('Veggie')

print('My favorite pizzas are:')
for pizza in my_pizza:
    print(pizza)
    
print('\n My friends favorite pizzas are:')
for pizza in friend_pizza:
    print(pizza)


