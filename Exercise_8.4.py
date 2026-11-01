# Exercise 8-4: Large Shirts
def make_shirt(size='large', text='I love Python'):
    print(f"Creating a {size}-inch t-shirt with the message: '{text}'.")

make_shirt()  # Default large & message
make_shirt(size='medium')  # Default message
make_shirt(size='small', text='Keep Coding.')