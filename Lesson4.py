from random import *
class Student:
    def __init__(self, name, age, education):
        self.name = name
        self.age = age
        self.education = education
        self.progress = 0
        self.gladness = 50
        self.alive = True
    def to_study(self):
        print("Time to study")
        self.gladness-=5
        self.progress+=0.5
    def to_sleep(self):
        print("Time to sleep")
        self.gladness+=3
    def to_chill(self):
        print("Time to chill")
        self.gladness+=5
        self.progress-=0.33
    def if_alive(self):
        if self.progress < -5:
            print("Cast out...")
            self.alive = False
        if self.gladness <=0:
            print("Stressed out...")
            self.alive = False
        if self.progress >= 6:
            print("Passed externally...")
            self.alive = False
    def printData(self):
        print(f"Gladness =  {self.gladness}")
        print(f"Progress = {self.progress}")
    def live(self,day):
        print(f"Day: {day} of life")
        live_cube = randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.printData()
        self.if_alive()
Zaharij = Student("Krakovetskyj Zahaharij", 13, "ItStep")
for day in range(365):
    if Zaharij.alive==False:
        print("Game over!")
        break
    Zaharij.live(day)