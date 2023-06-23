from random import *
class Waiter:
    def __init__(self, name, job=None, customer=None):
        self.name = name
        self.cafe = job
        self.gladness = 50
        self.money = 50
        self.popularity = 10
        self.customer = customer
        self.alive = True
    def get_customer(self):
        self.customer = Customer(types_of_drink)
    def get_job(self):
        self.cafe = Cafe()
    def work(self):
        if self.customer.drink == "Coffee":
            print("Customer wants cup of coffee...")
            self.money += 10
            self.popularity += 2
            self.cafe.mess += 5
            self.cafe.coffee -= 1
        if self.customer.drink == "Milk":
            print("Customer wants cup of milk...")
            self.money += 6
            self.popularity += 2
            self.cafe.mess += 3
            self.cafe.milk -= 1
        if self.customer.drink == "Double coffee":
            print("Customer wants cup of double coffee...")
            self.money += 20
            self.popularity += 2
            self.cafe.mess += 10
            self.cafe.coffee -= 2
        if self.customer.drink == "Coffee with milk":
            print("Customer wants cup of coffee with milk...")
            self.money += 16
            self.popularity += 2
            self.cafe.mess += 8
            self.cafe.coffee -= 1
            self.cafe.milk -= 1
        if self.customer.drink == "Coffee with sugar":
            print("Customer wants cup of coffe with sugar...")
            self.money += 26
            self.popularity += 2
            self.cafe.mess += 13
            self.cafe.coffee -= 1
            self.cafe.sugar -= 1
    def chill(self):
        if self.cafe.mess >= 30:
            print("Time to chill, but I can't chill, it's dirty here...")
            self.cleaning()
        else:
            print("Time to chill...")
            self.gladness += 15
            self.popularity -= 5
    def cleaning(self):
        if self.cafe.mess <= 0:
            print("Time to cleaning, but I don't need cleaning, it's clean here...")
            pass
        else:
            print("Time to cleaning...")
            self.cafe.mess -= 8
            self.gladness -= 5
            self.popularity += 3
    def shopping(self):
        print("Time to shopping...")
        self.gladness -= 14
        self.money -= 24
        self.cafe.coffee += 4
        self.cafe.milk += 2
        self.cafe.sugar += 1
    def day_index(self, day):
        print("-"*100)
        print(f"Today the {day} of {self.name}'s life")
        print("-"*100)
        print(f"Money - {self.money}")
        print(f"Gladness - {self.gladness}")
        print(f"Popularity - {self.popularity}")
        print(f"Mess - {self.cafe.mess}")
        print(f"Coffee - {self.cafe.coffee}")
        print(f"Milk - {self.cafe.milk}")
        print(f"Sugar - {self.cafe.sugar}")
    def is_alive(self):
        if self.money <= -50:
            print("I have no money...")
            self.alive = False
        if self.gladness <= 0:
            print("Stressed out...")
            self.alive = False
        if self.popularity < 0:
            print("No customers...")
            self.alive = False
    def live(self, day):
        if self.customer is None:
            print("Get order...")
            self.get_customer()
        if self.cafe is None:
            print("Getting a job...")
            self.get_job()
        self.day_index(day)
        dice = randint(1, 3)
        if self.cafe.coffee == 0 or self.cafe.milk == 0 or self.cafe.sugar == 0:
            self.shopping()
        if dice == 1:
            print("Working...")
            self.work()
        elif dice == 2:
            self.chill()
        elif dice == 3:
            self.cleaning()
        self.is_alive()
class Cafe:
    def __init__(self):
        self.mess = 0
        self.coffee = 0
        self.milk = 0
        self.sugar = 0
class Customer:
    def __init__(self, drink_list):
        self.drink = choice(list(drink_list))
types_of_drink = {"Coffee", "Milk", "Double coffee", "Coffee with milk", "Coffee with sugar"}
Zaharij = Waiter("Zaharij")
for day in range(1, 31):
    if Zaharij.alive == False:
        print("Game Over!..")
        break
    Zaharij.live(day)
Zaharij.day_index(None)