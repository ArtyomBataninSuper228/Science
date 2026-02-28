from itertools import *

num = 0
res = 0
for i in product('ЁЛОЧЩЬ', repeat=6):
    s = "".join(i)
    num += 1
    if 'Ь' in s and s[0] != 'Ь':
        num_s = 0
        for j in s:
            if i in ["Щ", "Л", "Ч"]:
                num_s += 1
        if num_s <= 2:
            res = num
print(res, num)