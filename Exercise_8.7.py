# Exercise 8-7: Album
def make_album(artist, title, songs=None):
    album = {'artist': artist.title(), 'title': title.title()}
    if songs:
        album['songs'] = songs
    return album

print(make_album('adele', '25'))
print(make_album('taylor swift', '1989', songs=16))