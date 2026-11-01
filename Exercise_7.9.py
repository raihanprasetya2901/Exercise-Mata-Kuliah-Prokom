# Exercise 7-9: No Pastrami
sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'chicken', 'pastrami', 'turkey']
print("Sorry, the deli has run out of pastrami.\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("Updated sandwich orders:", sandwich_orders)