# GUI
# TKinter

#Widgets => GUI elements: buttons, text boxes, labels, etc.
# Windows => The container to hold/contain the widgets

from tkinter import  *

window = Tk()  # Create a window (Instance of the window)
# window.geometry("420x420")  # Set the size of the window
# window.title("My First GUI")  # Set the title of the window
# # window.iconphoto(False, PhotoImage(file="elon.webp"))
# icon = PhotoImage(file="image.png")  # Create an icon for the window
# window.iconphoto(True, icon)  # Set the icon for the window
# window.config(background="#000000")  # Set the background color of the window

window.mainloop() # Keep the window open until the user closes it, listen for events
