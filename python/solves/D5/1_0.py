#square odd no

lst = input().split(',')

seq = []
lst = [int(i) for i in lst]
for i in lst:
	if i%2 != 0:
		i = i*i
		seq.append(i)


seq = [str(i) for i in seq]
print(",".join(seq))
