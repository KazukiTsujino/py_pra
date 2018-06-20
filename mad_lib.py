import re
text ="""キリンは大昔から __複数名詞__ の興味の対象でした。
キリンは __複数名詞__ の中で一番背が高いのですが、科学者たちは
そのような長い __体の一部で__ をどうやって獲得したのか説明できません。
キリンの身長は　__数値__ __単位__　近くあり、その高さのほとんどは脚と
__体の一部__によるものです。
"""

def mad_libs(mls):
    hints = re.findall("__.*?__",mls)
    if hints is not None:
        for word in hints:
            q = "{}を入力:".format(word)
            new = input(q)
            mls = mls.replace(word, new, 1)
        print('\n')
        mls = mls.replace("\n", "")
        print(mls)
    else:
        print("引数mlsをちゃんと渡してよ！")

mad_libs(text)