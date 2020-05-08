def bsearchasc(array,target):
    lower = 0
    upper = len(array)
    print("array length:".upper)
    while lower < upper:
        x = ((lower + upper)) //2
        print("Middle Value:",x)
        value = array[x]
        if target == value:
            return x
        elif target > value:
            lower = x
        elif target < value:
            upper = x

array = [1,3,5,6,8,9,12,14,21,43,54,77,88,89]
print("The value found at index:",bsearchasc(array,54))