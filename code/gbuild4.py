from tkinter import *

root = Tk()


def printName(event):
	print("My name is Bucky")

button1 = Button(root, text="Print Bucky")
button1.bind("<Button-1>", printName)
button1.pack()

root.mainloop()
