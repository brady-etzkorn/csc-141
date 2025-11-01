def make_album(artist,album_name,songs=None):
    #This program prints a dictionary of albums and their artists and can also tell you how many songs
    album = {'artist' : artist, 'album' : album_name}
    if songs:
        album['songs'] = songs
    return album

playlist_1 = make_album('radiohead','OK computer')
print(playlist_1)

playlist_2 = make_album('the strokes','is this it')
print(playlist_2)

playlist_3 = make_album('vacations','changes',songs = '10')
print(playlist_3)