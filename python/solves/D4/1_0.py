#upper and lower case

word = input()

upper,lower = 0,0

for i in word:
	if 'a'<=i and i<='z':
		lower+=1
	if 'A'<=i and i<='Z':
		upper+=1

print("Upper case {0}\n Lower case {1}".format(upper,lower))
