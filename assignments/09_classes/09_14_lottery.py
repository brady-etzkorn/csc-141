from random import choice
lottery = ['a','b','c','d','e','f','g','h','i','j',5,2,9,7,8]
winner = []

while len(winner) < 4:
    pick = choice(lottery)
    if pick not in winner:
        winner.append(pick)

print('Winning ticket:')
for item in winner:
    print(item)