# Check password


def is_low(x):
	for i in x:
		if 'a'<=i and i<='z':
			return True
	return False


def is_up(x):
        for i in x:
                if 'A'<=i and i<='Z':
                        return True
        return False

def is_num(x):
        for i in x:
                if '0'<=i and i<='9':
                        return True
        return False

def is_other(x):
        for i in x:
                if i=='$' or i=='#' or i=='@':
                        return True
        return False

s = input().split(',')
lst = []


for i in s:
	length = len(i)
	if 6<= length and length <=12 and is_low(i) and is_up(i) and is_num(i) and is_other(i):
		lst.append(i)

print(','.join(lst))


