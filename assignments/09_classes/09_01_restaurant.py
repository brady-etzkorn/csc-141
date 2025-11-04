class Restaurant:
    '''An attempt to model a restaurant'''

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"The restaurant's name is {self.restaurant_name}")
        print(f"They serve mainly {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open for business!")

my_restaurant = Restaurant('Pizza Hut','pizza')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

