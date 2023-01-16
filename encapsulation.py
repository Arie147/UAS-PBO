class Car:
    def __init__(self):
        self.__make = "Toyota"
        self.__year_model = 2020
        self.__speed = 0

    def set_make(self, make):
        self.__make = make

    def set_year_model(self, year):
        self.__year_model = year

    def set_speed(self, speed):
        self.__speed = 0

    def get_make(self):
        return self.__make

    def get_year_model(self):
        return self.__year_model

    def get_speed(self):
        return self.__speed

my_car = Car()
print(my_car.get_make())