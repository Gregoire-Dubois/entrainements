import xml.sax.xmlreader


class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 2000

    def get_descriptive_name(self):
        name=f"{self.make} {self.model} {self.year}"
        return (name.title())

    def update_ordometer(self, km):
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print('interdit')

    def increment_ordometer(self,km):
        self.odometer_reading += km

    def read_odometer(self, ):
        print(f"Cette voiture a {self.odometer_reading} km au compteur")

---------------------------

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"Le restaurant {self.restaurant_name} est spécialisé dans la cuisine {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Le restaurant {self.restaurant_name} est actuellement ouvert")

    def set_numbers_served(self, plates): #définir le nombrede clients servis
        self.number_served += plates

    def increment_number_served(self,):# incrément le nombre de client servis
        print(f"il a été servi au total {self.number_served}")

--------------------------------


class User:
    def __init__(self, first_name, last_name,age, city, login_attempts):
        self.first_name=first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"L'utilisateur s'appelle {self.first_name} {self.last_name}, il est agé de {self.age} ans et habite {self.city}")

    def greet_user(self):
        print(f"Bonjour {self.first_name} {self.last_name}, de {self.city}")

    def increment_login_attempts(self, connexion = 1): #incrémente la valeur de login_attempts de 1
        self.login_attempts += connexion
        print(f"Il y a eu {self.login_attempts} log")

    def reset_login_attempts(self): #réinitialise la valeur de login_attempts à 0
        self.login_attempts = 0
        print("Les logs sont effacés")

--------------------------------

class Car:
    def __init__(self, make, model, year, gaz):
        self.make = make
        self.model = model
        self.year = year
        self.ordometer = 0
        self.gaz = gaz


    def get_descriptive_name(self):
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name

    def read_ordometer(self):
        print(f"Cette voiture a {self.ordometer}")

    def update_ordometer(self, mileage):
        if mileage >= self.ordometer:
            self.ordometer = mileage
        else:
            print("il est interdit de trafiquer un compteur de voiture")

    def increment_ordemeter(self,mileage):
        self.ordometer += mileage


class Battery:
    def __init__(self, battery_size = 100):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"Cette voiture a une batterie de {self.battery_size} kwh")

    def get_range(self):
        if self.battery_size == 75 :
            range = 250
        elif self.battery_size == 100 :
            range = 315

        print(f"Avec une pleine charge le véhicule a une autonomie de {range} km")


class ElectricCar(Car):
    def __init__(self, make, model, year, gaz):
        super().__init__(make, model, year, gaz)
        self.battery = Battery()

    def gaz_tank(self):
        print("ce type de voiture n'a pas de réservoire à essence")

tesla = ElectricCar('Tesla', 'S', 2019,'essence')
print(tesla.get_descriptive_name())
tesla.gaz_tank()
tesla.battery.describe_battery()
tesla.battery.get_range()