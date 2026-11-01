# Exercise 6-10: Favorite Numbers
favorite_numbers = {
    'andi': [7, 12],
    'siti': [14, 5, 8],
    'joko': [3],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")