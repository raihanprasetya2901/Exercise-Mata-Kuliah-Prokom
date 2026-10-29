# Exercise 4-13: Buffet
foods = ('nasi goreng', 'mie ayam', 'sate', 'bakso', 'soto')

print("Menu asli restoran:")
for food in foods:
    print(food)

# Baris di bawah akan error jika di-uncomment karena tuple tidak bisa diubah:
# foods[0] = 'bubur ayam'

# Menulis ulang tuple dengan menu baru
foods = ('nasi goreng', 'mie ayam', 'sate', 'pecel', 'gado-gado')
print("\nMenu yang direvisi:")
for food in foods:
    print(food)