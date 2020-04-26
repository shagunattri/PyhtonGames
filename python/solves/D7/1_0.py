class Divisible:
	def div_seven(self,no):
		for number in range(no + 1):
			if number%7 == 0: yield number



div = Divisible()
gen = div.div_seven(int(input("Insert a number \n")))

for number in gen:
	print(number)
