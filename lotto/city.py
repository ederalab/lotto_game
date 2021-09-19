class City:
    """
    This class defines the name of the cities (in italian "ruote") that can be chosen from the user
    The possible cities are:
    Bari - Cagliari - Firenze - Genova - Milano - Napoli - Palermo - Roma - Torino - Venezia - Tutte
    pay attention to the possibility of error from the user!
    """
    cities = ["BARI", "CAGLIARI", "FIRENZE", "GENOVA", "MILANO", "NAPOLI", "PALERMO", "ROMA", "TORINO", "VENEZIA", "TUTTE"]

    def __init__(self, city):
        self.city = city
        if self.is_city_valid(city):
            city.__str__()

    def is_city_valid(self, city):
        if city.strip().upper() in City.cities:
            return True

    def __str__(self):
        if self.is_city_valid(self.city):
            return self.city.strip().upper()
        else:
            return "The city is not valid"


# TEST #
if __name__ == "__main__":
    usr_city = input("Insert the name of the city: ")
    mycity = City(usr_city)
    print(mycity.__str__())
