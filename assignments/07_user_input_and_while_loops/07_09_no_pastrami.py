sandwich_orders = ['turkey','pastrami','ham','pastrami','tuna','italian','pastrami','cheesesteak']
finished_sandwiches = []

print('I am very sorry the deli is out of pastrami')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

while sandwich_orders:
    sandwiches = sandwich_orders.pop()

    print(f'Your {sandwiches} samdwich is ready!')
    finished_sandwiches.append(sandwiches)

print(f'\nThe following sandwiches have been made:')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)