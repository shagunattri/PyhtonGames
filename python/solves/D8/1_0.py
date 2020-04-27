a = input().split()

dict = {}

for i in a:
    i = dict.setdefault(i,a.count(i))

dict = sorted(dict.items())

for i in dict:
    print("%s:%d"%(i[0],i[1]))

 #2
from collections import Counter

ss = input().split()
ss = Counter(ss)
ss =sorted(ss.items())

for i in ss:
    print("%s:%d"%(i[0],i[1]))



#3

from pprint import pprint

p = input().split()
pprint({i:p.count(i) for i in p})
