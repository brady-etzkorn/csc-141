import music 
album = music.make_album('tyler the creator','earthquake')
print(album)

from music import make_album 
album1 = make_album('radiohead', 'ok computer')
print(album1)

from music import make_album as ma
album2 = ma('Ole 60','songs about you')
print(album2)

import music as m
album3 = m.make_album('train','drops of jupiter')
print(album3)

from music import *
album4 = make_album('coldplay','parachutes')
print(album4)
