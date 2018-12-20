from tkinter import *

root = Tk()

Label1 = Label(root, text="Name")
Label2 = Label(root, text="Password")
entry1 = Entry(root)
entry2 = Entry(root)


Label1.grid(row=0, sticky=E)
Label2.grid(row=1, sticky=E)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

c = Checkbutton(root, text="Keep me signed in")
c.grid(columnspan=2)

root.mainloop()