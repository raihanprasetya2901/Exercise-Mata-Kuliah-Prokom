# Exercise 8-11: Archived Messages

# 1. Definisikan dulu fungsinya di bagian atas
def send_messages(messages, sent_messages):
    """Simulasi pengiriman pesan dan memindahkannya ke list sent_messages."""
    while messages:
        current_msg = messages.pop(0)
        print(f"Sending message: {current_msg}")
        sent_messages.append(current_msg)

# 2. Siapkan list awal
messages = ["Hello there!", "How are you?", "Keep learning Python!"]
sent_messages = []

# 3. Kirim salinan list menggunakan slice [:] agar list asli tidak kosong
send_messages(messages[:], sent_messages)

# 4. Cetak untuk membuktikan list asli aman dan list tujuan terisi
print("\nOriginal list (retained):", messages)
print("Sent list:", sent_messages)