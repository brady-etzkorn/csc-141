car = 'Subaru'
print(car.lower() == 'subaru')
print(car.lower() == 'audi')

age = '18'
print(age == '18')
print(age == '21')
print(age < '22')
print(age > '23')
print(age <= '23')
print(age >= '21')

age_0 = '19'
age_1 = '21'
print(age_0 >= '19' and age_1 <= '21')
print(age_0 == '18' or age_1 == '22')

games = ['GTA', 'Fortnite', 'Rocket League']
print('GTA' in games)
print('God of War' in games)