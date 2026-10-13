from tkinter import *


def submit_button():
    username = entry.get()
    print(f"Hello, {username}! you are welcome to appBrew")
    entry.config(state=DISABLED)

def delete_button():
    entry.delete(0, END)

def backspace_button():
    entry.delete(len(entry.get())-1, END)


window = Tk()
window.title("My Entry GUI")
entry = Entry(window, width=30, fg="blue", 
              bg="lightgray", font=("Arial", 14),
              bd=5, relief="sunken", justify="center")


submit = Button(window, text="Submit", command=submit_button)
delete = Button(window, text="Delete", command=delete_button)
backspace = Button(window, text="Backspace", command=backspace_button)


entry.pack(side=LEFT)
submit.pack(side=RIGHT)
delete.pack(side=RIGHT) 
backspace.pack(side=RIGHT)

window.mainloop()