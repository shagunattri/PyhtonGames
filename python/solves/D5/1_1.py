# bank Deposit and withdraw

total = 0
while True:
	s = input().split()
	if not s:
		break
	
	type,no = map(str,s)

	if type == 'D':
		total += int(no)

	if type == 'W':
		total -= int(no)

print(total)	
