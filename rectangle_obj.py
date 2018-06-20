class Rectangle:
    def __init__(self,w,h):
        self.width = w
        self.height = h
    
    def area(self):
        return self.width * self.height
    
    def change_size(self,w,h):
        self.width = w
        self.height = h

rectangle = Rectangle(3,4)
print(rectangle.area())
print("You can change size.\n")
width = int(input("Please enter the width. "))
height = int(input("Please enter the height. "))
rectangle.change_size(width,height)
print(rectangle.area())
