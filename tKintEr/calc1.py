from tkinter import *

# ---------- Window setup ----------
window = Tk()
window.title("Calculator")
window.geometry("320x420")
window.config(bg="#222222")
window.resizable(False, False)

# ---------- Display (Entry) ----------
expression = ""  # will hold the math expression as a string

display = Entry(
    window,
    font=("Arial", 24),
    fg="#00FF00",
    bg="#111111",
    bd=8,
    relief=SUNKEN,
    justify=RIGHT,
    insertbackground="#00FF00",  # cursor color
)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=15, ipady=12, sticky="nsew")

# ---------- Functions ----------
def press(value):
    """Add a character to the expression and show it."""
    global expression
    expression += str(value)
    display.delete(0, END)
    display.insert(0, expression)

def clear():
    """Clear the whole display."""
    global expression
    expression = ""
    display.delete(0, END)

def backspace():
    """Remove the last character."""
    global expression
    expression = expression[:-1]
    display.delete(0, END)
    display.insert(0, expression)

def calculate():
    """Evaluate the expression safely."""
    global expression
    try:
        # Restrict eval to digits and operators only (basic safety)
        allowed = set("0123456789+-*/.()")
        if not set(expression).issubset(allowed):
            raise ValueError("Invalid characters")
        result = str(eval(expression))
        display.delete(0, END)
        display.insert(0, result)
        expression = result
    except ZeroDivisionError:
        display.delete(0, END)
        display.insert(0, "Error: ÷0")
        expression = ""
    except Exception:
        display.delete(0, END)
        display.insert(0, "Error")
        expression = ""

# ---------- Button layout ----------
buttons = [
    ("C",  1, 0), ("AC", 1, 1), ("/", 1, 2), ("*", 1, 3),
    ("7",  2, 0), ("8",  2, 1), ("9", 2, 2), ("-", 2, 3),
    ("4",  3, 0), ("5",  3, 1), ("6", 3, 2), ("+", 3, 3),
    ("1",  4, 0), ("2",  4, 1), ("3", 4, 2), ("=", 4, 3),
    ("0",  5, 0), (".",  5, 1),("%",  5, 2), ("^", 5, 3)
]

for (text, row, col) in buttons:
    if text == "C":
        cmd = clear
        color = "#FF5555"
    elif text == "AC":
        cmd = backspace
        color = "#FFAA33"
    elif text == "=":
        cmd = calculate
        color = "#33AA55"
    elif text in "+-*/":
        cmd = lambda t=text: press(t)
        color = "#4477AA"
    else:
        cmd = lambda t=text: press(t)
        color = "#444444"

    Button(
        window, text=text, font=("Arial", 18, "bold"),
        fg="white", bg=color, activebackground="#666666",
        command=cmd, bd=2, relief=RAISED
    ).grid(row=row, column=col, padx=4, pady=4, ipadx=8, ipady=10, sticky="nsew")

# Make the grid expand evenly
for i in range(4):
    window.grid_columnconfigure(i, weight=1)
for i in range(1, 6):
    window.grid_rowconfigure(i, weight=1)

window.mainloop()

# pip install pyinstaller
# pyinstaller --onefile --noconsole calc1.py