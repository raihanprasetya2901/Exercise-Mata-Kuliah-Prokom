# Exercise 6-6: Polling
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

people_to_poll = ['jen', 'phil', 'budi', 'siti', 'sarah']

for person in people_to_poll:
    if person in favorite_languages.keys():
        print(f"Thank you {person.title()}, for taking the poll.")
    else:
        print(f"Hello {person.title()}, please take our poll!")