from tkinter import *

windows = Tk()
windows.title("Calculator")

entry = Entry(windows, font=("Arial", 16),
              fg="#00FF00", bg="white",
              bd=5, relief=SUNKEN, justify=RIGHT)
entry.pack(fill=X)

def press(value):
    entry.insert(END, value)

def clear_entry():
    entry.delete(0, END)

def backspace_entry():
    entry.delete(len(entry.get()) - 1, END)

# def calculate():
#     try:
#         result = eval(entry.get())
#         entry.delete(0, END)
#         entry.insert(0, result)
#     except:
#         entry.delete(0, END)
#         entry.insert(0, "Error")


def calculate():
    try:
        expr = entry.get()
        expr = expr.replace("sin", "math.sin(math.radians")
        expr = expr.replace("cos", "math.cos(math.radians")
        expr = expr.replace("tan", "math.tan(math.radians")
        result = eval(expr, {"math": math, "__builtins__": {}})
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")


# ----- Row 1 -----
row1 = Frame(windows)
row1.pack()
Button(row1, text="1", font=("Arial", 16), width=5, command=lambda: press("1")).pack(side=LEFT)
Button(row1, text="2", font=("Arial", 16), width=5, command=lambda: press("2")).pack(side=LEFT)
Button(row1, text="3", font=("Arial", 16), width=5, command=lambda: press("3")).pack(side=LEFT)

# ----- Row 2 -----
row2 = Frame(windows)
row2.pack()
Button(row2, text="4", font=("Arial", 16), width=5, command=lambda: press("4")).pack(side=LEFT)
Button(row2, text="5", font=("Arial", 16), width=5, command=lambda: press("5")).pack(side=LEFT)
Button(row2, text="6", font=("Arial", 16), width=5, command=lambda: press("6")).pack(side=LEFT)

# ----- Row 3 -----
row3 = Frame(windows)
row3.pack()
Button(row3, text="7", font=("Arial", 16), width=5, command=lambda: press("7")).pack(side=LEFT)
Button(row3, text="8", font=("Arial", 16), width=5, command=lambda: press("8")).pack(side=LEFT)
Button(row3, text="9", font=("Arial", 16), width=5, command=lambda: press("9")).pack(side=LEFT)

# ----- Row 4 -----
row4 = Frame(windows)
row4.pack()
Button(row4, text="+", font=("Arial", 16), width=5, command=lambda: press("+")).pack(side=LEFT)
Button(row4, text="=", font=("Arial", 16), width=5, command=calculate).pack(side=LEFT)
Button(row4, text="C", font=("Arial", 16), width=5, bg="red", command=clear_entry).pack(side=LEFT)

# ----- Row 5 -----
row5 = Frame(windows)
row5.pack()
Button(row5, text="⌫", font=("Arial", 16), width=5, command=backspace_entry).pack(side=LEFT)

windows.mainloop()


