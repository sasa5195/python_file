from Tkinter import *
root = Tk()

e1 = Entry(root)
e2 = Entry(root)
l = Label(root)
def callback():
    total = sum(int(e.get()) for e in (e1, e2))
    l.config(text="answer = %s" % total)
b = Button(root, text="add them", command=callback)
for widget in (e1, e2, l, b):
    widget.pack()
b.mainloop()
