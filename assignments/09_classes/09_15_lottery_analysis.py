from random import choice
lottery = ['a','b','c','d','e','f','g','h','i','j',5,2,9,7,8]
winner = ['a',9,'c',2]

def generate_ticket():
    ticket = []
    while len(ticket) < 4:
        pick = choice(lottery)
        if pick not in ticket:
            ticket.append(pick)
    return ticket

attempts = 0
while True:
    attempts += 1
    my_ticket = generate_ticket()
    if set(my_ticket) == set(winner):
        break

print(f'It took {attempts} to win')


    
