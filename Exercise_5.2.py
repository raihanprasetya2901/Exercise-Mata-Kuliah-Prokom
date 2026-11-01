# Exercise 5-2: More Conditional Tests
# Tes kesamaan dan ketidaksamaan dengan string
string_1 = "Python"
string_2 = "python"
print(string_1 == string_2)  # False
print(string_1 != string_2)  # True

# Tes menggunakan metode lower()
print(string_1.lower() == string_2)  # True

# Tes numerik
age_0 = 20
age_1 = 25
print(age_0 >= 18)  # True
print(age_1 < 21)   # False

# Tes menggunakan and dan or
print((age_0 >= 18) and (age_1 >= 18))  # True
print((age_0 > 25) or (age_1 > 20))    # True

# Tes item in / not in list
toppings = ['mushrooms', 'cheese', 'onions']
print('cheese' in toppings)      # True
print('pepperoni' in toppings)   # False