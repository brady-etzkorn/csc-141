def make_album(artist,album_name):
    #This program prints a dictionary of albums and their artists
    album = {'artist' : artist, 'album' : album_name}
    return album 

while True:
    print("\nEnter album details or 'q' to quit:")
    
    artist = input("Artist name: ")
    if artist.lower() == 'q':
        break
    album_name = input("Album title: ")
    if album_name.lower() == 'q':
        break
    album = make_album(artist,album_name)
    print(f"Added to playlist: {album}")


