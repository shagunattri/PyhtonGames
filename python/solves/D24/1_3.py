def rec(n):
    if n ==0:
        return n
    return (n-1) + n


n = int(input())

sum = rec(n)
print(sum)