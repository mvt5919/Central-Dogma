from tkinter import *


def doNothing():
	print("Do nothing I wont")

root = Tk()

# ******* MAIN MENU *******

menu = Menu(root)
root.config(menu=menu)

submenu = Menu(menu)
menu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="New Project...", command=doNothing)
submenu.add_command(label="New...", command=doNothing)
submenu.add_separator()
submenu.add_command(label="Exit", command=doNothing)

editmenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Redo", command=doNothing)

# ****** The Toolbar ******

toolbar = Frame(root, bg="blue")

insertbutt = Button(toolbar, text="Insert image", command=doNothing)
insertbutt.pack(side=LEFT, padx=2, pady=2)
printbutt = Button(toolbar, text="Print", command=doNothing)
printbutt.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP, fill=X)


#            STATUS BAR

status = Label(root, text="Preparing to do nothing", bd = 1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)


root.mainloop()
