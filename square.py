class Square:
    square_list = []
    def __init__(self,length):
        self.length = length
        self.square_list.append(self.length)
    def __repr__(self):
        return "{} by {} by {} by {}".format(self.length,self.length,self.length,self.length)

squ1 = Square(10)
squ2 = Square(20)
squ3 = Square(30)
#print(Square.square_list)
print(squ1)