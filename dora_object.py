class Doraemon:
    def __init__(self,w,h,c):
        self.weight = w
        self.height = h
        self.color = c
        self.pocket_num = 3
        print("__Creating Now__\n" +
              "僕、ドラえもんです.")
    
    def pocket(self,nobi):
        self.nobi_ask = nobi
        self.pocket_num *= nobi ** 2
        
    

Dora1 = Doraemon(129.3, 129.3, "blue")
print(Dora1.pocket_num)
help = int(input("のび太くんのドラえもーんの掛け声は何回ですか?"))
Dora1.pocket(help)
print("以上より" + str(Dora1.pocket_num) + "個です")

"""print("僕の体重は" + str(Dora1.weight) + "kgだよ。意外に重いねテクノロジーだね")
print("なので、ダイエットします。")

momentum = int(input("何キロぐらい減らしたい?"))
Dora1.weight -= momentum
print("えい！\n" + str(round(Dora1.weight,1)) + "kgになったよ")"""





