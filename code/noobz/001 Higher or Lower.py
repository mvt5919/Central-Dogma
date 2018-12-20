import sys
import random

number = random.randint(1,99)

print(number)



attempt = 0

while attempt < 4:
	var = int(input("Guess number"))

	if var > number:
		print("too high")
		attempt += 1
		print("attempt {}".format(attempt))
		
	if var < number:
		print("too Low")
		attempt+= 1
		print("attempt {}".format(attempt))
		
	if var == number:
		print("correct")
		sys.exit()

print("too many guesses")
