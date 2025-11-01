def describe_city(city_name,city_country = 'United States'):
    #This program is used to show a city and the country it is in 
    print(f'\n{city_name.title()} is in {city_country.title()}')

describe_city('los angeles')
describe_city('new york city')
describe_city('tokyo','japan')