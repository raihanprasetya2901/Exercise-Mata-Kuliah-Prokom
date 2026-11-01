# Exercise 7-6: Three Exits
prompt = "\nEnter your age: "
active = True

while active:
    age = input(prompt)
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print("Free ticket.")
        elif age <= 12:
            print("Ticket is $10.")
        else:
            print("Ticket is $15.")