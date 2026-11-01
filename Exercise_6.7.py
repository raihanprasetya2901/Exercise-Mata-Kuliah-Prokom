# Exercise 6-7: People
person_1 = {'first_name': 'Budi', 'last_name': 'Santoso', 'age': 20, 'city': 'Surakarta'}
person_2 = {'first_name': 'Siti', 'last_name': 'Aminah', 'age': 22, 'city': 'Yogyakarta'}
person_3 = {'first_name': 'Joko', 'last_name': 'Widodo', 'age': 25, 'city': 'Boyolali'}

people = [person_1, person_2, person_3]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"\nName: {full_name}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")