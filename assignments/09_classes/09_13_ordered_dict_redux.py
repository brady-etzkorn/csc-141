import random

class Die:
    
    def __init__(self,sides=6):
        self.sides = sides
    
    def roll_die(self):
        return random.randint(1,self.sides)

print('Rolling a six-sided die:')
six_sided = Die()
for _ in range(10):
    print(six_sided.roll_die())

print('Rolling a ten-sided die:')
six_sided = Die(10)
for _ in range(10):
    print(six_sided.roll_die())

print('Rolling a twenty-sided die:')
six_sided = Die(20)
for _ in range(10):
    print(six_sided.roll_die())


