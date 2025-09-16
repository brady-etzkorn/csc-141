star_wars=['X-wing','Y-wing','A-wing','Tie fighter']
star_wars[0]='Millenium Falcon'
star_wars.append('B-wing')
star_wars.insert(2,'Venator')
del star_wars[1]
destroied_ship = star_wars.pop()
star_wars.sort()

print(star_wars)
print(destroied_ship)
star_wars.remove('Tie fighter')
print(star_wars)
print(sorted(star_wars, reverse=True))

star_wars.reverse
print(star_wars)

message = f'My favorite Star Wars ship is {star_wars[0].title()}'
print(star_wars[1])
print(message)

print (len(star_wars))