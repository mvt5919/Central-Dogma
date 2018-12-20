import random

# ROCK       1
# PAPER      2
# SCISSORS   3
# LIZARD     4
# SPOCK      5

y = str(input("Player hand"))
hand = random.randint(1,5)

d = {1: "Rock", 2: "Paper", 3: "Scissors", 4: "Lizard", 5: "Spock"}

x = d[hand]
print(x)

if (y == "Spock" and x == "Lizard") or (y == "Lizard" and x == "Scissors") or (y == "Scissors" and x == "Paper") \
or (y == "Paper" and x == "Rock") or (y == "Rock" and x == "Spock") or (y=="Rock" and x =="Scissors"):
	print("win")

else:
	print("lose") 



