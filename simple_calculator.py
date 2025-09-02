import math
import tkinter as tk

def on_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current[:-1])

def calculator():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def squre_root():
    try:
        value = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(math.sqrt(value)))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def square():
    try:
        value = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(value**2))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def cube():
    try:
        value = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(value**3))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("CALCULATOR")
root.geometry("350x480")

entry = tk.Entry(root, font=("Arial",20), borderwidth=5, relief="ridge", justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, ipady=8, padx=10, pady=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

# number/operator buttons
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for b in row:
        if b == "=":
            action = calculator
        else:
            action = lambda x=b: on_click(x)
        tk.Button(frame, text=b, font=("Arial",16), command=action).pack(side="left", expand=True, fill="both")

# special buttons
frame = tk.Frame(root)
frame.pack(expand=True, fill="both")

specials = [
    ("C", clear),
    ("<--", backspace),
    ("√", squre_root),
    ("x²", square),
    ("x³", cube),
    ("x^y", lambda: on_click("**"))
]

for (label, action) in specials:
    tk.Button(frame, text=label, font=("Arial",16), command=action).pack(side="left", expand=True, fill="both")

root.mainloop()
