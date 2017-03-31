from Tkinter import *
from tkFileDialog import askopenfilename

def getfile():
    filename = askopenfilename() 
    print(filename)

root = Tk()
root.title("Hashing Tool")
root.geometry("600x300")

frame = Frame(root)
frame.pack()
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )
button = Button(frame, text="Choose File", fg="black", command=getfile)
button.pack( side = BOTTOM)
root.mainloop()

