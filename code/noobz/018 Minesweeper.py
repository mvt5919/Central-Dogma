import random
import sys

def displayv():
	print("", v1, "\n" , v2, "\n" , v3, "\n" , v4, "\n" , v5, "\n" ,
      v6, "\n" , v7, "\n", v8, "\n", v9)

def displayr():
	print("", r1, "\n" , r2, "\n" , r3, "\n" , r4, "\n" , r5, "\n" ,
      r6, "\n" , r7, "\n", r8, "\n", r9)

def coord_select():
	rowa = str(input("\nEnter row"))
	column = int(input("\nEnter column"))
	conversions = {"1":r1, "2":r2, "3":r3, "4":r4, "5":r5, "6":r6, "7":r7, "8":r8, "9":r9}
	row = conversions[rowa]
	if row[column-1] == "O":
		print("fucking dead")
		sys.exit()
	if row[column-1] != "O":
		row[column-1] = "_"

def minelay():
	mine_loc = {}
	randa = random.randint(1, 9)
	randb = random.randint(1, 9)
	mine = "O"
	x=0
	while x < 10:
	
		conversions = {1:r1, 2:r2, 3:r3, 4:r4, 5:r5, 6:r6, 7:r7, 8:r8, 9:r9}
		c = random.randint(1,9)
		rn = random.randint(1,9)
		r = conversions[rn]
		mine_loc.update({rn:c})
		if r[c - 1] == mine:
			print(".") 
		if r[c - 1] != mine:
			r[c - 1] = mine
			
			x += 1
	print(mine_loc)
		
def realboard():		
	r1 = ["X","X","X","X","X","X","X","X","X"]
	r2 = ["X","X","X","X","X","X","X","X","X"]
	r3 = ["X","X","X","X","X","X","X","X","X"]
	r4 = ["X","X","X","X","X","X","X","X","X"]
	r5 = ["X","X","X","X","X","X","X","X","X"]
	r6 = ["X","X","X","X","X","X","X","X","X"]
	r7 = ["X","X","X","X","X","X","X","X","X"]
	r8 = ["X","X","X","X","X","X","X","X","X"]
	r9 = ["X","X","X","X","X","X","X","X","X"]
	return r1, r2, r3, r4, r5, r6, r7, r8, r9

def visualboard():		
	v1 = ["X","X","X","X","X","X","X","X","X"]
	v2 = ["X","X","X","X","X","X","X","X","X"]
	v3 = ["X","X","X","X","X","X","X","X","X"]
	v4 = ["X","X","X","X","X","X","X","X","X"]
	v5 = ["X","X","X","X","X","X","X","X","X"]
	v6 = ["X","X","X","X","X","X","X","X","X"]
	v7 = ["X","X","X","X","X","X","X","X","X"]
	v8 = ["X","X","X","X","X","X","X","X","X"]
	v9 = ["X","X","X","X","X","X","X","X","X"]

def num_lay():
	rowa = str(input("\nR: "))
	iconv = int(rowa)
	column = int(input("\nC: "))
	conversions = {"1":r1, "2":r2, "3":r3, "4":r4, "5":r5, "6":r6, "7":r7, "8":r8, "9":r9}
	row = conversions[rowa]
	a1 = conversions[str(iconv+1)]
	a2 = conversions[str(iconv-1)]
	if row[column-1] == "O":
		print("fucking dead")
		sys.exit()
	if row[column-1] != "O":
		row[column-2] = "1"
		row[column] = "1"
		a1[column-1] = "1"
		a2[column-1] = "1"
		a1[column] = "1"
		a1[column-2] = "1"
		a2[column] = "1"
		a2[column-2] = "1"


#possible dict k/v storage for mine locations would be easier than symbol checks.
#if space next to mine is x make 1 if space is 1 make 2 simple addition for touch checks


r1, r2, r3, r4, r5, r6, r7, r8, r9 = realboard()
minelay()

displayr()
num_lay()
displayr()


# coord_select()
# display()
