# binary conversion and factor of 5

def check(x):
	return int(x,2)%5 == 0

data = input().split(',')

data = list(filter(check,data))

print(",".join(data))
