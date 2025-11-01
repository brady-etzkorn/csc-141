#used for 8.16

def make_album(artist,album_name,songs=None):
    #This function is used to present an album and its artist
    album = {'artist' : artist, 'album' : album_name}
    if songs:
        album['songs'] = songs
    return album