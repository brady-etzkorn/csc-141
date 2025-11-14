def city_country(city, country, population=None):
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"
    

from city_functions import city_country

def test_city_country():
    formatted = city_country('Toyko', 'Japan')
    assert formatted == 'Toyko Japan'

def test_city_population():
    formatted = city_country('toyko', 'japan', population = 123000200)
    assert formatted == 'Toyko, Japan - population 123000200'