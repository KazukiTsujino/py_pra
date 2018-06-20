class Horse:
    def __init__(self,name,owner):
        self.name = name
        self.owner = owner

class Rider:
    def __init__(self,name,lice):
        self.name = name
        self.license = lice

yutaka = Rider("Yutaka.Take","Pro")
kitasan = Horse("kitasan_black",yutaka)
print(kitasan.owner.name)
print(kitasan.owner.license)