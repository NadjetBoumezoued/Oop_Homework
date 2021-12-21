#qst1
class Rectangle:
    def __init__(self, l, w):
        self.l = l
        self.w= w
    def area(self):
        return self.l*self.w
#qst2
class Vehicle:
    def __init__(self,max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
vehicule1 = Vehicle(240, 18)
print(vehicule1.max_speed, vehicule1.mileage)
#qst3
class Vehicle:
    pass
#qst4
class Vehicle:

    def __init__(self, max_speed, mileage):
 
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass
