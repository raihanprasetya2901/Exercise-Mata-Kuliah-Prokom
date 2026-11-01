# Exercise 8-15: Printing Models (Importing an Entire Module)
import printing_functions

# Menyiapkan data
unprinted_messages = ["Hello there!", "How are you?", "Keep learning Python!"]
sent_messages = []

# Memanggil fungsi menggunakan nama modul (dot notation)
printing_functions.send_messages(unprinted_messages[:], sent_messages)

print("\n--- Hasil Akhir ---")
print("Unprinted:", unprinted_messages)
print("Sent:", sent_messages)