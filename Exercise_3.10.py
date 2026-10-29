# Exercise 3-10: Every Function
languages = ['Python', 'Java', 'C++', 'JavaScript', 'Ruby']

print("Daftar Awal:", languages)
print("Akses elemen:", languages[0])

languages[4] = 'Go'
print("Setelah diubah:", languages)

languages.append('Rust')
languages.insert(1, 'HTML')
print("Setelah append & insert:", languages)

del languages[1]
popped_lang = languages.pop()
languages.remove('Java')
print(f"Bahasa yang di-pop: {popped_lang}")
print("Setelah del, pop, & remove:", languages)

print("Sorted sementara:", sorted(languages))
languages.reverse()
print("Setelah reversed():", languages)

languages.sort()
print("Sorted permanen:", languages)
print("Jumlah bahasa:", len(languages))