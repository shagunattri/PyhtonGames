def even(x):
    return x%2 == 0

evenno = filter(even,range(1,21))
print(list(evenno))