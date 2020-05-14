li = [12,23,35,70,88,120,155]
li = [li[i] for i in range(len(li)) if i not in (0,4,5,)]
print(li)
