# Exercise 4-11: My Pizzas, Your Pizzas
my_pizzas = ['pepperoni', 'meatlovers', 'cheese']
friend_pizzas = my_pizzas[:]

my_pizzas.append('hawaiian')
friend_pizzas.append('veggie')

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)