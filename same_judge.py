class Vegetable:
    def __init__(self,veg_name):
        self.name = veg_name

def same_judge(a,b):
    return a is b

veg1 = Vegetable("carrot")
veg2 = veg1

print(same_judge(veg1,veg2))

veg3 = Vegetable("carrort")
print(same_judge(veg1,veg3))



