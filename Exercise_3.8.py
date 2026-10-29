# Exercise 3-8: Seeing the World
locations = ['Salatiga', 'Jogja', 'Solo', 'Klaten', 'Sukoharjo']

print("Original order:", locations)
print("Alphabetical order:", sorted(locations))
print("Original order after sorted():", locations)
print("Reverse alphabetical order:", sorted(locations, reverse=True))
print("Original order after sorted(reverse=True):", locations)

locations.reverse()
print("Reversed order:", locations)

locations.reverse()
print("Back to original order:", locations)

locations.sort()
print("Sorted alphabetically:", locations)

locations.sort(reverse=True)
print("Sorted reverse alphabetically:", locations)