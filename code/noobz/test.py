import string

# import string condensed method of going through a-z in dict

d = dict.fromkeys(string.ascii_lowercase)
for counter, value in enumerate(d, 1):
	print(counter, value) 

