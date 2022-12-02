from tkinter import *
from add_company import add_company
from time import strftime

def menu():
    root = Tk()
    root.title("Renuga Jewellers wholesales")
    root.state('zoomed')
    menubar = Menu(root)
    file = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='New', menu=file)
    file.add_command(label='Add', command= lambda:add_company(root))
    file.add_separator()
    file.add_command(label='Exit', command=root.destroy)
    root.configure(menu=menubar)
    root.mainloop()
menu()