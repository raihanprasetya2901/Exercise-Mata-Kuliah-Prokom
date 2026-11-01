# Exercise 8-12: Sandwiches
def make_sandwich(*items):
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

make_sandwich('cheese', 'tomato')
make_sandwich('turkey', 'lettuce', 'mayo')
make_sandwich('peanut butter', 'jelly')