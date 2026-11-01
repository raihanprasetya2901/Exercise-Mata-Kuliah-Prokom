# Exercise 8-16: Imports 
from printing_functions import send_messages as sm

messages = ["System updating...", "Reboot required", "All systems normal"]
sent = []

sm(messages[:], sent)

print("\nSent messages successfully:", sent)