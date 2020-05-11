import random

res = [i for i in range(1,1001) if i % 35 == 0]
result = random.sample(res,5)
print(result)