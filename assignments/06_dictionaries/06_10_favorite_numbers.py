favorite_numbers = {'Patrick' : [35,5], 'Mason' : [25,15], 'Ang' : [6,8], 'Monica' : [67,54], 'Kate' : [5,9]}
for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"{number}")