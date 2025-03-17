class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"\n{self.restaurant_name.title()} specializes on {self.cuisine_type} cuisine.")
    
    def open_restaurant(self):
        print(f"\n{self.restaurant_name.title()} is open!")

restaurant_wingstop = Restaurant('Wingstop','American')
restaurant_villa = Restaurant('Villa Pizza','Italian')
restaurant_morimoto = Restaurant('Morimoto','Japanese')

restaurant_wingstop.describe_restaurant()
restaurant_villa.describe_restaurant()
restaurant_morimoto.describe_restaurant()
