# Exercise 8-8: User Albums
def make_album(artist, title):
    return {'artist': artist.title(), 'title': title.title()}

while True:
    print("\nEnter artist and album title (enter 'q' to quit):")
    artist = input("Artist: ")
    if artist == 'q':
        break
    title = input("Title: ")
    if title == 'q':
        break
    
    album = make_album(artist, title)
    print("Created album dictionary:", album)