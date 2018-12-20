from tkinter import *

# Commands
def refreshGraph():
	
	graphOne = canvas.create_rectangle(20, 200, 50, 400, fill = "green")
	graphTwo = canvas.create_rectangle(80, 200, 110, 400, fill="red")
	graphThree = canvas.create_rectangle(140, 200, 170, 400, fill="blue")

def clearGraph():
	canvas.delete(ALL)

def onlyOne():
	canvas.delete(graphTwo)
	canvas.delete(graphThree)

def onlyTwo():
	canvas.delete(graphOne)
	canvas.delete(graphThree)

def onlyThree():
	canvas.delete(graphOne)
	canvas.delete(graphTwo)






ghone = int(input("Input graph height one"))
ghtwo = int(input("Input graph height two"))
ghthree = int(input("Input graph height three"))






root = Tk()
root.title("Graph Builder")


# Graph Menus and Tools

mainmenu = Menu(root)
root.config(menu=mainmenu)

subMenu = Menu(mainmenu)
mainmenu.add_cascade(label="GTools", menu=subMenu)
subMenu.add_command(label="Refresh Graph", command=refreshGraph)
subMenu.add_command(label="Clear Graph", command=clearGraph)


# Toolbar

toolbar = Frame(root, bg="white")

g1button = Button(toolbar, text="G1 Only", command=onlyOne)
g1button.pack(side=LEFT)
g2button = Button(toolbar, text="G2 Only", command=onlyTwo)
g2button.pack(side=LEFT)
g3button = Button(toolbar, text="G3 Only", command=onlyThree)
g3button.pack(side=LEFT)

toolbar.pack(side=TOP, fill=X)


# Canvas

canvas = Canvas(root, width= 600, height= 400)
canvas.pack(side=BOTTOM)


# params point top left x y, width, height ***** move 1st and 3rd values by 60 to add new graph
graphOne = canvas.create_rectangle(20, 200, 50, ghone, fill = "green")
graphTwo = canvas.create_rectangle(80, 200, 110, ghtwo, fill="red")
graphThree = canvas.create_rectangle(140, 200, 170, ghthree, fill="blue")

root.mainloop()


#need to fix show only not working after refresh