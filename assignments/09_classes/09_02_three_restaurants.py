class Restaurant:
    '''An attempt to model a restaurant'''

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"\nThe restaurant's name is {self.restaurant_name}")
        print(f"They serve mainly {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open for business!")

restaurant = Restaurant('Pizza Hut','pizza')
restaurant.describe_restaurant()

restaurant_2 = Restaurant('Taco Bell','mexican')
restaurant_2.describe_restaurant()

restaurant_3 = Restaurant('Chick-Fila','chicken')
restaurant_3.describe_restaurant()
