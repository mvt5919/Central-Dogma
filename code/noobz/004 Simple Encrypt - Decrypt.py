# This is a verbose way of doing the next ex

# my_string = "AAAA"

# mapping = [('A', '1'), ('B','2'), ('C','3'), ('D','4'), ('E','5')]
# for k, v in mapping:
# 	my_string = my_string.replace(k, v)
# 	print(my_string)


#concise version
# mapping = dict(zip('ABCDE'), range(1,6))



# this doesnt work because using zip doesnt produce a proper dict I guess?
# keys = ['A', 'B', 'C', 'D', 'E']
# values = ['1', '2', '3', '4', '5']
# mapping = dict(zip(keys, values))




# mine LLL Need to include all letters

holder = str(input("Input encryption text"))

my_string = ("-".join(holder.upper()))

mapping = [('A', 'Z'), ('B','Y'), ('C','X'), ('D','W'), ('E','V'), ('F','U'), \
			('G','T'), ('H','S'), ('I','R'), ('J', 'Q'), ('K', 'P'), ('L','O'), \
			('M','N'), ('N','M'), ('O','L'), ('P', 'K'), ('Q','J'), ('R','I'), \
			('S','H'), ('T','G'), ('U','F'), ('V','E'), ('W','D'), ('X','C'), \
			('Y','B'),('Z','A')]

decrypt = [('1', 10), ('2', 20)]

for k, v in mapping:
	my_string = my_string.replace(k,v)
print(my_string)

for k, v in mapping:
	my_string = my_string.replace(v,k)
print(my_string)







