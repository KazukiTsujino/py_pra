class Hexagon:
    def __init__(self,len):
        self.length = len
    
    def calculator_perimiter(self):
        return self.length * 6
length = int(input("Please enter the length of one side of hexagon."))
hexagon1 = Hexagon(length)
perimiter = hexagon1.calculator_perimiter()
print(perimiter)