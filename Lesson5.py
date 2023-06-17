class Human:
    def __init__(self, name):
        self.name = name
class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passenger = []
    def add_passenger(self, *args):
        for passenger in args:
            self.passenger.append(passenger)
    def print_passenger_names(self):
        if self.passenger != []:
            print(f"Names of {self.brand} passengers:")
            for passenger in self.passenger:
                print(passenger.name)
        else:
                print(f"There are no passenger in {self.brand}")
Zaharij = Human("Zaharij")
Nazar = Human("Nazar")
Jevgen = Human("Jevgen")
Sergij = Human("Sergij")
car = Auto("Ferrari")
car.add_passenger(Nazar, Zaharij)
car.print_passenger_names()
car2 =Auto("BMW")
car2.add_passenger(Jevgen, Sergij)
car2.print_passenger_names()