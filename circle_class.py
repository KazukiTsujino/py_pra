import math
class Circle:
    def __init__(self,r):
        self.radius = r
    
    def area(self):
        return self.radius ** 2 * math.pi

user_radius = int(input("Please enter your radius"))   
circle1 = Circle(user_radius)
print(round(circle1.area(),2)) 