class Car:
    def __init__(self, color, brand, year):
        self.color=color
        self.brand = brand
        self.year = year

    def displayDeatais(self):
        print("I am looking to sell my {} colour {} made in year {}".format(self.color,self.brand,self.year))

            
#child class
class Suv(Car):
    def __init__(self, color, brand, year, fuel_type):
        Car.__init__(self, color,brand, year)
        self.fuel_type=fuel_type
    def displayDeatails(self):
        print("I am looking to sell my {} {} colour {} made in year {}".format(self.fuel_type, self.color,self.brand,self.year))
    


SUV = Suv("black", "mercedes", "2023","diesel")

SUV.displayDeatails()


