favorite_language = {'jen' : 'python', 'edward' : 'rust', 'pat' : 'c'}
for name, value in favorite_language.items():
    print(f"\n{name.title()}, thank you for taking your poll")

if 'mason' not in favorite_language.keys():
    print("\nMason, please take the poll") 