li = [5,6,7,45,22,12,24]

def iseven(n):
    return n%2!=0


lis = list(filter(iseven,li))
print(lis)