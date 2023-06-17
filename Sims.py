from random import *
class Human:
    def __init__(self, name, job=None, home=None, car=None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.alive = True
    def get_home(self):
        self.home = House()
    def get_car(self):
        self.money -= 150
        self.gladness += 150
    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)
    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness
        self.satiety -= 5
    def shopping(self, manage):

    def chill(self):
        self.gladness += 5
        self.home.mess += 10
    def clean_house(self):
        self.gladness -= 10
        self.home.mess = 0
    def to_repair(self):
        self.car.speed += 7
        self.money -= 5
    def day_index(self, day):

    def is_alive(self):

    def(self, day):

class Auto:
    def __init__(self, brand_list):
        self.brand = choice(list (brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.speed = brand_list[self.brand]["speed"]
        self.consumption = brand_list[self.brand]["consumption"]
    def drive(self):
        if self.fuel >= self.consumption and self.speed > 0:
            self.fuel -= self.consumption
            self.speed -= 1
            return True
        else:
            print("The car cannot move...")
            return False
class Job:
    def __init__(self, job_list):
        self.job = choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness = job_list[self.job]["gladness"]
class House:
    def __init__(self):
        self.mess = 0
        self.food = 0
brands_of_car = {"BMW":{"fuels": 100, "speed": 100, "consumption": 6},
                 "Ferrari":{"fuels": 70, "speed": 300, "consumption": 20},
                 "Lada":{"fuels": 50, "speed": 40, "consumption": 20}}
job_list = {"IT":{"salary": 260, "gladness": -10},
            "Taxi":{"salary": 150, "gladness:": -25},
            "Waiter":{"salary": 90, "gladness": -20}}