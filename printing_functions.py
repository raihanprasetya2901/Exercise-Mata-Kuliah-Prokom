# Modul: printing_functions.py

def show_messages(messages):
    """Mencetak semua pesan yang ada di dalam list."""
    for msg in messages:
        print(f"Printing message: {msg}")

def send_messages(messages, sent_messages):
    """Simulasi pengiriman pesan dan memindahkannya ke list sent_messages."""
    while messages:
        current_msg = messages.pop(0)
        print(f"Sending message: {current_msg}")
        sent_messages.append(current_msg)