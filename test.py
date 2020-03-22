from tkinter import *

app = Tk()
app.title("TKINTER Test")
app.geometry("500x700")

menu = Menu(app)
app.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_command(label="Save As \t Ctrl+S")

helper = Menu(menu)
menu.add_cascade(label="Help", menu=helper)
def chat():
    print("Live chat started")

helper.add_command(label="Help")
helper.add_command(label="Live Chat", command=chat)

helper.add_command(label="Contact")
helper.add_command(label="Community")

filemenu = Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) 
filemenu.add_command(label='New') 
filemenu.add_command(label='Open...') 
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=app.quit) 

helpmenu = Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About') 

# menubutton = Menubutton(app, text="GFG")
# menubutton.grid()

# menu = Menu(menubutton)
# cVar = IntVar()
# menu.add_checkbutton ( label ='Contact', variable = cVar ) 

# menu.grid(row=0, column=0)


def showBtn():
    print("Show button clicked")

def checker():
    print("Male Checked")

def checker2():
    print("Female Checked")

button = Button(app, command=showBtn, text="Show", bg='orange',fg='white', height="2", width="10", pady="10", padx="10")
button.grid(row=0, column=0)


# not sure how to pass the arguements to the function, and how to recieve the returns
check_button = Checkbutton(app, command=checker, text="Male")
check_button.grid(row=1, column=0)

check_button2 = Checkbutton(app, command=checker2, text="Female")
check_button2.grid(row=1, column=2)

Label(app, text="Enter your name:").grid(row=2, column=0)

entry = Entry(app, width="10")
entry.grid(row=2, column=1)




Label(app, text="Enter your name: ").grid(row=3, column=0)
e = Entry(app, width=10)
e.grid(row=3, column=1)


buttonFrame = Frame(app)
Button(buttonFrame, text="Edit", fg="blue").grid(row=0, column=0)
Button(buttonFrame, text="Delete", fg="red").grid(row=0, column=1)
Button(buttonFrame, text="Update", fg="green").grid(row=0, column=2)
Button(buttonFrame, text="Read", fg="orange").grid(row=0, column=3)

buttonFrame.grid(row=4, column=0)


listbox = Listbox(app)
listbox.insert(1, "Python")
listbox.insert(1, "Javascript")
listbox.insert(1, "C++")
listbox.insert(1, "PHP")
listbox.grid(row=5, column=0)


msg = Message(app, text="Hello, this is a message", bg="lightgreen", width="300")
msg.grid(row=6, column=0)

Label(app, text="Gender").grid(row=7, column=0)
v = IntVar()
Radiobutton(app, text="Male", variable=v, value=1).grid(row=8, column=0)
Radiobutton(app, text="Female", variable=v, value=2).grid(row=8, column=1)

Scale(app, from_=0, to=40, orient=VERTICAL).grid(row=9, column=0)
Scale(app, from_=0, to=400, orient=HORIZONTAL).grid(row=10, column=0)

scrollbar = Scrollbar(app)

listbox = Listbox(app, yscrollcommand=scrollbar.set)
listbox.grid(row=11, column=0)
for i in range(200):
    listbox.insert(END, f"This is list {i+1}")

listbox.grid(row=13, column=0) 

scrollbar.config(command = listbox.yview)

T = Text(app, height=2, width=30)
T.grid(row=13, column=2)

T.insert(END, "hello world")


Top = Toplevel()
Top.title("Python")


Top.mainloop()


w = Spinbox(app, from_ = 0, to = 10).grid(row=0, column=4)



app.mainloop()

