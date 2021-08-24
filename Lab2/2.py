from math import pi

class Spherical:

    def __init__(self, r: int):
        self.radius = r

    def changeR(self, radius: int):
        self.radius = radius

    def findVolume(self):
        return 4/3 * pi *  self.radius**3
        
    def findArea(self):
        return 4*pi* self.radius**2

    def __str__(self):
        return f"Radius ={self.radius} Volumn = {4/3 * pi *  self.radius**3} Area = {4*pi* self.radius**2}"
        

r1, r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(dir(R1))
print(R1)
R1.changeR(int(r2))
print(R1)