# Exercise 7-4: Pizza Toppings
prompt = "\nEnter a pizza topping (type 'quit' when you are finished): "

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"I'll add {topping} to your pizza!")