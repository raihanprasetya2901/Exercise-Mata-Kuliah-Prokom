# Exercise 3-5: Changing Guest List
guests = ['Agus', 'Budi', 'Ajeng']

cant_make_it = guests[2]
print(f"Maaf, {cant_make_it} tidak bisa hadir.")

# Mengganti tamu yang tidak hadir
guests[2] = 'Supri'

print(f"\nYth. {guests[0]}, Anda masih diundang untuk makan malam.")
print(f"Yth. {guests[1]}, Anda masih diundang untuk makan malam.")
print(f"Yth. {guests[2]}, Anda diundang untuk makan malam menggantikan tamu sebelumnya.")