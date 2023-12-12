from tkinter import *
from tkinter import ttk 
from tkinter.ttk import Progressbar
import random
import time
import datetime
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import *
import tkinter as tk
from tkinter.font import Font

#SPLASH SCREEN

w = Tk()

width_of_window = 427
height_of_window = 250

screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()

x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)

w.geometry("%dx%d+%d+%d"%(width_of_window,height_of_window,x_coordinate,y_coordinate))
w.overrideredirect(1)

s=ttk.Style() 
s.theme_use("clam")
s.configure("red.Horizontal.TProgressbar",fg="red",bg="#4f4f4f")
progress = Progressbar(w,style="white.Horizontal.TProgressbar",orient=HORIZONTAL,length = 427,mode='determinate')

def progress_bar():
    l1 = Label(w,text = "Loading.....", fg = "white", bg = "#272727",font= ("Calibri",10))
    l1.place(x=0,y=210)
    #l1.grid(padx=0,pady=210)
    
    import time
    r = 0
    for i in range(100):
        progress['value']=r
        w.update_idletasks()
        time.sleep(0.05)
        r = r+1
    w.destroy()
    
progress.place(x=0,y=235)

#adding frame

Frame(w,width=427,height=241,bg = "#272727").place(x=0,y=0)
btn = Button(w,width=10, height=1,text="Get Started",command = progress_bar ,border=0,fg="#272727")
btn.place(x=170,y=200)

#adding label

l2 = Label(w,text="TO-DO LIST",fg="white",bg="#272727",font=("Calibri",20))
l2.place(x=50,y=80)


w.mainloop()



def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter task to perform")

def delete_task():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        messagebox.showwarning("Warning", "Please select a task to be deleted.")

def toggle_task():
    try:
        index = listbox.curselection()
        task_text = listbox.get(index)
        if task_text.startswith("✓ "):
            task_text = task_text[2:]
        else:
            task_text = "✓ " + task_text
        listbox.delete(index)
        listbox.insert(index, task_text)
    except:
        messagebox.showwarning("Warning", "Please select the task you've done.")


window = tk.Tk()
window.title("To-Do List")
window.configure(bg="grey") 

# Create an entry widget to add tasks
entry = tk.Entry(window, width=50)
entry.pack(padx=10, pady=5, side=tk.TOP)  

# Create a frame to hold the buttons
button_frame = tk.Frame(window, bg="pink")
button_frame.pack(padx=10, pady=5)


button_font = Font(family="Arial", size=12, weight="bold")

# an "Add Task" button
add_button = tk.Button(button_frame, text="Add Task", command=add_task, font=button_font)
add_button.pack(side=tk.LEFT, padx=5)

# a "Delete Task" button
delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, font=button_font)
delete_button.pack(side=tk.LEFT, padx=5)

# a "Done Task" button
toggle_button = tk.Button(button_frame, text="Done Task", command=toggle_task, font=button_font)
toggle_button.pack(side=tk.LEFT, padx=5)

# a listbox to display tasks
listbox = tk.Listbox(window, width=50)
listbox.pack(padx=10, pady=5)

# a scrollbar for the listbox
scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Link the scrollbar to the listbox
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Start the Tkinter event loop
window.mainloop()