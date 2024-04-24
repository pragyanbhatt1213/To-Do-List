# TO DO LIST!!!

from tkinter import * # importing tkinter
from tkinter import messagebox

def new(): # Adding Task if given
    task = my_entry.get()
    if task != "":
        n.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask(): # Deleting Task
    n.delete(ANCHOR)
    
x = Tk()
x.geometry('500x450+500+200') 
x.title('To Do list')
x.config(bg='#0C2945')
x.resizable(width=False, height=False)

frame = Frame(x)
frame.pack(pady=10)

n = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#355B7E',
    highlightthickness=0,
    selectbackground='#A6698D',
    activestyle="none",
    
)
n.pack(side=LEFT, fill=BOTH)

task_list = [ # Default list
    'Eat Time',
    'Drink water',
    'Go Tution',
    'Do Homework',
    'Take a nap',
    'Learn something',
    'Coding',
    'Eat Fruits'
    ]

for item in task_list: # Inserting
    n.insert(END, item)

q = Scrollbar(frame)
q.pack(side=RIGHT, fill=BOTH)

n.config(yscrollcommand=q.set)
q.config(command=n.yview)

my_entry = Entry(x,
    font=('times', 24))

my_entry.pack(pady=20)

button_frame = Frame(x)
button_frame.pack(pady=20)

addTask_btn = Button( # Adding 'Add Task' Button
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#9C69A6',
    padx=20,
    pady=10,
    command=new
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button( # Adding 'Delete Task' Button
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#74D9D7',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)
x.mainloop()
