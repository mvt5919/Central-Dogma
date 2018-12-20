import random



print("Name Generator \nPress 1 to Generate")

var = int(input())

parta = random.randint(0,4)
partb = random.randint(0,4)

first = ["bill","sally","sue", "joe", "loue"]
last = ["smith","write","dingle", "Anaheim","Taurus"]

print(first[parta] + " " + last[partb])

