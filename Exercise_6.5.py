# Exercise 6-5: Rivers
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nSungai yang ada di dictionary:")
for river in rivers.keys():
    print(river.title())

print("\nNegara yang ada di dictionary:")
for country in rivers.values():
    print(country.title())