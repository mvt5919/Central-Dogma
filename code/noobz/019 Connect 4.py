r0 = ["_","_","_","_","_","_","_"]
r1 = ["X","X","X","X","X","X","X"]
r2 = ["X","X","X","X","X","X","X"]
r3 = ["X","X","X","X","X","X","X"]
r4 = ["X","X","X","X","X","X","X"]
r5 = ["X","X","X","X","X","X","X"]
r6 = ["X","X","X","X","X","X","X"]



def value_update():
	c1 = [r0[0], r1[0], r2[0], r3[0], r4[0], r5[0], r6[0]]
	c2 = [r0[1], r1[1], r2[1], r3[1], r4[1], r5[1], r6[1]]
	c3 = [r0[2], r1[2], r2[2], r3[2], r4[2], r5[2], r6[2]]
	c4 = [r0[3], r1[3], r2[3], r3[3], r4[3], r5[3], r6[3]]
	c5 = [r0[4], r1[4], r2[4], r3[4], r4[4], r5[4], r6[4]]
	c6 = [r0[5], r1[5], r2[5], r3[5], r4[5], r5[5], r6[5]]
	c7 = [r0[6], r1[6], r2[6], r3[6], r4[6], r5[6], r6[6]]
	return c1, c2, c3, c4, c5, c6, c7

def place_chip():
	c = int(input("C: "))
	r0[c -1] = "O"

print("\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(r0, r1, r2, r3, r4, r5, r6))

match =["O"]

place_chip()
c1, c2, c3, c4, c5, c6, c7 = value_update()



clist = {0:c1, 1:c2, 2:c3, 3:c4, 4:c5, 5:c6, 6:c7}
for x in range(0,7):
	if bool(set(clist[x]).intersection(match)) == True and not r6[x] == "O":
		r6[x] = "O"
	else:
		print("duplicate")


r0 = ["_","_","_","_","_","_","_"]



print("\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(r0, r1, r2, r3, r4, r5, r6))
