# Exercise 3-7: Shrinking Guest List
guests = ['Yanto', 'Yanti', 'Tino', 'Tina', 'Dono', 'Doni']

print("Mohon maaf, meja baru tidak sampai tepat waktu. Saya hanya bisa mengundang dua orang.\n")

popped_guest = guests.pop()
print(f"Maaf {popped_guest}, saya tidak bisa mengundang Anda ke makan malam.")

popped_guest = guests.pop()
print(f"Maaf {popped_guest}, saya tidak bisa mengundang Anda ke makan malam.")

popped_guest = guests.pop()
print(f"Maaf {popped_guest}, saya tidak bisa mengundang Anda ke makan malam.")

popped_guest = guests.pop()
print(f"Maaf {popped_guest}, saya tidak bisa mengundang Anda ke makan malam.")

print(f"\nYth. {guests[0]}, Anda masih diundang untuk makan malam!")
print(f"Yth. {guests[1]}, Anda masih diundang untuk makan malam!")

del guests[0]
del guests[0]

print("\nDaftar tamu akhir:", guests)