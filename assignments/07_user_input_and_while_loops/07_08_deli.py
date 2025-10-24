sandwich_orders = ['turkey','ham','tuna','italian','cheesesteak']
finished_sandwiches = []

while sandwich_orders:
    sandwiches = sandwich_orders.pop()

    print(f'Your {sandwiches} samdwich is ready!')
    finished_sandwiches.append(sandwiches)

print(f'\nThe following sandwiches have been made:')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
    
