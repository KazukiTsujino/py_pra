con = input("あなたのやりたいことは何ですか?\n")

with open("ans.txt","w",encoding="utf-8") as f:
    f.write(con)