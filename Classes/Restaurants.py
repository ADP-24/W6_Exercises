class Restaurant:
# A class to represent a restaurant, storing its name and the type of food it serves.
    def __init__(self, rest_name, food_type):

        self.rest_name = rest_name
        self.food_type = food_type
    
# Initalize the restaurant with a name and type of food
    def describe_rest(self):

        print(f"{self.rest_name} serves {self.food_type}")

    def rest_open(self):
        
        print(f"{self.rest_name} is open")

Restaurant1 = Restaurant("McDonalds", "thee Big Mac")
Restaurant2 = Restaurant("Burger King", "thee Whopper")
Restaurant3 = Restaurant("Wendys", "thee Frosty")

Restaurant1.describe_rest()
Restaurant1.rest_open()

print()

Restaurant2.describe_rest()
Restaurant2.rest_open() 

print()

Restaurant3.describe_rest()
Restaurant3.rest_open()