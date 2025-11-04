'''used for 9.10 as a way to store the classes for restaurants'''
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

class IceCreamStand(Restaurant):
    ''' Subclass for an ice cream stand to show its flavors'''

    def __init__(self,restaurant_name,cuisine_type):
        '''Initializes attributes from the parent class'''
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['chocolate','vanilla','strawberry']
    def flavors_menu(self):
        '''Prints a statement that lists the menu'''
        print(f'The flavors are {self.flavors}')
my_stand = IceCreamStand('Dairy Queen','ice cream')
print(my_stand.describe_restaurant())
my_stand.open_restaurant()
my_stand.flavors_menu()