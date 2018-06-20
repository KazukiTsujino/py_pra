import re

t = "__one____two____three__"
found = re.findall("__.*?__",t)
for num in found:
    print(num)
