# Exercise 7-5: Movie Tickets
prompt = "\nPlease enter your age (type 'quit' to exit): "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    
    age = int(age)
    if age < 3:
        print("Your ticket is free!")
    elif age <= 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")