from tkinter import *

count = 0
count = 0
def click():
    global count
    count += 1
    button.config(text=f"Clicked {count} times")


window = Tk()

photo = PhotoImage(file="image.png")  # Create an image for the button
button = Button(window, text="Click Me!",
# button = Button(window, image=photo, text="Click Me!",
                 command=click,
                #  command=lambda: print("Button Clicked!"),
                 font=('Comic Sans MS', 16, "bold"),
                 bg="#00ff00", fg="#000000",
                 relief=RAISED, bd=12,
                #  relief=SUNKEN, borderwidth=5,
                #  padx=20, pady=20, compound='bottom',  #pass the window(master) as a parameter to the button
                 activebackground="#6e796e", activeforeground="#000000",
                #  state=DISABLED ACTIVE
                )

button.pack()
window.mainloop()