import sys

select = int(input("1 for Fahrenheit to Celsius\n2 for Celsius to Fahrenheit"))

if select == 1:
	fconv = int(input("Input temp Fahrenheit"))
	result = (fconv - 32) / 1.8
	print(result)
	sys.exit() 
if select == 2:
	cconv = int(input("Input temp Celsius"))
	result2 = (cconv * 1.8) + 32
	print(result2)
	sys.exit()
else:
	print("Invalid Input")
	sys.exit()
