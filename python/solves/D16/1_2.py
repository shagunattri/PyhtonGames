def f(n):
    if n<2:
        fibo[n] = n
        return fibo[n]
    fibo[n] = f(n-1) + f(n-2)
    return fibo[n]

n = int(input())
fibo = [0] * (n + 1)
f(n)

fibo = [str(i) for i in fibo]
ans = "".join(fibo)
print(ans)