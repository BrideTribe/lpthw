# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get a abbreivation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")

# study drills begins here
print('~' * 20)
print("STUDY DRILLS BEGINS HERE")

states = {
    'Ondo': 'OND',
    'Oyo': 'OYO',
    'Imo': 'IMO',
    'Ekiti': 'EKT',
    'Plateau': 'PLA',
    'Delta': 'DEL'
}

capital = {
    'OND': 'Akure',
    'OYO': 'Ibadan',
    'IMO': 'Owerri',
    'EKT': 'Ado-Ekiti',
    'PLA': 'Jos',
    'DEL': 'Asaba'
}

# print capital of some states
print('~' * 20)
print(f"OND State has: {capital['OND']}")
print(f"OYO State has: {capital['OYO']}")

# print out abbreviation of some states
print('~' * 20)
print(f"Plateau state's abbreviation is: {states['Plateau']}")
print(f"Delta state's abbreviation is: {states['Delta']}")

# print out abbreviation of all states
print('~' * 20)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print out the capital of states
print('~' * 20)
for abbrev, cap in list(capital.items()):
    print(f"{abbrev} has the capital {cap}")

# print out all the states, abbreviation and capitals
print('~' * 20)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated as {abbrev}")
    print(f"and its capital is {capital[abbrev]}\n")