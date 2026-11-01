# Exercise 8-10: Sending Messages
def send_messages(messages, sent_messages):
    while messages:
        current_msg = messages.pop(0)
        print(f"Sending message: {current_msg}")
        sent_messages.append(current_msg)

messages = ["Hello there!", "How are you?", "Keep learning Python!"]
sent_messages = []

send_messages(messages, sent_messages)
print("\nOriginal list:", messages)
print("Sent list:", sent_messages)