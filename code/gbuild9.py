from tkinter import *


root = Tk()

canvas = Canvas(root, width=200, height=100)
canvas.pack()

blackline = canvas.create_line(0, 0, 50, 50)
redline = canvas.create_line(0, 100, 200, 50, fill="red")
greeenBox = canvas.create_rectangle(25, 25, 130, 60, fill = "green")

canvas.delete(redline)

root.mainloop()
