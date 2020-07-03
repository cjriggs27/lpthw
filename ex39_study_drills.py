states = {
  'Virginia' : 'VA',
  'Alabama' : 'AL',
  'Illinois' : 'IL'
}

states['Georgia'] = 'GA'

cities = {
    'VA' : 'Richmond',
    'AL' : 'Montgomery',
    'IL' : 'Chicago'
}

cities['GA'] = 'Atlanta'

# print the cities by abbreviation
print("The city that is also the capital of Virginia is", cities['VA'])
print("Illinois has the city", cities['IL'])

# print abbreviations for states
print('-' * 30)
print("The abbreviation for the state of Virginia is", states['Virginia'])
print("The abbreviation for the state of Alabama is", states['Alabama'])
print("The abbreviation for the state of Illinois is", states['Illinois'])
print("The abbriviation for the state of Georgia is", states['Georgia'])

# print cities layerign dict refferences
print('-' * 30)
print("Virginia has:", cities[states['Virginia']])
print("Alabama has:", cities[states['Alabama']])
print("Illinois has:", cities[states['Illinois']])
print("Georgia has:", cities[states['Georgia']])

# print states and abbreviations using f refferences
print('-' * 30)
for state, abbreviation in list(states.items()):
    print(f"The state of {state} is abbreviated {abbreviation}")

# print abbreviations and cities using f refferences
print('-' * 30)
for abbreviation, city in list(cities.items()):
    print(f"{abbreviation} has the city {city}")
