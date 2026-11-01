# Exercise 6-11: Cities
cities = {
    'surakarta': {
        'country': 'indonesia',
        'population': '522,000',
        'fact': 'Known as Solo and famous for batik.'
    },
    'tokyo': {
        'country': 'japan',
        'population': '14 million',
        'fact': 'One of the most populous metropolitan areas in the world.'
    },
    'paris': {
        'country': 'france',
        'population': '2.1 million',
        'fact': 'Famous for the Eiffel Tower.'
    }
}

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"\tCountry: {info['country'].title()}")
    print(f"\tPopulation: {info['population']}")
    print(f"\tFact: {info['fact']}")