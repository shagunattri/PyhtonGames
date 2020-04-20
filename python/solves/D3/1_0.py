#word count and sort

str = input().split()

for i in str:
	if str.count(i) > 1:
		str.remove(i)

str.sort()
print(" ".join(str))
