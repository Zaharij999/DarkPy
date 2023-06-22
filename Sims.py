from random import *
class Human:
    def __init__(self, name, job=None, home=None, car=None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 0
        self.gladness = 50
        self.satiety = 20
        self.alive = True
    def get_home(self):
        self.home = House()
    def get_car(self):
        self.car = Auto(brands_of_car)
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
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("I bought fuel...")
            self.money -= 100
            self.car.fuel += 100
        if manage == "food":
            self.money -= 50
            self.home.food += 50
    def chill(self):
        self.gladness += 5
        self.home.mess += 10
    def clean_home(self):
        self.gladness -= 10
        self.home.mess = 0
    def to_repair(self):
        self.car.speed += 7
        self.money -= 5
    def day_index(self, day):
        print(f"Today the {day} of {self.name}'s life")
        print(f"Money - {self.money}")
        print(f"Gladness - {self.gladness}")
        print(f"Satiety - {self.satiety}")
        print(f"Food - {self.home.food}")
        print(f"Fuel car - {self.car.fuel}")
    def is_alive(self):
        if self.money <= -500:
            print("I have no money...")
            self.alive = False
        if self.gladness <= 0:
            print("Stressed out...")
            self.alive = False
        if self.satiety <= 0:
            print("Famine...")
            self.alive = False
    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Settled in the house...")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car... {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I don't have a job, I'm going to get job... {self.job.job} with salary {self.job.salary}")
        self.day_index(day)
        dice = randint(1,4)
        if self.satiety < 20:
            print("I'll go eat...")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I want to chill, but there mess \n So I'll clean the house...")
                self.clean_home()
            else:
                print("Lets chill...")
                self.chill()
        elif self.money < 0:
            print("Lets work...")
            self.work()
        elif self.car.speed < 15:
            print("I need to repair my car...")
        elif dice == 1:
            print("Lets chill...")
            self.chill()
        elif dice == 2:
            print("Start working...")
            self.work()
        elif dice == 3:
            print("Time to clean house...")
            self.clean_home()
        elif dice == 4:
            print("Time to eat...")
            self.eat()
class Auto:
    def __init__(self, brand_list):
        self.brand = choice(list(brand_list))
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
brands_of_car = {"BMW":{"fuel": 100, "speed": 100, "consumption": 6},
                 "Ferrari":{"fuel": 70, "speed": 300, "consumption": 20},
                 "Lada":{"fuel": 50, "speed": 40, "consumption": 20}}
job_list = {"IT":{"salary": 260, "gladness": -10},
            "Taxi":{"salary": 150, "gladness": -25},
            "Waiter":{"salary": 90, "gladness": -20}}
Zahar = Human("Zahar")
for day in range(8035):
    if Zahar.live(day) == False:
        break