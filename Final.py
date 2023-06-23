from random import *
class Waiter:
    def __init__(self, name, job=None):
        self.name = name
        self.cafe = job
        self.gladness = 50
        self.money = 50
        self.popularity = 0
        self.alive = True
    def get_job(self):
        self.cafe = Cafe()
    def work(self):
        if Customer == "Coffee":
            print("Customer wants cup of coffee...")
            self.money += 10
            self.popularity += 2
            self.cafe.mess += 5
            self.cafe.coffee -= 1
        if Customer == "Milk":
            print("Customer wants cup of milk...")
            self.money += 6
            self.popularity += 2
            self.cafe.mess += 3
            self.cafe.milk -= 1
        if Customer == "Double coffee":
            print("Customer wants cup of double coffee...")
            self.money += 20
            self.popularity += 2
            self.cafe.mess += 10
            self.cafe.coffee -= 2
        if Customer == "Coffee with milk":
            print("Customer wants cup of coffee with milk...")
            self.money += 16
            self.popularity += 2
            self.cafe.mess += 8
            self.cafe.coffee -= 1
            self.cafe.milk -= 1
        if Customer == "Coffee with sugar":
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
        print(f"Today the {day} of {self.name}'s life")
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
        if self.cafe is None:
            print("Getting a job...")
            self.get_job()
        self.day_index(day)
        dice = randint(1, 3)
        if self.cafe.coffee == 0 or self.cafe.milk == 0 or self.cafe.sugar == 0:
            self.shopping()
        if dice == 1:
            self.work()
        elif dice == 2:
            self.chill()
        elif dice == 3:
            self.cleaning()

class Cafe:
    def __init__(self):
        self.mess = 0
        self.coffee = 0
        self.milk = 0
        self.sugar = 0
class Customer:
    def __init__(self, drink_list):
        self.drink_C = choice(list(drink_list))
types_of_drink = {"Coffee", "Milk", "Double coffee", "Coffee with milk", "Coffee with sugar"}
Zaharij = Waiter("Zaharij")
for day in range(1, 31):
    if Zaharij.live(day) == False:
        print("Game Over!..")
        break