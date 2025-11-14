from city_functions import city_country 

while True:
    city = input('\nGive me a city name: ')
    if city.lower() == 'q':
        break
    country = input('Give me the name of the country the city is in: ')
    if country.lower() == 'q':
        break
    
    place = city_country(city, country)
    print(f'{place}')