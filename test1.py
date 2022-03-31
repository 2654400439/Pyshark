from collections import Counter

a = ['111', '111', '22', '3']
tmp = list(Counter(a).keys())
try:
    tmp.remove('444')
except:
    pass
print(tmp)
