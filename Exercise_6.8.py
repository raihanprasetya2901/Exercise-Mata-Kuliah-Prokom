# Exercise 6-8: Pets
pet_1 = {'kind': 'cat', 'owner': 'andi'}
pet_2 = {'kind': 'dog', 'owner': 'budi'}
pet_3 = {'kind': 'rabbit', 'owner': 'siti'}

pets = [pet_3, pet_2, pet_1]

for pet in pets:
    print(f"\nKind of animal: {pet['kind'].title()}")
    print(f"Owner: {pet['owner'].title()}")