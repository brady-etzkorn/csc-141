class Restaurant:
    '''An attempt to model a restaurant'''

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.customers = 0
    
    def describe_restaurant(self):
        print(f"The restaurant's name is {self.restaurant_name}")
        print(f"They serve mainly {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open for business!")
    
    def restaurant(self):
        print(f"There are {self.customers} customers at {self.restaurant_name}")

    def set_number_served(self,number):
        self.customers = number
    
    def increment_number_served(self,customers):
        self.customers += customers
        
        
my_restaurant = Restaurant('Pizza Hut','pizza')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant.customers = 15
my_restaurant.restaurant()

my_restaurant.set_number_served(25)
my_restaurant.restaurant()

my_restaurant.increment_number_served(200)
my_restaurant.restaurant()