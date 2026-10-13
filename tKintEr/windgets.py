#Label is an area widget that holds text and/or images within a window


from tkinter import *

window = Tk()
window.geometry("420x420from ")
photo = PhotoImage(file="image.png", )  # Create an image for the label
photo = photo.subsample(5, 5)


label = Label(window, image=photo, text="appBrew TechHub", 
              font=('Arial', 16, "bold"),
                fg="#00ff00", bg="#997A7A",
                # relief=RAISED, bd=12) #pass the window(master) as a parameter to the label
                relief=SUNKEN, bd=12,
                padx=20, pady=20,
                compound='top') #pass the window(master) as a parameter to the label
label.pack() #pack the label into the window
window.mainloop() # Keep the window open until the user closes it, listen for events
