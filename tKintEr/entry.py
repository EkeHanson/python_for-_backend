# Entry Widgets => is a textbox that allows the user to enter a single line of text. 
# It is used to accept user input in a GUI application.
from tkinter import *

windows = Tk()
windows.title("Entry Widget Example")
entry = Entry(windows, font=("Arial", 16),
               fg="#00FF00", bg="white",show="*",
               bd=5, relief=SUNKEN, justify=CENTER)  # Create an entry widget with a specific font, foreground color, background color, border width, and relief style. The text is centered within the entry widget.


def submit_entry():
    username = entry.get()
    print(f"Hello, {username} you are welcome to appBrew TechHub!")
    entry.config(state=DISABLED) 


def delete_entry():
    entry.delete(0, END)


def backspace_entry():
    entry.delete(len(entry.get()) - 1, END)


submit = Button(windows, text="Submit", font=("Arial", 16), command=submit_entry)
delete = Button(windows, text="Delete", font=("Arial", 16), bg="red", command=delete_entry)
backspace = Button(windows, text="Backspace", font=("Arial", 16), command=backspace_entry)



entry.pack(side=LEFT)
submit.pack(side=RIGHT)
delete.pack(side=RIGHT)
backspace.pack(side=RIGHT)
windows.mainloop()