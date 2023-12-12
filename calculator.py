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

l2 = Label(w,text="CALCULATOR",fg="white",bg="#272727",font=("Calibri",20))
l2.place(x=50,y=80)


w.mainloop()


def btns(num):#this function handles the function when the button clicked
    text = num.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())  
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    
    elif text == "del":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)
#setting the window size 
window= tk.Tk()
window.title("Calculator")
window.geometry("250x400")
window.configure(bg="gray" )

# Create an input field (Entry widget) for displaying and inputting numbers and expressions
entry = tk.Entry(window, font=("typewriter", 20))
entry.grid(row=0, column=0, columnspan=4, padx=15, pady=10) 

#buttons 
buttons = (
    "1", "2", "3", "+",
    "4", "5", "6", "-",
    "7", "8", "9", "*",
    ".", "0", "=", "/",
    "del",
)

c = 0  # column
r = 1  # row
button_index = 0

while button_index < len(buttons):
    button_text = buttons[button_index]
    btn = tk.Button(window, text=button_text, font=("typewriter", 15), padx=10, pady=10, width=5, height=2)
    #grid helps to the buttons to place in their respective rows and columns
    btn.grid(row=r, column=c, padx=5, pady=5)
    c += 1
    if c > 3:
        c = 0
        r += 1
    button_index += 1

row_index = 1
while row_index < 6:
    window.grid_rowconfigure(row_index, weight=1)
    row_index += 1

column_index = 0
while column_index < 4:
    window.grid_columnconfigure(column_index, weight=1)
    column_index += 1

child_index = 0
while child_index < len(window.winfo_children()):
    btn = window.winfo_children()[child_index]
    btn.bind("<Button-1>", btns)
    child_index += 1

window.mainloop()