import os
from tkFileDialog import askopenfilename
from Tkinter import *


content = ''
file_path = ''

def open_file():
    global content
    global file_path

    filename = askopenfilename()
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()
    file_path = os.path.dirname(filename)+filename
    entry.delete(0, END)
    entry.insert(0, file_path)
    return content

def process_file(content):
    print content
    print sum(int(e.get()) for e in (e1, e2))
    

root = Tk()
root.title('')
root.geometry()
mf = Frame(root)
mf.pack()

f1 = Frame(mf, width=300, height=150)
f1.pack(fill=Y)
f2 = Frame(mf, width=300, height=150)
f2.pack()


Label(f1,text="Select Your File (Only txt files)").grid(row=0, column=0, sticky='e')
Label(f1,text="Num1 :-").grid(row=1, column=0, sticky='e')
Label(f1,text="Num2 :-").grid(row=2, column=0, sticky='e')
entry = Entry(f1, width=50, textvariable=file_path)
entry.grid(row=0,column=1,padx=2,pady=2,sticky='we',columnspan=25)
e1 = Entry(f1, width=50)
e1.grid(row=1,column=1,padx=2,pady=2,sticky='we',columnspan=25)
e2 = Entry(f1, width=50)
e2.grid(row=2,column=1,padx=2,pady=2,sticky='we',columnspan=25)
Button(f1, text="Browse", command=open_file).grid(row=0, column=27, sticky='ew', padx=8, pady=4)
Button(f2, text="Process Now", width=32, command=lambda: process_file(content)).grid(sticky='ew', padx=10, pady=10)


root.mainloop()

