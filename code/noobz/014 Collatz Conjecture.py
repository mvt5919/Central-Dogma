value = int(input("Collatz conjecture sequence from input: \n"))

while value != 1:
	if value % 2 == 0:
		value = value / 2
		print(int(value))
	else:
		value = (value * 3) + 1
		print(int(value))