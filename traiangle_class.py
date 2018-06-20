class Triangle:
    def __init__(self,h,w):
        self.height = h
        self.width = w
    
    def area(self):
        return (self.height * self.width) / 2

height = int(input("Please enter the height."))
width = int(input("Please enter the width."))
traiangle1 = Triangle(height,width)
traiangle1_area = traiangle1.area()
print("The are of this triangle is " + str(traiangle1_area) + " ")