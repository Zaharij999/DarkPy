from random import *
class Waiter:
    def __init__(self, name, gladness, money, popularity):
        self.name = name
        self.gladness = 50
        self.money = 100
        self.popularity = 0
        self.alive = True
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
            print("Customer wants cup of coffee wit milk...")
            self.money += 16
            self.popularity += 2
            self.cafe.mess += 8
            self.cafe.coffee -= 1
            self.cafe.milk -= 1
        if Customer == "Coff"
    def chill(self):

    def cleaning(self):

    def shopping(self):

class Cafe:
    def __init__(self):
        self.mess = 0
        self.coffee = 0
        self.milk = 0
        self.sugar = 0
class Customer:
    def __init__(self, types_of_drink_C):
        self.drink_C = choice(list(types_of_drink_C))
types_of_drink_C = {"Coffee", "Milk", "Double coffee", "Coffee with milk", "Coffee with sugar"}
types_of_drink_W = {"Coffee", "Milk", "Double coffee", "Coffee with milk", "Coffee with sugar"}