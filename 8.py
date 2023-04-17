from itertools import *
s = "РУСЛАН"
a = ["".join(x) for x in set(product(s, repeat=5))]
a = [i for i in a if i.count("У") <= 1 and i.count("А") <= 1]
print(a)
print(len(a))