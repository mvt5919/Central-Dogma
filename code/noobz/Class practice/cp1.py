# convert integer to roman numeral class

class problem_one:
	def int_to_roman(self, num):
		val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
		symb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

		roman_num = ''
		i = 0
		while num > 0:
			for _ in range(num // val[i]):
				roman_num += symb[i]
				num -= val[i]
			i += 1
		return roman_num


print(problem_one().int_to_roman(1))
print(problem_one().int_to_roman(4000))