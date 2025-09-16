'''I pasted my work from 3.10 to show the index error, the error that I did was in line 21.
It is an error because there are less than 6 items in the list and I am asking for it to print item 6
I had changed the code back to submit without the error'''

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