from tkinter import *
import tkinter.messagebox


root = Tk()

tkinter.messagebox.showinfo("Window Title", "monkeys can live up to 300 years.")

answer = tkinter.messagebox.askquestion("Quiz 1", "IS this window open")

if answer == "yes":
	print("Silly Face")

root.mainloop()
