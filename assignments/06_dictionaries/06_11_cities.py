cities = {'Chicago' : {'country' : 'US', 'population' : '2.72 million', 'fact' : 'famous for deep dish pizza'}, 'New York City' : {'country' : 'US', 'population' : '8.48 million', 'fact' : 'Originally called New Amsterdam'}, 'Los Angeles' : {'country' : 'US', 'population' : '3.88 million', 'fact' : 'Has one of the largest urban parks in the US'}}

for city, city_info in cities.items():
    print(f'\n{city}')
    country = f"{city_info['country']}"
    population = f"{city_info['population']}"
    fact = f"{city_info['fact']}"

    print(f'{country.title()}')
    print(f'{population.title()}')
    print(f'{fact.title()}')