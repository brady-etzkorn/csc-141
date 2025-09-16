dinner_party = ['George Washington', 'David Njoku', 'Jalen Ramsey']
dinner_party.insert(0, 'Juan Soto')
dinner_party.insert(2, 'Aaron Rodgers')
dinner_party.append('DK Metcalf')
not_invited = dinner_party.pop(0)
not_invited1 = dinner_party.pop(1)
not_invited2 = dinner_party.pop(3)
not_invited3 = dinner_party.pop(2)

                
print(dinner_party)

print('Unfortunately the big table that I ordered will not come in time, and I can only invite two of you')

print(not_invited,',I am sorry you are not invited')
print(not_invited1,',I am sorry you are not invited')
print(not_invited2,',I am sorry you are not invited')
print(not_invited3,',I am sorry you are not invited')

message = f'Do not worry you are still invited {dinner_party[0].title()}'
message1 = f'Do not worry you are still invited {dinner_party[1].title()}'

print (message)
print (message1)

del dinner_party[1]
del dinner_party[0]
print(dinner_party)


