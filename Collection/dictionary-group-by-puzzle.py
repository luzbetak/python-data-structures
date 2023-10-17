from collections import defaultdict

city_list = [('TX', 'Austin'),
             ('TX', 'Houston'),
             ('NY', 'Albany'),
             ('NY', 'Syracuse'),
             ('NY', 'Buffalo'),
             ('NY', 'Rochester'),
             ('TX', 'Dallas'),
             ('CA', 'Sacramento'),
             ('CA', 'Palo Alto'),
             ('GA', 'Atlanta')]

# Group By using dictionary
cities_by_state = defaultdict(list)
for state, city in city_list:
    cities_by_state[state].append(city)

for state, cities in cities_by_state.items():
    print(state, ":",  ', '.join(cities))

