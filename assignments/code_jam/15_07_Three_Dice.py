from random import randint

class Die:

    def __init__(self, num_sides=6):
        self.num_sides = num_sides
    
    def roll(self):
        return randint(1, self.num_sides)
    
import matplotlib.pyplot as pl

die = Die()
die_2 = Die()
die_3 = Die()

results = [die.roll() + die_2.roll() + die_3.roll() for _ in range(1000)]

max_result = die.num_sides + die_2.num_sides + die_3.num_sides
frequencies = [results.count(value) for value in range(3, max_result + 1)]

pl.style.use('classic')
fig, ax = pl.subplots(figsize=(10, 6))
ax.bar(range(3, max_result +1), frequencies, color='lightblue', edgecolor = 'black')

ax.set_xticks(range(3, max_result + 1))

pl.show()