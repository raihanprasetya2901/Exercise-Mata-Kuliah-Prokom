# Exercise 6-9: Favorite Places
favorite_places = {
    'andi': ['bali', 'bandung', 'lombok'],
    'siti': ['yogyakarta', 'malang'],
    'budi': ['raja ampat']
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t- {place.title()}")