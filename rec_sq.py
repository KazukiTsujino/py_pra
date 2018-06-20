class Shape:
    def __init__(self):
        pass
    
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def calculate_perimeter(self):
        return (self.width + self.height) * 2
    
    def calculate_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self,len):
        self.length = len
    
    def calculate_perimeter(self):
        return self.length * 4
   
    def calculate_area(self):
        return self.length ** 2
    
    def change_size(self,len_dif):
        self.length += len_dif
        if self.length < 0:
            self.length = 0

#例外処理加えてみる
"""
while True:
    try:
        width = int(input("Enter width."))
        height = int(input("Enter height."))
        length = int(input("Enter length."))
        break
    except ValueError:
        print("Please enter the integer.")

rec1 = Rectangle(width,height)
rec1_area = rec1.calculate_area()
rec1_peri = rec1.calculate_perimeter()

squ1 = Square(length)
que = input("Do you want to change the size of area?(y/n)")
if que == "y":
    dif = int(input("Enter the difference."))
    squ1.change_size(dif)
else:
    pass
squ1_area = squ1.calculate_area()
squ1_peri = squ1.calculate_perimeter()

print("--Rectangle--\n" + "area => {}\n".format(rec1_area) + "perimeter => {}\n".format(rec1_peri))
print("--Square--\n" + "area => {}\n".format(squ1_area) + "perimeter => {}\n".format(squ1_peri))
"""
rec1 = Rectangle(10,10)
squ1 = Square(5)
rec1.what_am_i()
squ1.what_am_i()





